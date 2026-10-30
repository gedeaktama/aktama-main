<?php

namespace App\Mail;

use App\Models\Lead;
use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class NewInquiryAdminMail extends Mailable
{
    use Queueable, SerializesModels;

    public function __construct(
        public Lead $lead
    ) {}

    public function envelope(): Envelope
    {
        $clientName = $this->lead->name ?: 'Calon Klien';
        $service = $this->lead->service_label ?: 'Konsultasi';

        return new Envelope(
            subject: "🔔 [Aktama.com] Konsultasi Baru: {$clientName} - {$service}",
        );
    }

    public function content(): Content
    {
        return new Content(
            view: 'emails.new-inquiry-admin',
        );
    }
}

