<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
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

        $uploadDir = public_path('images/uploads');
        if (!file_exists($uploadDir)) {
            mkdir($uploadDir, 0755, true);
        }

        $extension = $file->getClientOriginalExtension();
        $baseName = Str::slug(pathinfo($file->getClientOriginalName(), PATHINFO_FILENAME));
        $filename = 'media-' . ($baseName ? substr($baseName, 0, 30) . '-' : '') . time() . '-' . Str::random(4) . '.' . $extension;

        $file->move($uploadDir, $filename);
        $fileUrl = asset('images/uploads/' . $filename);

        // Kompatibel dengan format respons TinyMCE (location) dan CKEditor (url)
        return response()->json([
            'location' => $fileUrl,
            'url' => $fileUrl,
            'filename' => $filename,
        ]);
    }
}
