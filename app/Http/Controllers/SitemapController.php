<?php

namespace App\Http\Controllers;

use App\Models\Article;
use Illuminate\Http\Response;

class SitemapController extends Controller
{
    public function index(): Response
    {
        $urls = [
            ['loc' => route('home'), 'priority' => '1.0', 'changefreq' => 'weekly'],
            ['loc' => route('about'), 'priority' => '0.8', 'changefreq' => 'monthly'],
            ['loc' => route('training'), 'priority' => '0.9', 'changefreq' => 'weekly'],
            ['loc' => route('services'), 'priority' => '0.9', 'changefreq' => 'weekly'],
            ['loc' => route('coffee'), 'priority' => '0.8', 'changefreq' => 'weekly'],
            ['loc' => route('invitations'), 'priority' => '0.8', 'changefreq' => 'weekly'],
            ['loc' => route('portfolios'), 'priority' => '0.7', 'changefreq' => 'monthly'],
            ['loc' => route('articles.index'), 'priority' => '0.8', 'changefreq' => 'daily'],
        ];

        $articles = Article::where('status', 'published')->orderByDesc('updated_at')->get();
        foreach ($articles as $article) {
            $urls[] = [
                'loc' => route('articles.show', $article->slug),
                'lastmod' => $article->updated_at->toAtomString(),
                'priority' => '0.7',
                'changefreq' => 'monthly',
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

        return response($xml, 200, ['Content-Type' => 'application/xml']);
    }
}
