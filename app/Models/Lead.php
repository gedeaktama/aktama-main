<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Lead extends Model
{
    protected $fillable = [
        'name',
        'whatsapp',
        'email',
        'organization',
        'service_type',
        'budget_range',
        'message',
        'source_page',
        'status',
        'admin_notes',
        'ip_address',
    ];

    public function getServiceLabelAttribute(): string
    {
        $labels = [
            'pelatihan-ai' => 'Pelatihan AI & Komputer',
            'jasa-website' => 'Jasa Pembuatan Website & Aplikasi',
            'aktama-academy' => 'Pendaftaran Kursus Aktama Academy',
            'aktama-coffee' => 'Kemitraan / Pasokan Kopi',
            'undangan-online' => 'Pemesanan Undangan Digital',
            'konsultasi' => 'Konsultasi Teknologi Umum',
        ];

        return $labels[$this->service_type] ?? ucwords(str_replace('-', ' ', $this->service_type));
    }

    public function getStatusBadgeAttribute(): string
    {
        return match ($this->status) {
            'new' => 'badge-soft-danger',
            'contacted' => 'badge-soft-warning',
            'qualified' => 'badge-soft-info',
            'closed' => 'badge-soft-success',
            default => 'badge-soft-secondary',
        };
    }
}
