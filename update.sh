#!/usr/bin/env bash
set -e

# ==============================================================================
# SKRIP 1-KLIK UPDATE & DEPLOYMENT - NIAGAHOSTER (PT AKTAMA DIGITAL ANTIKA)
# ==============================================================================

# Pastikan berada di folder direktori aplikasi
cd "$(dirname "$0")"

echo "=========================================================="
echo "  MEMULAI UPDATE OTOMATIS AKTAMA.COM (NIAGAHOSTER)       "
echo "=========================================================="

# 1. Deteksi otomatis binary PHP 8.3 / 8.2 Alt-PHP Niagahoster
if [ -x "/opt/alt/php83/usr/bin/php" ]; then
    PHP_BIN="/opt/alt/php83/usr/bin/php"
elif [ -x "/opt/alt/php82/usr/bin/php" ]; then
    PHP_BIN="/opt/alt/php82/usr/bin/php"
elif [ -x "/usr/local/bin/php" ]; then
    PHP_BIN="/usr/local/bin/php"
else
    PHP_BIN="php"
fi

echo "--> Menggunakan PHP: $($PHP_BIN -v | head -n 1)"

# 2. Tarik update terbaru dari Git
echo "--> [1/5] Menarik update kode & artikel dari GitHub (git pull)..."
git pull origin main

# 3. Jalankan migrasi dan seeder artikel
echo "--> [2/5] Memperbarui database dan seeder artikel terbaru..."
$PHP_BIN artisan migrate --force
$PHP_BIN artisan db:seed --force

# 4. Sinkronisasi aset gambar dan build ke public_html
echo "--> [3/5] Sinkronisasi gambar artikel & aset publik..."
WEB_ROOT="/home/u107454400/domains/aktama.com/public_html"
if [ -d "$WEB_ROOT" ]; then
    mkdir -p "$WEB_ROOT/images/articles" "$WEB_ROOT/images/services" "$WEB_ROOT/images/training" "$WEB_ROOT/images/portfolios" "$WEB_ROOT/images/uploads" "$WEB_ROOT/images/pages" "$WEB_ROOT/build"
    cp -r public/images/. "$WEB_ROOT/images/" 2>/dev/null || true
    cp -r public/build/. "$WEB_ROOT/build/" 2>/dev/null || true
    chmod -R 755 "$WEB_ROOT/images" "$WEB_ROOT/build" 2>/dev/null || true
fi

# 5. Storage symlink
echo "--> [4/5] Memastikan symlink storage terhubung..."
$PHP_BIN artisan storage:link 2>/dev/null || true

# 6. Optimasi Cache
echo "--> [5/5] Membersihkan dan mengoptimalkan cache produksi..."
$PHP_BIN artisan optimize:clear
$PHP_BIN artisan view:cache
$PHP_BIN artisan route:cache

echo ""
echo "=========================================================="
echo "  BERHASIL! Seluruh pembaruan sudah live di server.       "
echo "  Kunjungi: https://aktama.com/artikel                    "
echo "=========================================================="
