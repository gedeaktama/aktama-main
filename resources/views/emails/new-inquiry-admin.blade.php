@php
    $digits = preg_replace('/\D+/', '', (string) ($lead->whatsapp ?? ''));
    if (str_starts_with($digits, '0')) {
        $waPhone = '62' . substr($digits, 1);
    } elseif (str_starts_with($digits, '62')) {
        $waPhone = $digits;
    } else {
        $waPhone = $digits;
    }

    $leadName = $lead->name ?? 'Calon Klien';
    $waText = urlencode("Halo {$leadName}, terima kasih telah menghubungi Aktama Digital melalui formulir konsultasi website kami...");
    $waUrl = filled($waPhone) ? "https://wa.me/{$waPhone}?text={$waText}" : null;
    $adminUrl = url('/admin/leads/' . $lead->id);
@endphp
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Konsultasi Baru Masuk - Aktama Digital</title>
</head>
<body style="margin: 0; padding: 0; background-color: #0b1120; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #334155;">
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background-color: #0b1120; padding: 32px 16px;">
        <tr>
            <td align="center">
                <table role="presentation" width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 32px 28px; text-align: center; border-bottom: 3px solid #38bdf8;">
                            <div style="display: inline-block; padding: 6px 14px; background-color: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 9999px; font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 12px;">
                                WEBSITE UTAMA AKTAMA.COM
                            </div>
                            <h1 style="margin: 0; color: #ffffff; font-size: 24px; font-weight: 800; letter-spacing: -0.02em;">
                                🚀 Konsultasi / Inquiry Baru!
                            </h1>
                            <p style="margin: 8px 0 0; color: #94a3b8; font-size: 14px;">
                                Ada calon klien baru yang mengajukan konsultasi layanan melalui website utama.
                            </p>
                        </td>
                    </tr>

                    <!-- Highlight Box -->
                    <tr>
                        <td style="padding: 24px 28px 0;">
                            <table role="presentation" width="100%" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
                                <tr>
                                    <td>
                                        <div style="font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Layanan Diminati</div>
                                        <div style="font-size: 18px; font-weight: 800; color: #0284c7; margin-top: 2px;">{{ $lead->service_label }}</div>
                                    </td>
                                    <td align="right">
                                        <div style="font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">Estimasi Budget</div>
                                        <div style="font-size: 16px; font-weight: 700; color: #059669; margin-top: 2px;">
                                            {{ $lead->budget_range ?: 'Fleksibel / Diskusi' }}
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Details Table -->
                    <tr>
                        <td style="padding: 20px 28px;">
                            <h2 style="margin: 0 0 14px; font-size: 14px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.05em;">
                                Data Calon Klien
                            </h2>
                            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="font-size: 14px; border-collapse: collapse;">
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b; width: 38%;">Nama Lengkap</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; font-weight: 600; color: #0f172a;">{{ $leadName }}</td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b;">WhatsApp</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; font-weight: 600; color: #0f172a;">
                                        {{ $lead->whatsapp }}
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b;">Email</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #0f172a;">
                                        {{ $lead->email ?: '-' }}
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b;">Perusahaan / Instansi</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #0f172a;">
                                        {{ $lead->organization ?: '-' }}
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b;">Halaman Asal</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b;">
                                        {{ $lead->source_page ?: 'Website Utama' }}
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b; vertical-align: top;">Pesan / Kebutuhan</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #334155; font-style: italic;">
                                        "{{ $lead->message }}"
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Action Buttons -->
                    <tr>
                        <td style="padding: 10px 28px 28px; text-align: center;">
                            @if($waUrl)
                            <a href="{{ $waUrl }}" target="_blank" style="display: inline-block; background-color: #22c55e; color: #ffffff; text-decoration: none; font-size: 14px; font-weight: 700; padding: 12px 24px; border-radius: 8px; margin: 6px; box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3);">
                                💬 Hubungi Klien di WhatsApp
                            </a>
                            @endif
                            <a href="{{ $adminUrl }}" target="_blank" style="display: inline-block; background-color: #0f172a; color: #ffffff; text-decoration: none; font-size: 14px; font-weight: 700; padding: 12px 24px; border-radius: 8px; margin: 6px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);">
                                📊 Buka di Admin Aktama
                            </a>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f8fafc; border-top: 1px solid #e2e8f0; padding: 20px 28px; text-align: center; color: #94a3b8; font-size: 12px;">
                            Email otomatis dari portal resmi <strong>Aktama Digital (aktama.com)</strong>.<br>
                            Anda dapat langsung merespons klien melalui tombol WhatsApp di atas.
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>

