@extends('layouts.admin')

@section('title', $article->exists ? 'Edit Postingan' : 'Tulis Postingan / Berita Baru')
@section('page_title', $article->exists ? 'Edit Postingan: ' . $article->title : 'Tulis Postingan / Berita Baru')

@section('content')

    <div class="row justify-content-center">
        <div class="col-lg-10">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
                <form action="{{ $article->exists ? route('admin.articles.update', $article->id) : route('admin.articles.store') }}" method="POST" enctype="multipart/form-data">
                    @csrf
                    @if($article->exists)
                        @method('PUT')
                    @endif

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Judul Postingan / Berita *</label>
                        <input type="text" name="title" id="article-title" class="form-control form-control-lg fw-bold" required value="{{ old('title', $article->title) }}" placeholder="Contoh: Terobosan Kecerdasan Artifisial untuk Efisiensi Pelayanan Publik">
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Slug / URL Permalink</label>
                        <div class="input-group">
                            <span class="input-group-text bg-light text-muted small">/artikel/</span>
                            <input type="text" name="slug" id="article-slug" class="form-control font-monospace" value="{{ old('slug', $article->slug) }}" placeholder="otomatis-dari-judul">
                        </div>
                    </div>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Kategori Berita</label>
                            <select name="category_id" class="form-select mb-2">
                                <option value="">Pilih Kategori Yang Ada...</option>
                                @foreach($categories as $cat)
                                    <option value="{{ $cat->id }}" {{ old('category_id', $article->category_id) == $cat->id ? 'selected' : '' }}>
                                        {{ $cat->name }}
                                    </option>
                                @endforeach
                            </select>
                            <input type="text" name="new_category" class="form-control form-control-sm" placeholder="Atau ketik kategori baru di sini...">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Penulis *</label>
                            <input type="text" name="author" class="form-control" required value="{{ old('author', $article->author ?? 'Gede Erik Aktama, S.Pd., M.Pd.') }}">
                        </div>
                    </div>

                    <!-- GAMBAR UTAMA / FEATURED IMAGE -->
                    <div class="card border rounded-3 p-3 bg-light mb-3">
                        <label class="form-label small fw-bold text-dark d-block">
                            <i class="bi bi-image text-primary me-1"></i> Gambar Unggulan (Featured Image / Thumbnail)
                        </label>
                        @if($article->image)
                            <div class="mb-2">
                                <img src="{{ asset('images/' . $article->image) }}" alt="Preview" class="rounded-3 shadow-xs object-fit-cover" style="max-height: 140px; max-width: 250px;">
                                <small class="text-muted d-block mt-1">Gambar saat ini. Pilih file baru di bawah jika ingin mengganti.</small>
                            </div>
                        @endif
                        <input type="file" name="image_file" class="form-control form-control-sm" accept="image/png,image/jpeg,image/webp">
                        <small class="text-muted" style="font-size: 0.75rem;">Format JPG, PNG, WEBP. Maksimal 2 MB.</small>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Ringkasan Singkat (Excerpt / Cuplikan)</label>
                        <textarea name="summary" class="form-control" rows="2" placeholder="1-2 kalimat ringkasan yang muncul pada kartu daftar berita...">{{ old('summary', $article->summary) }}</textarea>
                    </div>

                    <!-- TOOLBAR FORMATTING CEPAT -->
                    <div class="mb-1 d-flex flex-wrap gap-1 align-items-center">
                        <label class="form-label small fw-bold text-dark mb-0 me-2">Isi Konten Berita *</label>
                        <div class="btn-group btn-group-sm">
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<b>', '</b>')" title="Bold"><b>B</b></button>
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<i>', '</i>')" title="Italic"><i>I</i></button>
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<h3>', '</h3>')" title="Heading 3">H3</button>
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<h4>', '</h4>')" title="Heading 4">H4</button>
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<p>', '</p>')" title="Paragraf">&lt;p&gt;</button>
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<ul>\n  <li>', '</li>\n</ul>')" title="List">Bullet</button>
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<a href=\x22#\x22>', '</a>')" title="Link">Link</button>
                            <button type="button" class="btn btn-outline-secondary" onclick="insertTag('<blockquote class=\x22blockquote\x22>', '</blockquote>')" title="Kutipan">Quote</button>
                        </div>
                    </div>

                    <div class="mb-3">
                        <textarea name="content" id="article-content" class="form-control font-monospace" rows="12" required placeholder="Tuliskan isi berita lengkap di sini...">{{ old('content', $article->content) }}</textarea>
                        <small class="text-muted" style="font-size: 0.75rem;">Mendukung format HTML standar untuk teks, paragraf, gambar, dan tabel.</small>
                    </div>

                    <div class="border rounded-3 p-3 bg-light mb-4">
                        <strong class="text-dark small d-block mb-3"><i class="bi bi-search text-primary me-1"></i> Optimasi Meta SEO (Opsional):</strong>
                        <div class="row g-3">
                            <div class="col-12">
                                <label class="form-label small text-muted">Meta Title untuk Google</label>
                                <input type="text" name="meta_title" class="form-control" value="{{ old('meta_title', $article->meta_title) }}" placeholder="Judul khusus pencarian Google...">
                            </div>
                            <div class="col-12">
                                <label class="form-label small text-muted">Meta Description untuk Google</label>
                                <textarea name="meta_description" class="form-control" rows="2" placeholder="Deskripsi ringkas yang muncul di hasil pencarian...">{{ old('meta_description', $article->meta_description) }}</textarea>
                            </div>
                        </div>
                    </div>

                    <div class="row g-3 align-items-center mb-4">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Status Publikasi</label>
                            <select name="status" class="form-select">
                                <option value="published" {{ old('status', $article->status) === 'published' ? 'selected' : '' }}>Publikasikan Langsung (Published)</option>
                                <option value="draft" {{ old('status', $article->status) === 'draft' ? 'selected' : '' }}>Simpan sebagai Draf (Draft)</option>
                            </select>
                        </div>
                    </div>

                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-brand rounded-pill px-5">
                            <i class="bi bi-send-check me-1"></i> {{ $article->exists ? 'Perbarui Postingan' : 'Terbitkan Postingan' }}
                        </button>
                        <a href="{{ route('admin.articles.index') }}" class="btn btn-light border rounded-pill px-3">Batal</a>
                    </div>
                </form>
            </div>
        </div>
    </div>

@endsection

@push('scripts')
<script>
    function insertTag(openTag, closeTag) {
        const textarea = document.getElementById('article-content');
        if (!textarea) return;

        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        const text = textarea.value;
        const selected = text.substring(start, end);

        const replacement = openTag + (selected || 'teks') + closeTag;
        textarea.value = text.substring(0, start) + replacement + text.substring(end);
        textarea.focus();
        textarea.setSelectionRange(start + openTag.length, start + openTag.length + (selected ? selected.length : 4));
    }

    document.addEventListener('DOMContentLoaded', function () {
        const titleInput = document.getElementById('article-title');
        const slugInput = document.getElementById('article-slug');

        @if(!$article->exists)
        if (titleInput && slugInput) {
            titleInput.addEventListener('keyup', function () {
                if (!slugInput.dataset.manual) {
                    slugInput.value = this.value
                        .toLowerCase()
                        .trim()
                        .replace(/[^\w\s-]/g, '')
                        .replace(/[\s_-]+/g, '-')
                        .replace(/^-+|-+$/g, '');
                }
            });
            slugInput.addEventListener('input', function () {
                slugInput.dataset.manual = 'true';
            });
        }
        @endif
    });
</script>
@endpush
