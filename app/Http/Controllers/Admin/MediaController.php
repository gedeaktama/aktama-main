<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Str;

class MediaController extends Controller
{
    /**
     * Upload gambar inline dari TinyMCE / WYSIWYG editor layaknya WordPress Media Uploader
     */
    public function upload(Request $request): JsonResponse
    {
        $file = $request->file('file') ?? $request->file('upload');

        if (!$file) {
            return response()->json(['error' => ['message' => 'Tidak ada file gambar yang diunggah.']], 400);
        }

        $validated = $request->validate([
            'file' => 'nullable|image|mimes:jpeg,png,jpg,gif,webp,svg|max:5120',
            'upload' => 'nullable|image|mimes:jpeg,png,jpg,gif,webp,svg|max:5120',
        ]);

        $folder = $request->input('folder', 'uploads');
        $allowedFolders = ['uploads', 'articles', 'services', 'training', 'portfolios', 'pages'];
        if (!in_array($folder, $allowedFolders)) {
            $folder = 'uploads';
        }

        $uploadDir = public_path('images/' . $folder);
        if (!file_exists($uploadDir)) {
            mkdir($uploadDir, 0755, true);
        }

        $extension = $file->getClientOriginalExtension();
        $baseName = Str::slug(pathinfo($file->getClientOriginalName(), PATHINFO_FILENAME));
        $filename = 'media-' . ($baseName ? substr($baseName, 0, 30) . '-' : '') . time() . '-' . Str::random(4) . '.' . $extension;

        $file->move($uploadDir, $filename);
        $fileUrl = asset('images/' . $folder . '/' . $filename);

        return response()->json([
            'location' => $fileUrl,
            'url' => $fileUrl,
            'filename' => $filename,
            'folder' => $folder,
            'size' => $this->formatBytes(filesize($uploadDir . '/' . $filename)),
            'date' => date('d M Y H:i'),
        ]);
    }

    /**
     * Mengambil daftar seluruh gambar untuk Pustaka Media (WordPress Media Library Modal)
     */
    public function index(Request $request): JsonResponse
    {
        $search = strtolower(trim((string) $request->input('search', '')));
        $targetFolder = $request->input('folder', 'all');

        $folders = [
            'uploads' => public_path('images/uploads'),
            'articles' => public_path('images/articles'),
            'services' => public_path('images/services'),
            'training' => public_path('images/training'),
            'portfolios' => public_path('images/portfolios'),
            'pages' => public_path('images/pages'),
        ];

        $mediaList = [];
        $allowedExtensions = ['jpg', 'jpeg', 'png', 'webp', 'svg', 'gif', 'avif'];

        foreach ($folders as $folderKey => $folderPath) {
            if ($targetFolder !== 'all' && $targetFolder !== $folderKey) {
                continue;
            }

            if (!File::exists($folderPath)) {
                continue;
            }

            $files = File::files($folderPath);
            foreach ($files as $file) {
                $ext = strtolower($file->getExtension());
                if (!in_array($ext, $allowedExtensions)) {
                    continue;
                }

                $filename = $file->getFilename();

                // Abaikan file internal seperti gitkeep
                if (str_starts_with($filename, '.')) {
                    continue;
                }

                if ($search && !str_contains(strtolower($filename), $search)) {
                    continue;
                }

                $mtime = $file->getMTime();
                $size = $file->getSize();
                $relativePath = 'images/' . $folderKey . '/' . $filename;
                $url = asset($relativePath);

                $dimensions = null;
                if ($ext !== 'svg') {
                    $imgSize = @getimagesize($file->getPathname());
                    if ($imgSize) {
                        $dimensions = $imgSize[0] . ' × ' . $imgSize[1] . ' px';
                    }
                }

                $mediaList[] = [
                    'filename' => $filename,
                    'folder' => $folderKey,
                    'url' => $url,
                    'relative_path' => $relativePath,
                    'size' => $this->formatBytes($size),
                    'timestamp' => $mtime,
                    'date' => date('d M Y, H:i', $mtime),
                    'dimensions' => $dimensions ?? '-',
                ];
            }
        }

        // Urutkan dari file paling baru
        usort($mediaList, fn($a, $b) => $b['timestamp'] <=> $a['timestamp']);

        return response()->json([
            'total' => count($mediaList),
            'media' => $mediaList,
        ]);
    }

    /**
     * Hapus gambar dari folder uploads (hanya folder uploads demi keamanan)
     */
    public function destroy(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'filename' => 'required|string',
            'folder' => 'required|string|in:uploads',
        ]);

        $safeFilename = basename($validated['filename']);
        $filePath = public_path('images/uploads/' . $safeFilename);

        if (File::exists($filePath)) {
            File::delete($filePath);
            return response()->json(['success' => true, 'message' => 'Gambar berhasil dihapus dari pustaka media.']);
        }

        return response()->json(['success' => false, 'message' => 'File tidak ditemukan.'], 404);
    }

    private function formatBytes(int $bytes, int $precision = 1): string
    {
        $units = ['B', 'KB', 'MB', 'GB'];
        $bytes = max($bytes, 0);
        $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
        $pow = min($pow, count($units) - 1);
        $bytes /= (1 << (10 * $pow));

        return round($bytes, $precision) . ' ' . $units[$pow];
    }
}
