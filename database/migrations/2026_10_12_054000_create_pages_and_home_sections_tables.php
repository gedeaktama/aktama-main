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
        // 1. Tabel Halaman Custom & Visual Page Builder (GrapesJS / Standard)
        Schema::create('pages', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->string('slug')->unique();
            $table->string('editor_type')->default('builder'); // 'builder' (GrapesJS) or 'standard' (WYSIWYG/HTML)
            $table->longText('content_html')->nullable();
            $table->longText('content_css')->nullable();
            $table->longText('content_json')->nullable();
            $table->string('meta_title')->nullable();
            $table->text('meta_description')->nullable();
            $table->boolean('is_published')->default(true);
            $table->integer('sort_order')->default(0);
            $table->timestamps();
        });

        // 2. Tabel Seksi Beranda (Opsi A: Modular Section Drag & Drop Builder)
        Schema::create('home_sections', function (Blueprint $table) {
            $table->id();
            $table->string('section_key')->unique();
            $table->string('name');
            $table->string('badge')->nullable();
            $table->string('title')->nullable();
            $table->text('subtitle')->nullable();
            $table->json('content_data')->nullable();
            $table->integer('sort_order')->default(0);
            $table->boolean('is_active')->default(true);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('home_sections');
        Schema::dropIfExists('pages');
    }
};
