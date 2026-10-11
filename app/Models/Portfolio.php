<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Portfolio extends Model
{
    protected $fillable = [
        'title',
        'slug',
        'category',
        'client_type',
        'technology',
        'project_year',
        'project_url',
        'description',
        'image',
        'is_published',
    ];

    protected $casts = [
        'is_published' => 'boolean',
    ];
}
