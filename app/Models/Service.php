<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Service extends Model
{
    protected $fillable = [
        'title',
        'slug',
        'category',
        'excerpt',
        'description',
        'price_starting',
        'features',
        'icon',
        'image',
        'is_featured',
        'is_published',
        'sort_order',
    ];

    protected $casts = [
        'features' => 'array',
        'is_featured' => 'boolean',
        'is_published' => 'boolean',
    ];
}
