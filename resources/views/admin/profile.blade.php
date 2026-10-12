@extends('layouts.admin')

@section('title', 'Profil & Keamanan Akun')
@section('page_title', 'Profil Administrator & Keamanan Akun')

@section('content')

    <div class="row g-4 max-w-4xl">
        <!-- Kolom Kiri: Informasi Akun -->
        <div class="col-lg-5">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4 h-100">
                <div class="text-center mb-4">
                    <div class="rounded-circle bg-primary bg-opacity-10 text-primary d-inline-flex align-items-center justify-content-center mb-3" style="width: 80px; height: 80px;">
                        <i class="bi bi-person-badge-fill fs-1"></i>
                    </div>
                    <h5 class="fw-bold text-dark mb-1">{{ $user->name }}</h5>
                    <span class="badge bg-success bg-opacity-10 text-success fw-semibold text-uppercase px-3 py-1">
                        <i class="bi bi-shield-check me-1"></i> {{ ucfirst($user->role) }}
                    </span>
                </div>

                <div class="border rounded-3 p-3 bg-light mb-3">
                    <div class="small text-muted mb-1">Alamat Email Login</div>
                    <div class="fw-semibold text-dark">{{ $user->email }}</div>
                </div>

                <div class="border rounded-3 p-3 bg-light mb-3">
                    <div class="small text-muted mb-1">Status Keamanan Akun</div>
                    <div class="fw-semibold text-success"><i class="bi bi-patch-check-fill me-1"></i> Aktif & Terlindungi</div>
                </div>

                <div class="border rounded-3 p-3 bg-light">
                    <div class="small text-muted mb-1">Terdaftar Sejak</div>
                    <div class="fw-semibold text-dark">{{ $user->created_at?->format('d F Y, H:i') ?? '-' }}</div>
                </div>
            </div>
        </div>

        <!-- Kolom Kanan: Form Ubah Password -->
        <div class="col-lg-7">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4 p-md-5">
                <div class="d-flex align-items-center gap-2 mb-3">
                    <i class="bi bi-key-fill text-primary fs-4"></i>
                    <h5 class="fw-bold text-dark mb-0">Ubah Kata Sandi (Password)</h5>
                </div>
                <p class="text-muted small mb-4">
                    Demi keamanan server produksi, ganti kata sandi default sistem dengan kata sandi yang kuat dan unik (minimal 8 karakter kombinasi huruf, angka, dan simbol).
                </p>

                @if ($errors->any())
                    <div class="alert alert-danger rounded-3 small mb-4">
                        <ul class="mb-0 ps-3">
                            @foreach ($errors->all() as $error)
                                <li>{{ $error }}</li>
                            @endforeach
                        </ul>
                    </div>
                @endif

                <form action="{{ route('admin.profile.password') }}" method="POST">
                    @csrf
                    @method('PUT')

                    <div class="mb-3">
                        <label for="current_password" class="form-label small fw-bold text-dark">Kata Sandi Saat Ini *</label>
                        <input type="password" class="form-control rounded-3" id="current_password" name="current_password" required placeholder="Masukkan kata sandi lama">
                    </div>

                    <div class="mb-3">
                        <label for="password" class="form-label small fw-bold text-dark">Kata Sandi Baru *</label>
                        <input type="password" class="form-control rounded-3" id="password" name="password" required minlength="8" placeholder="Minimal 8 karakter">
                    </div>

                    <div class="mb-4">
                        <label for="password_confirmation" class="form-label small fw-bold text-dark">Konfirmasi Kata Sandi Baru *</label>
                        <input type="password" class="form-control rounded-3" id="password_confirmation" name="password_confirmation" required minlength="8" placeholder="Ulangi kata sandi baru">
                    </div>

                    <div class="d-flex justify-content-end">
                        <button type="submit" class="btn btn-brand rounded-pill px-4 py-2">
                            <i class="bi bi-shield-lock-fill me-1"></i> Perbarui Kata Sandi
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

@endsection
