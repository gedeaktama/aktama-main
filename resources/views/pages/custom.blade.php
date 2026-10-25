@extends('layouts.app')

@section('title', ($page->meta_title ?: $page->title) . ' | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', $page->meta_description ?: Str::limit(strip_tags($page->content_html), 150))
@if($page->featured_image)
    @section('og_image', asset('images/' . $page->featured_image))
@endif

@push('styles')
@if($page->content_css)
    <style>
        {!! $page->content_css !!}
    </style>
@endif
<style>
    .page-prose h2 { font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #0f172a; }
    .page-prose h3 { font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #1e293b; }
    .page-prose p { margin-bottom: 1.25rem; line-height: 1.8; color: #334155; }
    .page-prose img { max-width: 100%; height: auto; border-radius: 0.75rem; margin: 1.5rem 0; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
    .page-prose table { width: 100%; margin-bottom: 1.5rem; border-collapse: collapse; }
    .page-prose table th, .page-prose table td { border: 1px solid #e2e8f0; padding: 0.75rem 1rem; }
    .page-prose table th { background: #f8fafc; font-weight: 600; }
    .page-prose blockquote { border-left: 4px solid #6366f1; padding-left: 1.25rem; margin: 1.5rem 0; font-style: italic; color: #475569; }
</style>
@endpush

@section('content')

    @if($page->template !== 'blank')
        <!-- HERO HEADER HALAMAN -->
        <section class="py-4 py-md-5 bg-light border-bottom">
            <div class="container">
                <nav aria-label="breadcrumb">
                    <ol class="breadcrumb small mb-2">
                        <li class="breadcrumb-item"><a href="{{ route('home') }}" class="text-decoration-none">Beranda</a></li>
                        <li class="breadcrumb-item active" aria-current="page">{{ $page->title }}</li>
                    </ol>
                </nav>
                <h1 class="display-6 fw-bold font-display text-dark mb-0">{{ $page->title }}</h1>
            </div>
        </section>
    @endif

    <!-- CONTENT BODY HALAMAN -->
    <section class="py-5 bg-white">
        @if($page->template === 'full-width' || $page->editor_type === 'builder')
            <div class="container-fluid px-3 px-lg-5">
                <div class="custom-page-content page-prose">
                    {!! $page->content_html !!}
                </div>
            </div>
        @else
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-10">
                        @if($page->featured_image)
                            <div class="mb-4 text-center">
                                <img src="{{ asset('images/' . $page->featured_image) }}" alt="{{ $page->title }}" class="img-fluid rounded-4 shadow-sm w-100 object-fit-cover" style="max-height: 420px;">
                            </div>
                        @endif
                        <div class="card border-0 shadow-xs rounded-4 p-4 p-md-5 bg-white">
                            <article class="prose max-w-none lh-lg text-dark page-prose">
                                {!! $page->content_html !!}
                            </article>
                        </div>
                    </div>
                </div>
            </div>
        @endif
    </section>

@endsection
