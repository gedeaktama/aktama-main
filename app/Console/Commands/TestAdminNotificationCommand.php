<?php

namespace App\Console\Commands;

use App\Models\Lead;
use App\Services\InquiryNotificationService;
use Illuminate\Console\Command;

class TestAdminNotificationCommand extends Command
{
    protected $signature = 'notification:test {--email= : Target email admin untuk pengujian} {--chat-id= : Target Telegram chat id untuk pengujian} {--sample : Kirim simulasi format inquiry lengkap}';
    protected $description = 'Uji coba pengiriman notifikasi inquiry ke Telegram dan Email Admin';

    public function handle(): int
    {
        $this->info('🚀 Memulai pengujian notifikasi Aktama.com...');

        $email = $this->option('email');
        $chatId = $this->option('chat-id');

        $results = InquiryNotificationService::sendTestNotifications($email, $chatId);

        $this->line('');
        $this->info('--- Status Pengujian Telegram ---');
        if ($results['telegram']['sent']) {
            $this->info('✅ ' . $results['telegram']['message']);
        } else {
            $this->warn('⚠️ ' . $results['telegram']['message']);
        }

        $this->line('');
        $this->info('--- Status Pengujian Email ---');
        if ($results['email']['sent']) {
            $this->info('✅ ' . $results['email']['message']);
        } else {
            $this->warn('⚠️ ' . $results['email']['message']);
        }

        if ($this->option('sample')) {
            $this->line('');
            $this->info('--- Mengirim Simulasi Email Inquiry HTML Lengkap ---');

            $lead = Lead::first() ?? new Lead([
                'name' => 'Budi Santoso',
                'whatsapp' => '081234567890',
                'email' => 'budi@ptmaju.co.id',
                'organization' => 'PT Maju Bersama',
                'service_type' => 'jasa-website',
                'budget_range' => 'Rp 5.000.000 - Rp 10.000.000',
                'message' => 'Kami memerlukan website profil perusahaan lengkap dengan integrasi WhatsApp dan CMS artikel.',
                'source_page' => 'Jasa Pembuatan Website',
            ]);

            $res = InquiryNotificationService::sendEmailNotification($lead);
            if ($res['sent']) {
                $this->info('✅ ' . $res['message']);
            } else {
                $this->warn('⚠️ ' . $res['message']);
            }
        }

        $this->line('');
        return Command::SUCCESS;
    }
}

