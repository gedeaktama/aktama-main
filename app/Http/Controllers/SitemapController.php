<?php

namespace App\Http\Controllers;

use App\Models\Article;
use App\Models\Page;
use App\Models\Portfolio;
use App\Models\Service;
use App\Models\SiteSetting;
use App\Models\TrainingProgram;
use Illuminate\Http\Response;
use Illuminate\Support\Str;

class SitemapController extends Controller
{
    /**
     * Dynamic XML Sitemap untuk Google Bot & Mesin Pencari
     */
    public function index(): Response
    {
        $urls = [
            ['loc' => route('home'), 'priority' => '1.0', 'changefreq' => 'daily'],
            ['loc' => route('about'), 'priority' => '0.8', 'changefreq' => 'monthly'],
            ['loc' => route('training'), 'priority' => '0.9', 'changefreq' => 'weekly'],
            ['loc' => route('services'), 'priority' => '0.9', 'changefreq' => 'weekly'],
            ['loc' => route('coffee'), 'priority' => '0.8', 'changefreq' => 'weekly'],
            ['loc' => route('invitations'), 'priority' => '0.8', 'changefreq' => 'weekly'],
            ['loc' => route('portfolios'), 'priority' => '0.8', 'changefreq' => 'weekly'],
            ['loc' => route('articles.index'), 'priority' => '0.9', 'changefreq' => 'daily'],
        ];

        // 1. Artikel & Berita Diterbitkan
        $articles = Article::where('status', 'published')->orderByDesc('updated_at')->get();
        foreach ($articles as $article) {
            $urls[] = [
                'loc' => route('articles.show', $article->slug),
                'lastmod' => $article->updated_at->toAtomString(),
                'priority' => '0.8',
                'changefreq' => 'weekly',
            ];
        }

        // 2. Halaman Kustom & Landing Page Visual Builder Diterbitkan
        $pages = Page::where('is_published', true)->orderByDesc('updated_at')->get();
        foreach ($pages as $page) {
            $urls[] = [
                'loc' => route('pages.show', $page->slug),
                'lastmod' => $page->updated_at->toAtomString(),
                'priority' => '0.7',
                'changefreq' => 'weekly',
            ];
        }

        $xml = '<?xml version="1.0" encoding="UTF-8"?>';
        $xml .= '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">';

        foreach ($urls as $u) {
            $xml .= '<url>';
            $xml .= '<loc>' . htmlspecialchars($u['loc']) . '</loc>';
            if (isset($u['lastmod'])) {
                $xml .= '<lastmod>' . $u['lastmod'] . '</lastmod>';
            }
            $xml .= '<changefreq>' . ($u['changefreq'] ?? 'weekly') . '</changefreq>';
            $xml .= '<priority>' . ($u['priority'] ?? '0.5') . '</priority>';
            $xml .= '</url>';
        }

        $xml .= '</urlset>';

        return response($xml, 200, ['Content-Type' => 'application/xml; charset=utf-8']);
    }

    /**
     * Dynamic RSS 2.0 Feed untuk Sindikasi Berita & Google News
     */
    public function rss(): Response
    {
        $siteTitle = SiteSetting::get('company_name', 'PT Aktama Digital Antika');
        $siteDesc = SiteSetting::get('tagline', 'Solusi Teknologi, Pelatihan AI, dan Ekosistem Bisnis Digital');
        $articles = Article::where('status', 'published')->with('category')->orderByDesc('created_at')->limit(30)->get();

        $xml = '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
        $xml .= '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">' . "\n";
        $xml .= '  <channel>' . "\n";
        $xml .= '    <title>' . htmlspecialchars($siteTitle) . '</title>' . "\n";
        $xml .= '    <link>' . url('/') . '</link>' . "\n";
        $xml .= '    <description>' . htmlspecialchars($siteDesc) . '</description>' . "\n";
        $xml .= '    <language>id-ID</language>' . "\n";
        $xml .= '    <atom:link href="' . route('rss') . '" rel="self" type="application/rss+xml" />' . "\n";

        foreach ($articles as $article) {
            $xml .= '    <item>' . "\n";
            $xml .= '      <title>' . htmlspecialchars($article->title) . '</title>' . "\n";
            $xml .= '      <link>' . route('articles.show', $article->slug) . '</link>' . "\n";
            $xml .= '      <guid isPermaLink="true">' . route('articles.show', $article->slug) . '</guid>' . "\n";
            $xml .= '      <pubDate>' . ($article->published_at ? $article->published_at->toRssString() : $article->created_at->toRssString()) . '</pubDate>' . "\n";
            $xml .= '      <category>' . htmlspecialchars($article->category?->name ?? 'Teknologi') . '</category>' . "\n";
            $xml .= '      <description><![CDATA[' . ($article->summary ?: Str::limit(strip_tags($article->content), 200)) . ']]></description>' . "\n";
            $xml .= '    </item>' . "\n";
        }

        $xml .= '  </channel>' . "\n";
        $xml .= '</rss>';

        return response($xml, 200, ['Content-Type' => 'application/xml; charset=utf-8']);
    }
}
