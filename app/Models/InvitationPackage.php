<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class InvitationPackage extends Model
{
    protected $fillable = [
        'name',
        'slug',
        'image',
        'price',
        'discount_price',
        'features',
        'demo_url',
        'is_popular',
        'is_published',
        'sort_order',
    ];

    protected $casts = [
        'price' => 'decimal:2',
        'discount_price' => 'decimal:2',
        'features' => 'array',
        'is_popular' => 'boolean',
        'is_published' => 'boolean',
    ];
}
