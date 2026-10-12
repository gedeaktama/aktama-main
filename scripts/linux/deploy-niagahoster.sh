#!/bin/bash
set -euo pipefail

# ==============================================================================
# SKRIP DEPLOYMENT OTOMATIS - PT AKTAMA DIGITAL ANTIKA (WEB UTAMA)
# Domain    : https://aktama.com
# Hosting   : Niagahoster / cPanel CloudLinux Alt-PHP 8.3
# ==============================================================================

# Auto-deteksi lokasi direktori source code di server
CURRENT_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
if [ -f "$CURRENT_SCRIPT_DIR/artisan" ]; then
    APP_ROOT="${APP_ROOT:-$CURRENT_SCRIPT_DIR}"
elif [ -d "/home/u107454400/domains/aktama.com/public_html/aktama-main-source" ]; then
    APP_ROOT="${APP_ROOT:-/home/u107454400/domains/aktama.com/public_html/aktama-main-source}"
else
    APP_ROOT="${APP_ROOT:-/home/u107454400/domains/aktama.com/public_html/aktama-main}"
fi

# Web root publik untuk domain utama: https://aktama.com
DEFAULT_WEB_ROOT="/home/u107454400/domains/aktama.com/public_html"
WEB_ROOT="${WEB_ROOT:-$DEFAULT_WEB_ROOT}"

PHP_BIN="${PHP_BIN:-/opt/alt/php83/usr/bin/php}"
RUN_SEED="${RUN_SEED:-true}"

if [ ! -d "$APP_ROOT" ]; then
  echo "ERROR: APP_ROOT tidak ditemukan: $APP_ROOT"
  exit 1
fi

if [ ! -d "$WEB_ROOT" ]; then
  echo "ERROR: WEB_ROOT tidak ditemukan: $WEB_ROOT"
  exit 1
fi

cd "$APP_ROOT"
APP_DIR_NAME="$(basename "$APP_ROOT")"

# 1. Deteksi binary PHP (Alt-PHP Niagahoster)
if [ ! -x "$PHP_BIN" ]; then
    if [ -x "/opt/alt/php82/usr/bin/php" ]; then
        PHP_BIN="/opt/alt/php82/usr/bin/php"
    elif [ -x "/usr/local/bin/php" ]; then
        PHP_BIN="/usr/local/bin/php"
    elif command -v php >/dev/null 2>&1; then
        PHP_BIN="$(command -v php)"
    fi
fi

# 2. Deteksi binary Composer
COMPOSER_BIN="composer"
if command -v composer2 >/dev/null 2>&1; then
  COMPOSER_BIN="$(command -v composer2)"
elif [ -x "/usr/local/bin/composer2" ]; then
  COMPOSER_BIN="/usr/local/bin/composer2"
elif [ -x "/usr/bin/composer2" ]; then
  COMPOSER_BIN="/usr/bin/composer2"
elif command -v composer >/dev/null 2>&1; then
  COMPOSER_BIN="$(command -v composer)"
fi

echo "=========================================================="
echo "  MEMULAI DEPLOYMENT WEB UTAMA PT AKTAMA DIGITAL ANTIKA   "
echo "  Domain      : https://aktama.com                        "
echo "  APP_ROOT    : $APP_ROOT ($APP_DIR_NAME)                 "
echo "  WEB_ROOT    : $WEB_ROOT                                 "
echo "  PHP Binary  : $($PHP_BIN -v | head -n 1)                "
echo "=========================================================="

# 3. Ambil update terbaru dari Git
echo "==> [1/7] Mengambil update terbaru dari Git (git pull)..."
if [ -d ".git" ]; then
  git pull origin main
else
  echo "    Direktori bukan git repo, melewati git pull."
fi

# 4. Pastikan file .env tersedia
if [ ! -f "$APP_ROOT/.env" ]; then
  if [ -f "$APP_ROOT/.env.production.example" ]; then
    echo "==> [Setup] Membuat file .env baru dari .env.production.example..."
    cp "$APP_ROOT/.env.production.example" "$APP_ROOT/.env"
  fi
fi

# Buat folder penyimpanan dan izin akses (writable)
mkdir -p storage/framework/cache/data storage/framework/sessions storage/framework/views storage/logs bootstrap/cache
chmod -R 775 storage bootstrap/cache 2>/dev/null || true

