@extends('layouts.app')

@section('title', ($page->meta_title ?: $page->title) . ' | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', $page->meta_description ?: Str::limit(strip_tags($page->content_html), 150))

@push('styles')
@if($page->content_css)
    <style>
        {!! $page->content_css !!}
    </style>
@endif
@endpush

@section('content')

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

    <!-- CONTENT BODY HALAMAN -->
    <section class="py-5 bg-white">
        <div class="container">
            @if($page->editor_type === 'builder')
                <div class="custom-page-builder-content">
                    {!! $page->content_html !!}
                </div>
            @else
                <div class="row justify-content-center">
                    <div class="col-lg-10">
                        <div class="card border-0 shadow-xs rounded-4 p-4 p-md-5 bg-white">
                            <article class="prose max-w-none lh-lg text-dark">
                                {!! $page->content_html !!}
                            </article>
                        </div>
                    </div>
                </div>
            @endif
        </div>
    </section>

@endsection
