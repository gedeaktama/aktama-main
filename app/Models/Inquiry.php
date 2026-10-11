<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Inquiry extends Model
{
    protected $fillable = [
        'name',
        'whatsapp',
        'email',
        'business_unit',
        'budget_range',
        'message',
        'status',
        'ip_address',
    ];
}
