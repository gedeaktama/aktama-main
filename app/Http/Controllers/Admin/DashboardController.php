<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Article;
use App\Models\CoffeeProduct;
use App\Models\HomeSection;
use App\Models\Lead;
use App\Models\Page;
use App\Models\Portfolio;
use App\Models\Service;
use App\Models\TrainingProgram;
use Illuminate\View\View;

class DashboardController extends Controller
{
    public function index(): View
    {
        $stats = [
            'total_leads' => Lead::count(),
            'new_leads' => Lead::where('status', 'new')->count(),
            'services_count' => Service::count(),
            'training_count' => TrainingProgram::count(),
            'coffee_count' => CoffeeProduct::count(),
            'portfolios_count' => Portfolio::count(),
            'articles_count' => Article::count(),
            'pages_count' => Page::count(),
            'sections_count' => HomeSection::count(),
        ];

        $recentLeads = Lead::orderByDesc('created_at')->take(6)->get();

        return view('admin.dashboard', compact('stats', 'recentLeads'));
    }
}
