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
        Schema::create('leads', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('whatsapp', 30);
            $table->string('email')->nullable();
            $table->string('organization')->nullable();
            $table->string('service_type')->index(); // pelatihan-ai, jasa-website, aktama-academy, aktama-coffee, undangan-online, konsultasi
            $table->string('budget_range')->nullable();
            $table->text('message');
            $table->string('source_page')->nullable();
            $table->string('status')->default('new')->index(); // new, contacted, qualified, closed, cancelled
            $table->text('admin_notes')->nullable();
            $table->string('ip_address', 45)->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('leads');
    }
};
