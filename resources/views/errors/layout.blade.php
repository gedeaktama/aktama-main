<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title') | PT Aktama Digital Antika</title>
    <link rel="icon" type="image/png" href="{{ asset('images/logo-aktama.png') }}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #0b1120;
            color: #f8fafc;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 1.5rem;
        }
        .error-card {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(16px);
            border-radius: 1.5rem;
            max-width: 580px;
            width: 100%;
            padding: 3rem 2rem;
            text-align: center;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }
        .status-badge {
            font-size: 4.5rem;
            font-weight: 800;
            line-height: 1;
            letter-spacing: -2px;
            background: linear-gradient(135deg, #38bdf8 0%, #6366f1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        .btn-brand {
            background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
            color: #ffffff;
            border: none;
            font-weight: 600;
            transition: all 0.2s ease;
        }
        .btn-brand:hover {
            opacity: 0.92;
            transform: translateY(-2px);
            color: #ffffff;
        }
    </style>
</head>
<body>
    <div class="error-card">
        <a href="{{ url('/') }}" class="d-inline-block mb-4">
            <img src="{{ asset('images/logo-aktama.png') }}" alt="PT Aktama Digital Antika" style="height: 48px; width: auto;" class="bg-white p-2 rounded-3 shadow-sm">
        </a>

        <div class="status-badge">@yield('code')</div>
        <h2 class="fw-bold mb-3">@yield('heading')</h2>
        <p class="text-white-50 mb-4 fs-6 leading-relaxed">@yield('message')</p>

        <div class="d-flex flex-wrap justify-content-center gap-3">
            <a href="{{ url('/') }}" class="btn btn-brand rounded-pill px-4 py-2">
                <i class="bi bi-house-door-fill me-1"></i> Kembali ke Beranda
            </a>
            <a href="https://wa.me/6285341026331?text={{ urlencode('Halo Admin Aktama, saya mengalami kendala saat mengakses website.') }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-light rounded-pill px-4 py-2">
                <i class="bi bi-whatsapp text-success me-1"></i> Bantuan WhatsApp
            </a>
        </div>

        <div class="mt-4 pt-3 border-top border-secondary border-opacity-25 text-white-50 small">
            &copy; {{ date('Y') }} PT Aktama Digital Antika. Seluruh hak cipta dilindungi.
        </div>
    </div>
</body>
</html>
