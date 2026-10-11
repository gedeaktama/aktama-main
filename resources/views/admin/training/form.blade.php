@extends('layouts.admin')

@section('title', $program->exists ? 'Edit Program Pelatihan' : 'Tambah Pelatihan Baru')
@section('page_title', $program->exists ? 'Edit Pelatihan: ' . $program->title : 'Tambah Pelatihan Baru')

@section('content')

    <div class="card border-0 shadow-sm rounded-4 bg-white p-4 max-w-2xl">
        <form action="{{ $program->exists ? route('admin.training.update', $program->id) : route('admin.training.store') }}" method="POST">
            @csrf
            @if($program->exists)
                @method('PUT')
            @endif

            <div class="row g-3 mb-3">
                <div class="col-md-8">
                    <label class="form-label small fw-bold text-dark">Judul Program Pelatihan *</label>
                    <input type="text" name="title" class="form-control" required value="{{ old('title', $program->title) }}" placeholder="Contoh: AI untuk Efisiensi Administrasi Perkantoran">
                </div>
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-dark">Kategori *</label>
                    <select name="category" class="form-select" required>
                        <option value="ai-kantor" {{ old('category', $program->category) === 'ai-kantor' ? 'selected' : '' }}>AI Kantor</option>
                        <option value="ai-pendidikan" {{ old('category', $program->category) === 'ai-pendidikan' ? 'selected' : '' }}>AI Tenaga Pendidik</option>
                        <option value="ai-bisnis" {{ old('category', $program->category) === 'ai-bisnis' ? 'selected' : '' }}>AI Bisnis / UMKM</option>
                        <option value="coding" {{ old('category', $program->category) === 'coding' ? 'selected' : '' }}>Koding & Komputasi</option>
                    </select>
                </div>
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Target Sasaran Peserta *</label>
                <input type="text" name="target_audience" class="form-control" required value="{{ old('target_audience', $program->target_audience) }}" placeholder="Contoh: Staf Tata Usaha, Sekretaris, Admin Kantor...">
            </div>

            <div class="row g-3 mb-3">
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-dark">Format Pelaksanaan *</label>
                    <select name="delivery_format" class="form-select" required>
                        <option value="hybrid" {{ old('delivery_format', $program->delivery_format) === 'hybrid' ? 'selected' : '' }}>Hybrid (Online & Tatap Muka)</option>
                        <option value="online" {{ old('delivery_format', $program->delivery_format) === 'online' ? 'selected' : '' }}>Online (Webinar / Zoom)</option>
                        <option value="offline" {{ old('delivery_format', $program->delivery_format) === 'offline' ? 'selected' : '' }}>Offline (In-House / Tatap Muka)</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-dark">Durasi Pelatihan</label>
                    <input type="text" name="duration" class="form-control" value="{{ old('duration', $program->duration) }}" placeholder="Contoh: 2 Hari (16 Jam)">
                </div>
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-dark">Informasi Biaya</label>
                    <input type="text" name="price_info" class="form-control" value="{{ old('price_info', $program->price_info) }}" placeholder="Contoh: Sesuai Penawaran Instansi">
                </div>
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Tujuan Pembelajaran / Manfaat Program</label>
                <textarea name="objectives" class="form-control" rows="3">{{ old('objectives', $program->objectives) }}</textarea>
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Pokok Bahasan & Silabus (1 Topik per Baris)</label>
                <textarea name="syllabus_text" class="form-control" rows="5" placeholder="Pengenalan Dasar AI&#10;Teknik Prompt Engineering Dokumen&#10;Otomasi Tabel Spreadsheet">{{ old('syllabus_text', is_array($program->syllabus) ? implode("\n", $program->syllabus) : '') }}</textarea>
            </div>

            <div class="form-check form-switch mb-4">
                <input class="form-check-input" type="checkbox" name="is_published" value="1" id="is_published" {{ old('is_published', $program->is_published ?? true) ? 'checked' : '' }}>
                <label class="form-check-label text-dark fw-bold small" for="is_published">Publikasikan Program Pelatihan Ini</label>
            </div>

            <div class="d-flex gap-2">
                <button type="submit" class="btn btn-brand rounded-pill px-4">
                    <i class="bi bi-save me-1"></i> Simpan Pelatihan
                </button>
                <a href="{{ route('admin.training.index') }}" class="btn btn-light border rounded-pill px-3">Batal</a>
            </div>
        </form>
    </div>

@endsection
