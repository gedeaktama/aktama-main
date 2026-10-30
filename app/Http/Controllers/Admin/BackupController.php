<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\File;
use Illuminate\View\View;
use Symfony\Component\HttpFoundation\StreamedResponse;
use ZipArchive;

class BackupController extends Controller
{
    /**
     * Tampilan Pusat Pencadangan Data (1-Click Backup ala UpdraftPlus)
     */
    public function index(): View
    {
        $dbName = config('database.connections.mysql.database');
        
        // Hitung estimasi ukuran database
        $dbSize = '0 MB';
        try {
            $sizeQuery = DB::select("
                SELECT table_schema AS `database`, 
                ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS `size_mb` 
                FROM information_schema.tables 
                WHERE table_schema = ? 
                GROUP BY table_schema
            ", [$dbName]);

            if (!empty($sizeQuery)) {
                $dbSize = $sizeQuery[0]->size_mb . ' MB';
            }
        } catch (\Throwable $e) {
            $dbSize = 'Tersedia';
        }

        // Hitung total berkas dan ukuran media
        $mediaPath = public_path('images');
        $mediaCount = 0;
        $mediaSizeMb = 0;

        if (File::exists($mediaPath)) {
            $files = File::allFiles($mediaPath);
            $mediaCount = count($files);
            $totalBytes = 0;
            foreach ($files as $file) {
                $totalBytes += $file->getSize();
            }
            $mediaSizeMb = round($totalBytes / 1024 / 1024, 2) . ' MB';
        }

        return view('admin.backup.index', compact('dbName', 'dbSize', 'mediaCount', 'mediaSizeMb'));
    }

    /**
     * 1-Click Download Cadangan Database (.sql) Native PDO
     */
    public function downloadDatabase(): StreamedResponse
    {
        $dbName = config('database.connections.mysql.database');
        $filename = 'aktama_db_backup_' . date('Y-m-d_His') . '.sql';

        return response()->streamDownload(function () use ($dbName) {
            $pdo = DB::connection()->getPdo();

            echo "-- ==========================================================\n";
            echo "-- PT AKTAMA DIGITAL ANTIKA - DATABASE BACKUP\n";
            echo "-- Tanggal Backup : " . date('Y-m-d H:i:s') . "\n";
            echo "-- Database       : " . $dbName . "\n";
            echo "-- Arsitektur     : Laravel 12 Native PDO SQL Dump\n";
            echo "-- ==========================================================\n\n";
            echo "SET FOREIGN_KEY_CHECKS=0;\n";
            echo "SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';\n";
            echo "SET NAMES utf8mb4;\n\n";

            $tables = [];
            $tableRows = $pdo->query("SHOW TABLES")->fetchAll(\PDO::FETCH_NUM);
            foreach ($tableRows as $row) {
                $tables[] = $row[0];
            }

            foreach ($tables as $table) {
                // Skema Create Table
                echo "-- --------------------------------------------------------\n";
                echo "-- Struktur Tabel `{$table}`\n";
                echo "-- --------------------------------------------------------\n";
                echo "DROP TABLE IF EXISTS `{$table}`;\n";

                $createRow = $pdo->query("SHOW CREATE TABLE `{$table}`")->fetch(\PDO::FETCH_ASSOC);
                echo $createRow['Create Table'] . ";\n\n";

                // Data Baris Tabel
                $dataStmt = $pdo->query("SELECT * FROM `{$table}`");
                $dataRows = $dataStmt->fetchAll(\PDO::FETCH_ASSOC);

                if (!empty($dataRows)) {
                    echo "-- Dumping Data untuk Tabel `{$table}`\n";
                    $columns = array_keys($dataRows[0]);
                    $colList = implode('`, `', $columns);

                    foreach (array_chunk($dataRows, 100) as $chunk) {
                        $valuesList = [];
                        foreach ($chunk as $row) {
                            $rowValues = [];
                            foreach ($row as $val) {
                                if (is_null($val)) {
                                    $rowValues[] = 'NULL';
                                } else {
                                    $rowValues[] = $pdo->quote($val);
                                }
                            }
                            $valuesList[] = '(' . implode(', ', $rowValues) . ')';
                        }
                        echo "INSERT INTO `{$table}` (`{$colList}`) VALUES\n" . implode(",\n", $valuesList) . ";\n";
                    }
                    echo "\n";
                }
            }

            echo "SET FOREIGN_KEY_CHECKS=1;\n";
            echo "-- BACKUP SELESAI --\n";
        }, $filename, [
            'Content-Type' => 'application/sql',
            'Content-Disposition' => 'attachment; filename="' . $filename . '"',
        ]);
    }

    /**
     * 1-Click Download Arsip Seluruh Berkas Media (.zip)
     */
    public function downloadMedia(): mixed
    {
        $zipFilename = 'aktama_media_' . date('Y-m-d_His') . '.zip';
        $tempPath = storage_path('framework/cache/' . $zipFilename);

        $zip = new ZipArchive();
        if ($zip->open($tempPath, ZipArchive::CREATE | ZipArchive::OVERWRITE) !== true) {
            return back()->with('error', 'Gagal membuat file arsip ZIP.');
        }

        $mediaDir = public_path('images');
        if (File::exists($mediaDir)) {
            $files = File::allFiles($mediaDir);
            foreach ($files as $file) {
                $relativePath = 'images/' . $file->getRelativePathname();
                $zip->addFile($file->getRealPath(), $relativePath);
            }
        }

        $zip->close();

        return response()->download($tempPath, $zipFilename)->deleteFileAfterSend(true);
    }
}

