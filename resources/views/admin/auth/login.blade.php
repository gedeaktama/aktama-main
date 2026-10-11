<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Administrator | Aktama Digital CMS</title>
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="{{ asset('images/logo-aktama.png') }}">
    @vite(['resources/scss/app.scss', 'resources/js/app.js'])
</head>
<body class="bg-brand-dark d-flex align-items-center justify-content-center min-vh-100 p-3">

    <div class="card border-0 shadow-lg rounded-4 p-4 p-md-5 bg-white max-w-md w-100" style="max-width: 420px;">
        <div class="text-center mb-4">
            <img src="{{ asset('images/logo-aktama.png') }}" alt="PT Aktama Digital Antika" class="mb-3 mx-auto d-block" style="max-height: 46px; width: auto; object-fit: contain;">
            <h4 class="fw-bold font-display text-dark mb-1">Masuk Panel Admin</h4>
            <small class="text-muted">PT Aktama Digital Antika</small>
        </div>

        @if(session('error'))
            <div class="alert alert-danger rounded-3 small py-2 d-flex align-items-center gap-2 mb-3">
                <i class="bi bi-exclamation-circle-fill"></i>
                <div>{{ session('error') }}</div>
            </div>
        @endif

        @if(session('success'))
            <div class="alert alert-success rounded-3 small py-2 d-flex align-items-center gap-2 mb-3">
                <i class="bi bi-check-circle-fill"></i>
                <div>{{ session('success') }}</div>
            </div>
        @endif

        <form action="{{ route('admin.login.submit') }}" method="POST">
            @csrf

            <div class="mb-3">
                <label for="email" class="form-label small fw-bold text-dark">Alamat Email</label>
                <div class="input-group">
                    <span class="input-group-text bg-light border-end-0"><i class="bi bi-envelope text-muted"></i></span>
                    <input type="email" class="form-control border-start-0" id="email" name="email" required value="{{ old('email', 'admin@aktama.com') }}" placeholder="admin@aktama.com">
                </div>
            </div>

            <div class="mb-3">
                <label for="password" class="form-label small fw-bold text-dark">Kata Sandi</label>
                <div class="input-group">
                    <span class="input-group-text bg-light border-end-0"><i class="bi bi-lock text-muted"></i></span>
                    <input type="password" class="form-control border-start-0" id="password" name="password" required placeholder="••••••••">
                </div>
            </div>

            <div class="d-flex justify-content-between align-items-center mb-4">
                <div class="form-check small">
                    <input class="form-check-input" type="checkbox" name="remember" id="remember">
                    <label class="form-check-label text-muted" for="remember">Ingat Saya</label>
                </div>
            </div>

            <button type="submit" class="btn btn-brand btn-lg w-100 rounded-pill shadow-sm fw-bold">
                <i class="bi bi-box-arrow-in-right me-1"></i> Masuk Sekarang
            </button>

            <div class="text-center mt-4">
                <a href="{{ route('home') }}" class="text-muted small text-decoration-none hover-primary">
                    <i class="bi bi-arrow-left me-1"></i> Kembali ke Website Publik
                </a>
            </div>
        </form>
    </div>

</body>
</html>
