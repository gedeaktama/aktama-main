<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class HomeSection extends Model
{
    protected $fillable = [
        'section_key',
        'name',
        'badge',
        'title',
        'subtitle',
        'content_data',
        'sort_order',
        'is_active',
    ];

    protected $casts = [
        'content_data' => 'array',
        'sort_order' => 'integer',
        'is_active' => 'boolean',
    ];
}
