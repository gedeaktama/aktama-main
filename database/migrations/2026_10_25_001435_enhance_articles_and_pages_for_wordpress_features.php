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
        Schema::table('articles', function (Blueprint $table) {
            if (!Schema::hasColumn('articles', 'tags')) {
                $table->string('tags')->nullable()->after('author');
            }
            if (!Schema::hasColumn('articles', 'views_count')) {
                $table->unsignedBigInteger('views_count')->default(0)->after('status');
            }
        });

        Schema::table('pages', function (Blueprint $table) {
            if (!Schema::hasColumn('pages', 'template')) {
                $table->string('template')->default('default')->after('editor_type');
            }
            if (!Schema::hasColumn('pages', 'featured_image')) {
                $table->string('featured_image')->nullable()->after('template');
            }
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('articles', function (Blueprint $table) {
            if (Schema::hasColumn('articles', 'tags')) {
                $table->dropColumn('tags');
            }
            if (Schema::hasColumn('articles', 'views_count')) {
                $table->dropColumn('views_count');
            }
        });

        Schema::table('pages', function (Blueprint $table) {
            if (Schema::hasColumn('pages', 'template')) {
                $table->dropColumn('template');
            }
            if (Schema::hasColumn('pages', 'featured_image')) {
                $table->dropColumn('featured_image');
            }
        });
    }
};
