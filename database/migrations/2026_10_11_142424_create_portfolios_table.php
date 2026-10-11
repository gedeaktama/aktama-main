<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('portfolios', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->string('slug')->unique();
            $table->string('category')->index(); // website, aplikasi, sistem-informasi, otomasi
            $table->string('client_type')->nullable(); // e.g. "Sekolah Menengah", "Instansi Kampus", "UMKM Retail"
            $table->string('technology'); // e.g. "Laravel, MySQL, Bootstrap"
            $table->string('project_year', 4)->nullable();
            $table->string('project_url')->nullable();
            $table->text('description')->nullable();
            $table->string('image')->nullable();
            $table->boolean('is_published')->default(true);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('portfolios');
    }
};
