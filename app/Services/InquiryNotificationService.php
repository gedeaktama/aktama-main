<?php

namespace App\Services;

use App\Mail\NewInquiryAdminMail;
use App\Models\Lead;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Mail;
use Throwable;

class InquiryNotificationService
{
    /**
     * Dispatch both Email and Telegram notifications for new inquiry/lead.
     * Always returns an array status and never throws exceptions.
     *
     * @return array{email: array{sent: bool, message: string}, telegram: array{sent: bool, message: string}}
     */
    public static function notifyAdminNewInquiry(Lead $lead): array
    {
        $results = [
            'email' => ['sent' => false, 'message' => 'Not executed'],
            'telegram' => ['sent' => false, 'message' => 'Not executed'],
        ];

        // 1. Telegram Notification
        try {
            $results['telegram'] = self::sendTelegramNotification($lead);
        } catch (Throwable $e) {
            Log::error('InquiryNotificationService [Telegram Exception]: ' . $e->getMessage(), [
                'lead_id' => $lead->id,
            ]);
            $results['telegram'] = ['sent' => false, 'message' => $e->getMessage()];
        }

        // 2. Email Notification
        try {
            $results['email'] = self::sendEmailNotification($lead);
        } catch (Throwable $e) {
            Log::error('InquiryNotificationService [Email Exception]: ' . $e->getMessage(), [
                'lead_id' => $lead->id,
            ]);
            $results['email'] = ['sent' => false, 'message' => $e->getMessage()];
        }

        return $results;
    }

    /**
     * Send inquiry alert to Telegram admin chat.
     *
     * @return array{sent: bool, message: string}
     */
    public static function sendTelegramNotification(Lead $lead): array
    {
        $botToken = config('services.telegram.bot_token') ?: env('TELEGRAM_BOT_TOKEN');
        $chatId = config('services.telegram.chat_id') ?: env('TELEGRAM_CHAT_ID');

        if (blank($botToken) || blank($chatId)) {
            Log::debug('Telegram inquiry notification skipped: credentials missing');
            return ['sent' => false, 'message' => 'TELEGRAM_BOT_TOKEN atau TELEGRAM_CHAT_ID belum diisi di .env'];
        }

        $name = htmlspecialchars((string) ($lead->name ?: 'Calon Klien'), ENT_QUOTES, 'UTF-8');
        $whatsapp = htmlspecialchars((string) ($lead->whatsapp ?: '-'), ENT_QUOTES, 'UTF-8');
        $email = htmlspecialchars((string) ($lead->email ?: '-'), ENT_QUOTES, 'UTF-8');
        $organization = htmlspecialchars((string) ($lead->organization ?: '-'), ENT_QUOTES, 'UTF-8');
        $service = htmlspecialchars((string) ($lead->service_label ?: 'Konsultasi'), ENT_QUOTES, 'UTF-8');
        $budget = htmlspecialchars((string) ($lead->budget_range ?: 'Fleksibel'), ENT_QUOTES, 'UTF-8');
        $sourcePage = htmlspecialchars((string) ($lead->source_page ?: 'Website Utama'), ENT_QUOTES, 'UTF-8');

        // Format clean phone for WhatsApp direct click
        $cleanDigits = preg_replace('/\D+/', '', (string) ($lead->whatsapp ?? ''));
        if (str_starts_with($cleanDigits, '0')) {
            $waPhone = '62' . substr($cleanDigits, 1);
        } elseif (str_starts_with($cleanDigits, '62')) {
            $waPhone = $cleanDigits;
        } else {
            $waPhone = $cleanDigits;
        }

        $waUrl = filled($waPhone)
            ? 'https://wa.me/' . $waPhone . '?text=' . urlencode("Halo {$lead->name}, terima kasih telah menghubungi Aktama Digital melalui formulir konsultasi website kami...")
            : null;

        $adminUrl = url('/admin/leads/' . $lead->id);

        $lines = [
            "🔔 <b>KONSULTASI BARU (AKTAMA.COM)</b>",
            "",
            "<b>Nama:</b> {$name}",
            "<b>WhatsApp:</b> {$whatsapp}",
            "<b>Email:</b> {$email}",
            "<b>Instansi:</b> {$organization}",
            "<b>Layanan:</b> <b>{$service}</b>",
            "<b>Budget:</b> {$budget}",
            "<b>Sumber:</b> {$sourcePage}",
        ];

        if (!empty($lead->message)) {
            $message = htmlspecialchars((string) $lead->message, ENT_QUOTES, 'UTF-8');
            $lines[] = "";
            $lines[] = "💬 <i>\"{$message}\"</i>";
        }

        $lines[] = "";
        if ($waUrl) {
            $lines[] = "👉 <a href=\"{$waUrl}\">Chat Calon Klien di WhatsApp</a>";
        }
        $lines[] = "📊 <a href=\"{$adminUrl}\">Buka di Admin Aktama</a>";

        $text = implode("\n", $lines);

        $baseUrl = self::getTelegramApiUrl();
        $response = self::createTelegramHttpClient()->post("{$baseUrl}/bot{$botToken}/sendMessage", [
            'chat_id' => $chatId,
            'text' => $text,
            'parse_mode' => 'HTML',
            'disable_web_page_preview' => true,
        ]);

        if ($response->successful()) {
            return ['sent' => true, 'message' => 'Notifikasi Telegram berhasil terkirim.'];
        }

        $errorMsg = $response->json('description') ?: ('HTTP ' . $response->status());
        Log::warning('Telegram send failed: ' . $errorMsg);
        return ['sent' => false, 'message' => 'Telegram API gagal: ' . $errorMsg];
    }

