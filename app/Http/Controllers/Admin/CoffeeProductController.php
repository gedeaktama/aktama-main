<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\CoffeeProduct;
use App\Models\CoffeeProductVariant;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class CoffeeProductController extends Controller
{
    public function index(): View
    {
        $products = CoffeeProduct::with('variants')->paginate(15);
        return view('admin.coffee.index', compact('products'));
    }

    public function create(): View
    {
        return view('admin.coffee.form', ['product' => new CoffeeProduct()]);
    }

    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'name' => 'required|string|max:150',
            'sku' => 'nullable|string|max:50',
            'origin' => 'nullable|string|max:100',
            'roast_level' => 'nullable|string|max:50',
            'description' => 'nullable|string',
            'is_published' => 'boolean',
        ]);

        $product = CoffeeProduct::create([
            ...$validated,
            'slug' => Str::slug($request->name) . '-' . rand(100, 999),
            'is_published' => $request->boolean('is_published'),
        ]);

        // Default variant
        CoffeeProductVariant::create([
            'coffee_product_id' => $product->id,
            'variant_name' => 'Kemasan 250g',
            'weight_grams' => 250,
            'retail_price' => $request->input('default_retail_price', 35000),
            'wholesale_price' => $request->input('default_wholesale_price', 28000),
            'min_wholesale_qty' => 10,
            'is_active' => true,
        ]);

        return redirect()->route('admin.coffee.index')->with('success', 'Produk kopi berhasil ditambahkan!');
    }

    public function edit(CoffeeProduct $coffee): View
    {
        $coffee->load('variants');
        return view('admin.coffee.form', ['product' => $coffee]);
    }

    public function update(Request $request, CoffeeProduct $coffee): RedirectResponse
    {
        $validated = $request->validate([
            'name' => 'required|string|max:150',
            'sku' => 'nullable|string|max:50',
            'origin' => 'nullable|string|max:100',
            'roast_level' => 'nullable|string|max:50',
            'description' => 'nullable|string',
            'is_published' => 'boolean',
        ]);

        $coffee->update([
            ...$validated,
            'is_published' => $request->boolean('is_published'),
        ]);

        return redirect()->route('admin.coffee.index')->with('success', 'Produk kopi berhasil diperbarui!');
    }

    public function storeVariant(Request $request, CoffeeProduct $coffee): RedirectResponse
    {
        $validated = $request->validate([
            'variant_name' => 'required|string|max:100',
            'weight_grams' => 'required|integer|min:1',
            'retail_price' => 'required|numeric|min:0',
            'wholesale_price' => 'nullable|numeric|min:0',
            'min_wholesale_qty' => 'required|integer|min:1',
        ]);

        $coffee->variants()->create([
            ...$validated,
            'is_active' => true,
        ]);

        return back()->with('success', 'Varian kopi berhasil ditambahkan!');
    }

    public function destroyVariant(CoffeeProductVariant $variant): RedirectResponse
    {
        $variant->delete();
        return back()->with('success', 'Varian kopi berhasil dihapus.');
    }

    public function destroy(CoffeeProduct $coffee): RedirectResponse
    {
        $coffee->delete();
        return redirect()->route('admin.coffee.index')->with('success', 'Produk kopi berhasil dihapus.');
    }
}
