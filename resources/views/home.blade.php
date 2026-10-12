@extends('layouts.app')

@section('title', ($settings['brand_name'] ?? 'Aktama Digital') . ' | Solusi Teknologi, Pelatihan AI, dan Ekosistem Bisnis')
@section('meta_description', $settings['meta_default_description'] ?? 'PT Aktama Digital Antika menghadirkan solusi teknologi terpadu: Pelatihan Kecerdasan Artifisial (AI), Jasa Pembuatan Website, Aktama Academy, Undangan Digital, dan Distribusi Kopi.')

@section('content')

    {{-- OPSI A: MODULAR DYNAMIC SECTIONS LOOP --}}
    @if(isset($homeSections) && $homeSections->isNotEmpty())
        @foreach($homeSections as $section)
            @if($section->is_active)
                @includeIf('partials.home.' . $section->section_key, ['sectionConfig' => $section])
            @endif
        @endforeach
    @else
        {{-- Fallback jika seksi database belum terisi --}}
        @include('partials.home.hero', ['sectionConfig' => null])
        @include('partials.home.jasa_website', ['sectionConfig' => null])
        @include('partials.home.pelatihan_ai', ['sectionConfig' => null])
        @include('partials.home.ekosistem_digital', ['sectionConfig' => null])
        @include('partials.home.portofolio', ['sectionConfig' => null])
        @include('partials.home.tentang_kami', ['sectionConfig' => null])
        @include('partials.home.artikel', ['sectionConfig' => null])
        @include('partials.home.form_konsultasi', ['sectionConfig' => null])
    @endif

@endsection
