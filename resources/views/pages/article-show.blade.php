@extends('layouts.app')

@section('title', ($article->meta_title ?: $article->title) . ' | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', $article->meta_description ?: $article->summary)

@section('content')

    <style>
        .article-content h2 {
            font-size: 1.55rem;
            font-weight: 700;
            color: #0f172a;
            margin-top: 2.25rem;
            margin-bottom: 1.1rem;
            border-left: 4px solid #4f46e5;
            padding-left: 0.85rem;
            line-height: 1.35;
            scroll-margin-top: 80px;
        }
        .article-content h3 {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1e293b;
            margin-top: 1.75rem;
            margin-bottom: 0.85rem;
            scroll-margin-top: 80px;
        }
        .article-content p {
            margin-bottom: 1.35rem;
            color: #334155;
            font-size: 1.05rem;
            line-height: 1.85;
        }
        .article-content ul, .article-content ol {
            margin-bottom: 1.6rem;
            padding-left: 1.6rem;
            color: #334155;
            font-size: 1.02rem;
            line-height: 1.8;
        }
        .article-content li {
            margin-bottom: 0.6rem;
        }
        .article-content blockquote {
            border-left: 4px solid #6366f1;
            background: #f8fafc;
            padding: 1.25rem 1.5rem;
            border-radius: 0 0.75rem 0.75rem 0;
            font-style: italic;
            color: #475569;
            margin: 2rem 0;
            line-height: 1.75;
        }
        .article-content .callout-card {
            background: linear-gradient(135deg, #f0fdf4 0%, #eff6ff 100%);
            border: 1px solid #bfdbfe;
            border-radius: 1rem;
            padding: 1.5rem 1.75rem;
            margin: 2.25rem 0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .article-content code {
            color: #4338ca;
            background-color: #eef2ff;
            padding: 0.2rem 0.45rem;
            border-radius: 0.35rem;
            font-size: 0.9em;
        }
        .article-content table {
            margin: 1.5rem 0;
            width: 100%;
        }
        .article-content .prompt-box {
            background-color: #0f172a;
            color: #f1f5f9;
            border-radius: 0.75rem;
            padding: 1.25rem 1.5rem;
            margin: 1.75rem 0;
            font-size: 0.95rem;
            border-left: 4px solid #38bdf8;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            line-height: 1.7;
        }
        .article-content .prompt-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 0.5rem;
            margin-bottom: 0.75rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.15);
            font-size: 0.8rem;
            color: #38bdf8;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .article-content .output-box {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-left: 4px solid #10b981;
            border-radius: 0.75rem;
            padding: 1.25rem 1.5rem;
            margin: 1.75rem 0;
            font-size: 0.95rem;
            line-height: 1.7;
        }
        .toc-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 2.5rem;
        }
        .toc-list {
            list-style: none;
            padding-left: 0;
            margin-bottom: 0;
        }
        .toc-list li {
            margin-bottom: 0.5rem;
            font-size: 0.95rem;
        }
        .toc-list li.toc-h3 {
            padding-left: 1.25rem;
            font-size: 0.88rem;
        }
        .toc-list a {
            color: #334155;
            text-decoration: none;
            transition: color 0.15s;
        }
        .toc-list a:hover {
            color: #2563eb;
            text-decoration: underline;
        }
    </style>

    <!-- Header Breadcrumb & Judul -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-2 max-w-3xl">
            <nav aria-label="breadcrumb" class="mb-3">
                <ol class="breadcrumb small">
                    <li class="breadcrumb-item"><a href="{{ route('home') }}" class="text-decoration-none">Beranda</a></li>
                    <li class="breadcrumb-item"><a href="{{ route('articles.index') }}" class="text-decoration-none">Artikel</a></li>
                    @if($article->category)
                        <li class="breadcrumb-item"><a href="{{ route('articles.index', ['kategori' => $article->category->slug]) }}" class="text-decoration-none">{{ $article->category->name }}</a></li>
                    @endif
                    <li class="breadcrumb-item active text-truncate" aria-current="page" style="max-width: 250px;">{{ $article->title }}</li>
                </ol>
            </nav>

            <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">
                {{ $article->category?->name ?? 'Wawasan Teknologi' }}
            </span>
            <h1 class="display-6 fw-bold font-display text-dark mb-3">{{ $article->title }}</h1>

            <div class="d-flex flex-wrap align-items-center gap-3 small text-muted">
                <span><i class="bi bi-person me-1"></i> {{ $article->author }}</span>
                <span>&bull;</span>
                <span><i class="bi bi-calendar3 me-1"></i> {{ $article->published_at?->format('d F Y') ?? date('d F Y') }}</span>
                <span>&bull;</span>
                <span><i class="bi bi-clock me-1"></i> {{ max(3, ceil(str_word_count(strip_tags($article->content)) / 180)) }} menit baca</span>
            </div>
        </div>
    </section>

    <!-- Isi Artikel Lengkap -->
    <section class="py-5 bg-white">
        <div class="container py-2 max-w-3xl">
            @if($article->image)
                <div class="mb-4 text-center">
                    <img src="{{ asset('images/' . $article->image) }}" alt="{{ $article->title }}" class="img-fluid rounded-4 shadow-sm object-fit-cover w-100" style="max-height: 440px;">
                </div>
            @endif

            <!-- DAFTAR ISI OTOMATIS (TABLE OF CONTENTS) -->
            <div id="tableOfContentsContainer" class="toc-card d-none">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <h6 class="fw-bold text-dark mb-0 d-flex align-items-center gap-2">
                        <i class="bi bi-list-nested text-primary fs-5"></i>
                        <span>Daftar Isi Artikel</span>
                    </h6>
                    <button type="button" id="btnToggleToc" class="btn btn-sm btn-link text-muted p-0 text-decoration-none" style="font-size: 0.8rem;">
                        [Sembunyikan]
                    </button>
                </div>
                <div id="tocContent">
                    <hr class="my-2 border-secondary border-opacity-25">
                    <ul id="tocList" class="toc-list">
                        <!-- Populated by JS -->
                    </ul>
                </div>
            </div>

            <!-- Konten Artikel -->
            <div id="mainArticleContent" class="article-content fs-6 text-dark leading-relaxed mb-5">
                {!! $article->content !!}
            </div>

            <!-- Author Bio Card (Membangun Otoritas Pakar) -->
            <div class="card border rounded-4 p-4 mb-5 bg-light bg-opacity-50 shadow-xs">
                <div class="d-flex flex-column flex-sm-row align-items-sm-center gap-3">
                    <img src="{{ asset('images/gede-erik-aktama.jpg') }}" alt="{{ $article->author }}" class="rounded-circle object-fit-cover shadow-xs border" style="width: 72px; height: 72px; min-width: 72px;">
                    <div>
                        <div class="d-flex align-items-center gap-2 mb-1">
                            <h6 class="fw-bold text-dark mb-0">{{ $article->author }}</h6>
                            <span class="badge bg-success bg-opacity-10 text-success small" style="font-size: 0.7rem;">Verified Author & Researcher</span>
                        </div>
                        <p class="text-muted small mb-2">
                            Direktur PT Aktama Digital Antika • Dosen & Peneliti Sistem Komputer Univ. Parna Raya • Fasilitator Nasional KKA Kemdikdasmen.
                        </p>
                        <a href="https://profil.aktama.com" target="_blank" rel="noopener noreferrer" class="small text-primary text-decoration-none fw-semibold">
                            Lihat Profil Akademik & Publikasi Jurnal SINTA <i class="bi bi-arrow-up-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Share Buttons Lengkap -->
            <div class="p-4 rounded-4 bg-light border d-flex flex-wrap align-items-center justify-content-between gap-3 mb-5">
                <div>
                    <h6 class="fw-bold text-dark mb-1"><i class="bi bi-share me-1 text-primary"></i> Bagikan Wawasan Ini:</h6>
                    <small class="text-muted">Bantu rekan instansi atau komunitas Anda mendapatkan wawasan strategis ini.</small>
                </div>
                <div class="d-flex flex-wrap gap-2">
                    <a href="https://api.whatsapp.com/send?text={{ urlencode($article->title . "\n\n" . url()->current()) }}" target="_blank" rel="noopener noreferrer" class="btn btn-success btn-sm rounded-pill px-3 shadow-xs">
                        <i class="bi bi-whatsapp me-1"></i> WhatsApp
                    </a>
                    <a href="https://www.linkedin.com/sharing/share-offsite/?url={{ urlencode(url()->current()) }}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm rounded-pill px-3 shadow-xs" style="background-color: #0077b5; border-color: #0077b5;">
                        <i class="bi bi-linkedin me-1"></i> LinkedIn
                    </a>
                    <a href="https://www.facebook.com/sharer/sharer.php?u={{ urlencode(url()->current()) }}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm rounded-pill px-3 shadow-xs" style="background-color: #1877f2; border-color: #1877f2;">
                        <i class="bi bi-facebook me-1"></i> Facebook
                    </a>
                    <a href="https://twitter.com/intent/tweet?text={{ urlencode($article->title) }}&url={{ urlencode(url()->current()) }}" target="_blank" rel="noopener noreferrer" class="btn btn-dark btn-sm rounded-pill px-3 shadow-xs">
                        <i class="bi bi-twitter-x me-1"></i> X
                    </a>
                    <button type="button" class="btn btn-outline-secondary btn-sm rounded-pill px-3 shadow-xs" id="btnCopyLink" onclick="copyArticleLink()">
                        <i class="bi bi-link-45deg me-1"></i> <span id="copyLinkText">Salin Tautan</span>
                    </button>
                </div>
            </div>

            <!-- Call-To-Action Banner Konsultasi / Pelatihan -->
            <div class="card border-0 rounded-4 p-4 p-md-5 mb-5 text-white position-relative overflow-hidden shadow-sm" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);">
                <div class="position-relative" style="z-index: 2;">
                    <span class="badge bg-info bg-opacity-25 text-info fw-bold text-uppercase px-3 py-1 mb-2">Konsultasi Resmi</span>
                    <h4 class="fw-bold font-display mb-2">Butuh Pelatihan Serupa atau Solusi Rekayasa Website?</h4>
                    <p class="text-white-50 small mb-4" style="max-width: 600px;">
                        PT Aktama Digital Antika siap menghadirkan program pelatihan in-house bersertifikat LPK resmi maupun pembuatan website & sistem informasi berstandar enterprise bebas dari celah injeksi malware.
                    </p>
                    <div class="d-flex flex-wrap gap-2">
                        <a href="https://wa.me/{{ $settings['whatsapp_number'] ?? '6285341026331' }}?text={{ urlencode('Halo PT Aktama Digital Antika, saya tertarik setelah membaca artikel ' . $article->title . ' dan ingin berkonsultasi mengenai solusi yang relevan.') }}" target="_blank" rel="noopener noreferrer" class="btn btn-success rounded-pill px-4 py-2 fw-semibold shadow-sm">
                            <i class="bi bi-whatsapp me-1"></i> Konsultasi via WhatsApp
                        </a>
                        <a href="{{ route('home') }}#form-konsultasi" class="btn btn-outline-light rounded-pill px-4 py-2 fw-semibold">
                            Minta Proposal Penawaran
                        </a>
                    </div>
                </div>
            </div>

            <!-- Artikel Terkait -->
            @if($relatedArticles->count() > 0)
                <div class="border-top pt-4">
                    <h5 class="fw-bold font-display text-dark mb-4">Artikel Terkait dalam Topik Serupa</h5>
                    <div class="row g-3">
                        @foreach($relatedArticles as $rel)
                            <div class="col-md-4">
                                <div class="card h-100 p-3 rounded-4 border bg-light shadow-xs hover-lift">
                                    @if($rel->image)
                                        <img src="{{ asset('images/' . $rel->image) }}" alt="{{ $rel->title }}" class="img-fluid rounded-3 mb-2 object-fit-cover w-100" style="height: 100px;">
                                    @endif
                                    <h6 class="fw-bold text-dark fs-6 mb-2">
                                        <a href="{{ route('articles.show', $rel->slug) }}" class="text-dark text-decoration-none hover-primary">
                                            {{ $rel->title }}
                                        </a>
                                    </h6>
                                    <small class="text-muted mt-auto" style="font-size: 0.75rem;">{{ $rel->published_at?->format('d M Y') }}</small>
                                </div>
                            </div>
                        @endforeach
                    </div>
                </div>
            @endif
        </div>
    </section>

    <!-- Script Table of Contents & Copy Link -->
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // 1. GENERATE DAFTAR ISI OTOMATIS
            const content = document.getElementById('mainArticleContent');
            const tocContainer = document.getElementById('tableOfContentsContainer');
            const tocList = document.getElementById('tocList');
            const btnToggleToc = document.getElementById('btnToggleToc');
            const tocContent = document.getElementById('tocContent');

            if (content && tocContainer && tocList) {
                const headings = content.querySelectorAll('h2, h3');
                if (headings.length >= 2) {
                    tocContainer.classList.remove('d-none');

                    headings.forEach((h, index) => {
                        let id = h.id;
                        if (!id) {
                            id = 'section-' + (index + 1) + '-' + h.textContent.trim().toLowerCase()
                                .replace(/[^\w\s-]/g, '')
                                .replace(/[\s_-]+/g, '-')
                                .replace(/^-+|-+$/g, '');
                            h.id = id;
                        }

                        const li = document.createElement('li');
                        li.className = h.tagName.toLowerCase() === 'h3' ? 'toc-h3' : 'toc-h2';

                        const icon = h.tagName.toLowerCase() === 'h3' ? 'bi-dot text-muted' : 'bi-chevron-right text-primary';
                        li.innerHTML = `<a href="#${id}"><i class="bi ${icon} me-1 small"></i>${h.textContent.trim()}</a>`;
                        tocList.appendChild(li);
                    });

                    // Toggle expand/collapse TOC
                    if (btnToggleToc && tocContent) {
                        btnToggleToc.addEventListener('click', function () {
                            if (tocContent.classList.contains('d-none')) {
                                tocContent.classList.remove('d-none');
                                btnToggleToc.textContent = '[Sembunyikan]';
                            } else {
                                tocContent.classList.add('d-none');
                                btnToggleToc.textContent = '[Tampilkan]';
                            }
                        });
                    }
                }
            }
        });

        // 2. COPY LINK HELPER
        function copyArticleLink() {
            navigator.clipboard.writeText(window.location.href).then(() => {
                const btnText = document.getElementById('copyLinkText');
                if (btnText) {
                    const original = btnText.textContent;
                    btnText.textContent = 'Tersalin!';
                    setTimeout(() => {
                        btnText.textContent = original;
                    }, 2000);
                }
            }).catch(err => {
                prompt('Salin tautan berikut:', window.location.href);
            });
        }
    </script>

@endsection
