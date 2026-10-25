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
            'slug' => 'nullable|string|max:200|unique:training_programs,slug',
            'category' => 'required|string|max:50',
            'target_audience' => 'required|string|max:255',
            'objectives' => 'nullable|string',
            'syllabus_text' => 'nullable|string',
            'delivery_format' => 'required|string|max:30',
            'duration' => 'nullable|string|max:100',
            'price_info' => 'nullable|string|max:100',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'is_published' => 'nullable|boolean',
            'sort_order' => 'nullable|integer',
        ]);

        $syllabus = array_filter(array_map('trim', explode("\n", $request->input('syllabus_text', ''))));

        $imagePath = null;
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/training');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'training-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'training/' . $fileName;
        }

        $slug = !empty($validated['slug']) ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        $originalSlug = $slug;
        $counter = 1;
        while (TrainingProgram::where('slug', $slug)->exists()) {
            $slug = $originalSlug . '-' . $counter++;
        }

        TrainingProgram::create([
            'title' => $validated['title'],
            'slug' => $slug,
            'category' => $validated['category'],
            'target_audience' => $validated['target_audience'],
            'objectives' => $validated['objectives'] ?? null,
            'syllabus' => $syllabus,
            'delivery_format' => $validated['delivery_format'],
            'duration' => $validated['duration'] ?? null,
            'price_info' => $validated['price_info'] ?? null,
            'image' => $imagePath,
            'is_published' => $request->has('is_published'),
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
            'slug' => 'required|string|max:200|unique:training_programs,slug,' . $training->id,
            'category' => 'required|string|max:50',
            'target_audience' => 'required|string|max:255',
            'objectives' => 'nullable|string',
            'syllabus_text' => 'nullable|string',
            'delivery_format' => 'required|string|max:30',
            'duration' => 'nullable|string|max:100',
            'price_info' => 'nullable|string|max:100',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'remove_image' => 'nullable|boolean',
            'is_published' => 'nullable|boolean',
            'sort_order' => 'nullable|integer',
        ]);

        $syllabus = array_filter(array_map('trim', explode("\n", $request->input('syllabus_text', ''))));

        $imagePath = $training->image;
        if ($request->boolean('remove_image')) {
            $imagePath = null;
        }
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/training');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'training-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'training/' . $fileName;
        }

        $training->update([
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'category' => $validated['category'],
            'target_audience' => $validated['target_audience'],
            'objectives' => $validated['objectives'] ?? null,
            'syllabus' => $syllabus,
            'delivery_format' => $validated['delivery_format'],
            'duration' => $validated['duration'] ?? null,
            'price_info' => $validated['price_info'] ?? null,
            'image' => $imagePath,
            'is_published' => $request->has('is_published'),
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
