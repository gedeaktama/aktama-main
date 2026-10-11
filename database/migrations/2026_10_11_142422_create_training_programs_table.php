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
        Schema::create('training_programs', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->string('slug')->unique();
            $table->string('category')->index(); // ai-kantor, ai-produktivitas, ai-pendidikan, ai-bisnis, coding
            $table->string('target_audience');
            $table->text('objectives')->nullable();
            $table->json('syllabus')->nullable();
            $table->string('delivery_format')->default('hybrid'); // online, offline, hybrid
            $table->string('duration')->nullable(); // e.g. "2 Hari (16 Jam)"
            $table->string('price_info')->nullable();
            $table->boolean('is_featured')->default(false);
            $table->boolean('is_published')->default(true);
            $table->integer('sort_order')->default(0);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('training_programs');
    }
};
