<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class CoffeeProduct extends Model
{
    protected $fillable = [
        'name',
        'slug',
        'sku',
        'description',
        'origin',
        'roast_level',
        'image',
        'is_published',
    ];

    protected $casts = [
        'is_published' => 'boolean',
    ];

    public function variants(): HasMany
    {
        return $this->hasMany(CoffeeProductVariant::class);
    }
}
