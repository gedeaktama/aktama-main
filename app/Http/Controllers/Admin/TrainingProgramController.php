<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\TrainingProgram;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class TrainingProgramController extends Controller
{
    public function index(): View
    {
        $programs = TrainingProgram::orderBy('sort_order')->paginate(15);
        return view('admin.training.index', compact('programs'));
    }

    public function create(): View
    {
        return view('admin.training.form', ['program' => new TrainingProgram()]);
    }

    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:200',
            'category' => 'required|string|max:50',
            'target_audience' => 'required|string|max:255',
            'objectives' => 'nullable|string',
            'syllabus_text' => 'nullable|string',
            'delivery_format' => 'required|string|max:30',
            'duration' => 'nullable|string|max:100',
            'price_info' => 'nullable|string|max:100',
            'is_published' => 'boolean',
            'sort_order' => 'integer',
        ]);

        $syllabus = array_filter(array_map('trim', explode("\n", $request->input('syllabus_text', ''))));

        TrainingProgram::create([
            ...$validated,
            'slug' => Str::slug($request->title) . '-' . rand(100, 999),
            'syllabus' => $syllabus,
            'is_published' => $request->boolean('is_published'),
            'sort_order' => $request->input('sort_order', 0),
        ]);

        return redirect()->route('admin.training.index')->with('success', 'Program pelatihan berhasil ditambahkan!');
    }

    public function edit(TrainingProgram $training): View
    {
        return view('admin.training.form', ['program' => $training]);
    }

    public function update(Request $request, TrainingProgram $training): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:200',
            'category' => 'required|string|max:50',
            'target_audience' => 'required|string|max:255',
            'objectives' => 'nullable|string',
            'syllabus_text' => 'nullable|string',
            'delivery_format' => 'required|string|max:30',
            'duration' => 'nullable|string|max:100',
            'price_info' => 'nullable|string|max:100',
            'is_published' => 'boolean',
            'sort_order' => 'integer',
        ]);

        $syllabus = array_filter(array_map('trim', explode("\n", $request->input('syllabus_text', ''))));

        $training->update([
            ...$validated,
            'syllabus' => $syllabus,
            'is_published' => $request->boolean('is_published'),
            'sort_order' => $request->input('sort_order', 0),
        ]);

        return redirect()->route('admin.training.index')->with('success', 'Program pelatihan berhasil diperbarui!');
    }

    public function destroy(TrainingProgram $training): RedirectResponse
    {
        $training->delete();
        return redirect()->route('admin.training.index')->with('success', 'Program pelatihan berhasil dihapus.');
    }
}