    /**
     * Send inquiry notification email to administrator.
     *
     * @return array{sent: bool, message: string}
     */
    public static function sendEmailNotification(Lead $lead): array
    {
        $adminEmail = config('mail.admin_address')
            ?: config('services.admin_email')
            ?: env('ADMIN_NOTIFICATION_EMAIL')
            ?: config('mail.from.address');

        if (blank($adminEmail)) {
            Log::debug('Admin inquiry email skipped: ADMIN_NOTIFICATION_EMAIL not set');
            return ['sent' => false, 'message' => 'ADMIN_NOTIFICATION_EMAIL belum diisi'];
        }

        Mail::to($adminEmail)->send(new NewInquiryAdminMail($lead));

        return ['sent' => true, 'message' => "Email notifikasi berhasil dikirim ke {$adminEmail}"];
    }

    /**
     * Send a test notification to verify credentials.
     *
     * @return array{email: array{sent: bool, message: string}, telegram: array{sent: bool, message: string}}
     */
    public static function sendTestNotifications(
        ?string $targetEmail = null,
        ?string $telegramChatId = null,
        ?string $telegramBotToken = null,
    ): array {
        $results = [
            'telegram' => ['sent' => false, 'message' => 'Skipped'],
            'email' => ['sent' => false, 'message' => 'Skipped'],
        ];

        // Telegram Test
        $botToken = $telegramBotToken ?: (config('services.telegram.bot_token') ?: env('TELEGRAM_BOT_TOKEN'));
        $chatId = $telegramChatId ?: (config('services.telegram.chat_id') ?: env('TELEGRAM_CHAT_ID'));

        if (filled($botToken) && filled($chatId)) {
            try {
                $baseUrl = self::getTelegramApiUrl();
                $response = self::createTelegramHttpClient()->post("{$baseUrl}/bot{$botToken}/sendMessage", [
                    'chat_id' => $chatId,
                    'text' => "🎉 <b>UJI COBA NOTIFIKASI AKTAMA.COM BERHASIL!</b>\n\nSistem konsultasi dan inquiry dari website utama Aktama Digital telah terhubung dengan akun Telegram ini.",
                    'parse_mode' => 'HTML',
                ]);

                if ($response->successful()) {
                    $results['telegram'] = ['sent' => true, 'message' => 'Pesan uji coba Telegram berhasil masuk ke chat ID ' . $chatId];
                } else {
                    $results['telegram'] = ['sent' => false, 'message' => 'Telegram API gagal: ' . ($response->json('description') ?: $response->body())];
                }
            } catch (Throwable $e) {
                $results['telegram'] = ['sent' => false, 'message' => 'Error koneksi Telegram: ' . $e->getMessage()];
            }
        } else {
            $results['telegram'] = ['sent' => false, 'message' => 'TELEGRAM_BOT_TOKEN atau TELEGRAM_CHAT_ID belum diatur'];
        }

        // Email Test
        $email = $targetEmail
            ?: (config('mail.admin_address') ?: env('ADMIN_NOTIFICATION_EMAIL') ?: config('mail.from.address'));

        if (filled($email)) {
            try {
                Mail::raw("Halo Admin,\n\nIni adalah email uji coba dari website utama Aktama Digital (aktama.com). Notifikasi email untuk konsultasi/inquiry baru berfungsi dengan baik!", function ($message) use ($email) {
                    $message->to($email)->subject('✅ Uji Coba Notifikasi Email Aktama.com');
                });
                $results['email'] = ['sent' => true, 'message' => 'Email uji coba berhasil dikirim ke ' . $email];
            } catch (Throwable $e) {
                $results['email'] = ['sent' => false, 'message' => 'Gagal mengirim email: ' . $e->getMessage()];
            }
        } else {
            $results['email'] = ['sent' => false, 'message' => 'ADMIN_NOTIFICATION_EMAIL belum diatur'];
        }

        return $results;
    }

    /**
     * Create configured HTTP client for Telegram API with IPv4 enforcement and resilient timeouts.
     */
    protected static function createTelegramHttpClient(): \Illuminate\Http\Client\PendingRequest
    {
        $curlOptions = [];
        if (defined('CURLOPT_IPRESOLVE') && defined('CURL_IPRESOLVE_V4')) {
            $curlOptions[CURLOPT_IPRESOLVE] = CURL_IPRESOLVE_V4;
        }

        return Http::withOptions([
            'connect_timeout' => 10,
            'timeout' => 15,
            'curl' => $curlOptions,
        ])->asJson();
    }

    /**
     * Resolve Telegram API base URL (supports proxy/mirror when configured).
     */
    protected static function getTelegramApiUrl(): string
    {
        $url = config('services.telegram.base_url') ?: env('TELEGRAM_API_URL', 'https://api.telegram.org');
        return rtrim($url, '/');
    }
}

