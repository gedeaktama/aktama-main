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
        Schema::table('services', function (Blueprint $table) {
            if (!Schema::hasColumn('services', 'image')) {
                $table->string('image')->nullable()->after('icon');
            }
        });

        Schema::table('training_programs', function (Blueprint $table) {
            if (!Schema::hasColumn('training_programs', 'image')) {
                $table->string('image')->nullable()->after('price_info');
            }
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('services', function (Blueprint $table) {
            if (Schema::hasColumn('services', 'image')) {
                $table->dropColumn('image');
            }
        });

        Schema::table('training_programs', function (Blueprint $table) {
            if (Schema::hasColumn('training_programs', 'image')) {
                $table->dropColumn('image');
            }
        });
    }
};
