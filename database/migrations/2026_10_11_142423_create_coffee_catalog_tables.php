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
        Schema::create('coffee_products', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('slug')->unique();
            $table->string('sku')->nullable();
            $table->text('description')->nullable();
            $table->string('origin')->nullable();
            $table->string('roast_level')->nullable(); // Light, Medium, Dark
            $table->string('image')->nullable();
            $table->boolean('is_published')->default(true);
            $table->timestamps();
        });

        Schema::create('coffee_product_variants', function (Blueprint $table) {
            $table->id();
            $table->foreignId('coffee_product_id')->constrained('coffee_products')->onDelete('cascade');
            $table->string('variant_name'); // e.g. Biji Kopi 250g, Bubuk Halus 250g, 1kg Grosir
            $table->integer('weight_grams')->default(250);
            $table->decimal('retail_price', 12, 2)->default(0);
            $table->decimal('wholesale_price', 12, 2)->nullable();
            $table->integer('min_wholesale_qty')->default(5);
            $table->boolean('is_active')->default(true);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('coffee_product_variants');
        Schema::dropIfExists('coffee_products');
    }
};
