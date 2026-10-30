<?php

namespace Tests\Feature;

use App\Mail\NewInquiryAdminMail;
use App\Models\Lead;
use App\Services\InquiryNotificationService;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Config;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Mail;
use Tests\TestCase;

class InquiryNotificationTest extends TestCase
{
    use RefreshDatabase;

    public function test_dispatches_telegram_and_email_when_inquiry_stored(): void
    {
        Mail::fake();
        Http::fake([
            'https://api.telegram.org/*' => Http::response(['ok' => true], 200),
        ]);

        Config::set('services.telegram.bot_token', 'test-token');
        Config::set('services.telegram.chat_id', '8993785499');
        Config::set('mail.admin_address', 'owner@aktama.com');

        $lead = Lead::create([
            'name' => 'Pak Wayan',
            'whatsapp' => '08123456789',
            'email' => 'wayan@example.com',
            'organization' => 'CV Bali Sukses',
            'service_type' => 'jasa-website',
            'budget_range' => 'Rp 5jt - 10jt',
            'message' => 'Butuh website untuk rental mobil dan tour.',
            'source_page' => 'Jasa Website',
            'status' => 'new',
        ]);

        $results = InquiryNotificationService::notifyAdminNewInquiry($lead);

        $this->assertTrue($results['telegram']['sent']);
        $this->assertTrue($results['email']['sent']);

        Mail::assertSent(NewInquiryAdminMail::class, function (NewInquiryAdminMail $mail) use ($lead) {
            return $mail->hasTo('owner@aktama.com')
                && $mail->lead->id === $lead->id;
        });

        Http::assertSent(function ($request) use ($lead) {
            return str_contains($request->url(), 'api.telegram.org')
                && str_contains($request['text'], 'KONSULTASI BARU (AKTAMA.COM)')
                && str_contains($request['text'], $lead->name);
        });
    }

    public function test_failsafe_does_not_throw_when_notification_fails(): void
    {
        Mail::shouldReceive('to->send')->andThrow(new \Exception('SMTP timeout'));
        Http::fake([
            'https://api.telegram.org/*' => Http::response(['description' => 'Unauthorized'], 401),
        ]);

        Config::set('services.telegram.bot_token', 'bad-token');
        Config::set('services.telegram.chat_id', '999');

        $lead = Lead::create([
            'name' => 'Failsafe Test',
            'whatsapp' => '0877777777',
            'service_type' => 'konsultasi',
            'message' => 'Test message',
            'status' => 'new',
        ]);

        $results = InquiryNotificationService::notifyAdminNewInquiry($lead);

        $this->assertFalse($results['telegram']['sent']);
        $this->assertFalse($results['email']['sent']);
    }

    public function test_email_view_renders_cleanly(): void
    {
        $lead = Lead::create([
            'name' => 'Made Artawan',
            'whatsapp' => '085341026331',
            'email' => 'made@example.com',
            'organization' => 'PT Bali Mandiri',
            'service_type' => 'pelatihan-ai',
            'budget_range' => 'Rp 10.000.000+',
            'message' => 'Ingin pelatihan in-house untuk staf kami sebanyak 15 orang.',
            'status' => 'new',
        ]);

        $mailable = new NewInquiryAdminMail($lead);
        $rendered = $mailable->render();

        $this->assertStringContainsString('Made Artawan', $rendered);
        $this->assertStringContainsString('085341026331', $rendered);
        $this->assertStringContainsString('Pelatihan AI &amp; Komputer', $rendered);
        $this->assertStringContainsString('Hubungi Klien di WhatsApp', $rendered);
    }
}