# 5. Install Composer Dependencies (Production Mode)
echo "==> [2/7] Memperbarui dependensi PHP (composer install)..."
if command -v "$COMPOSER_BIN" >/dev/null 2>&1 || [ -f "$COMPOSER_BIN" ]; then
  "$PHP_BIN" "$COMPOSER_BIN" install --no-dev --optimize-autoloader --no-interaction
fi

# Generate APP_KEY jika belum terisi
if [ -f "$APP_ROOT/.env" ]; then
  if ! grep -q "^APP_KEY=base64:" "$APP_ROOT/.env" 2>/dev/null; then
    echo "    Menghasilkan APP_KEY baru..."
    "$PHP_BIN" artisan key:generate --force || true
  fi
fi

# 6. Migrasi Database & Seeder
echo "==> [3/7] Menjalankan migrasi database..."
"$PHP_BIN" artisan migrate --force

if [ "$RUN_SEED" = "true" ]; then
  echo "==> [4/7] Memperbarui data awal & pengaturan (DatabaseSeeder)..."
  "$PHP_BIN" artisan db:seed --force || true
fi

# 7. Storage Symlink
echo "==> [5/7] Menghubungkan storage link..."
"$PHP_BIN" artisan storage:link || true

# 8. Optimasi Cache Produksi
echo "==> [6/7] Membersihkan & mengoptimasi cache produksi..."
"$PHP_BIN" artisan optimize:clear
"$PHP_BIN" artisan config:cache
"$PHP_BIN" artisan route:cache
"$PHP_BIN" artisan view:cache

# 9. Publikasi Asset ke Web Root (public_html)
echo "==> [7/7] Menerbitkan asset publik ke WEB_ROOT ($WEB_ROOT)..."

# Salin asset build Vite dan vendor tanpa menghapus folder subdomain lain
mkdir -p "$WEB_ROOT/build" "$WEB_ROOT/images" "$WEB_ROOT/vendor"
cp -r public/build/. "$WEB_ROOT/build/" 2>/dev/null || true
cp -r public/images/. "$WEB_ROOT/images/" 2>/dev/null || true
cp -r public/vendor/. "$WEB_ROOT/vendor/" 2>/dev/null || true
cp public/favicon.ico "$WEB_ROOT/favicon.ico" 2>/dev/null || true
cp public/robots.txt "$WEB_ROOT/robots.txt" 2>/dev/null || true

# Hubungkan symlink storage di web root
rm -f "$WEB_ROOT/storage"
ln -s "$APP_DIR_NAME/storage/app/public" "$WEB_ROOT/storage" 2>/dev/null || true

# Tulis file index.php terarah di WEB_ROOT
cat > "$WEB_ROOT/index.php" <<PHP
<?php

use Illuminate\Http\Request;

define('LARAVEL_START', microtime(true));

if (file_exists(\$maintenance = __DIR__.'/$APP_DIR_NAME/storage/framework/maintenance.php')) {
    require \$maintenance;
}

require __DIR__.'/$APP_DIR_NAME/vendor/autoload.php';

\$app = require_once __DIR__.'/$APP_DIR_NAME/bootstrap/app.php';

\$app->handleRequest(Request::capture());
PHP

# Buat .htaccess yang aman di WEB_ROOT (tidak mengganggu subdomain & folder lain)
cat > "$WEB_ROOT/.htaccess" << 'HTACCESS'
<IfModule mod_rewrite.c>
    <IfModule mod_negotiation.c>
        Options -MultiViews -Indexes
    </IfModule>

    RewriteEngine On

    # Handle Authorization Header
    RewriteCond %{HTTP:Authorization} .
    RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

    # Redirect Trailing Slashes If Not A Folder...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_URI} (.+)/$
    RewriteRule ^ %1 [L,R=301]

    # Send Requests To Front Controller (Kecuali folder atau file fisik yang ada)
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^ index.php [L]
</IfModule>
HTACCESS

chmod 644 "$WEB_ROOT/index.php" "$WEB_ROOT/.htaccess"
chmod -R 775 storage bootstrap/cache 2>/dev/null || true

echo "=========================================================="
echo "  DEPLOYMENT WEB UTAMA AKTAMA DIGITAL BERHASIL!           "
echo "  Website siap diakses di:                                "
echo "  👉 https://aktama.com                                   "
echo "  👉 Panel Admin : https://aktama.com/admin/login         "
echo "=========================================================="
