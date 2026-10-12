<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     * Clean up mock/ghost tables (coffee retail & standalone invitation packages)
     * from main corporate portal, as they now have dedicated live subdomains.
     */
    public function up(): void
    {
        Schema::dropIfExists('coffee_product_variants');
        Schema::dropIfExists('coffee_products');
        Schema::dropIfExists('invitation_packages');
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        // Reversal not required as these tables belong to separate subdomains
    }
};
