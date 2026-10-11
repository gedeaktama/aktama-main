<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class CoffeeProductVariant extends Model
{
    protected $fillable = [
        'coffee_product_id',
        'variant_name',
        'weight_grams',
        'retail_price',
        'wholesale_price',
        'min_wholesale_qty',
        'is_active',
    ];

    protected $casts = [
        'retail_price' => 'decimal:2',
        'wholesale_price' => 'decimal:2',
        'is_active' => 'boolean',
    ];

    public function product(): BelongsTo
    {
        return $this->belongsTo(CoffeeProduct::class, 'coffee_product_id');
    }
}
