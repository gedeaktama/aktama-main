<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class TrainingProgram extends Model
{
    protected $fillable = [
        'title',
        'slug',
        'category',
        'target_audience',
        'objectives',
        'syllabus',
        'delivery_format',
        'duration',
        'price_info',
        'image',
        'is_featured',
        'is_published',
        'sort_order',
    ];

    protected $casts = [
        'syllabus' => 'array',
        'is_featured' => 'boolean',
        'is_published' => 'boolean',
    ];
}
