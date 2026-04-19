import os

schema = """
{% schema %}
{
  "name": "TQS Collection Page",
  "settings": [
    {
      "type": "header",
      "content": "Collection Settings"
    },
    {
      "type": "text",
      "id": "mobile_subtitle",
      "label": "Mobile Subtitle",
      "default": "Curated botanical remedies for daily vitality."
    }
  ],
  "presets": [
    {
      "name": "TQS Collection Page"
    }
  ]
}
{% endschema %}
"""

desktop_view = """
        <!-- Desktop UI -->
        <div class="hidden md:flex flex-row max-w-[1600px] mx-auto w-full px-6 py-12 gap-12">
            <!-- Left Sidebar Filters -->
            <aside class="w-full md:w-64 flex-shrink-0 space-y-12">
                <div class="space-y-6">
                    <h3 class="font-headline font-bold text-lg tracking-tight text-primary">Category</h3>
                    <div class="space-y-4 font-label text-sm text-on-surface-variant flex flex-col">
                        <a href="/collections/all" class="group transition-colors w-full {% if active_collection == 'all' %}font-bold text-primary{% else %}hover:text-primary{% endif %}">
                            All Skincare
                        </a>
                        <a href="/collections/face-wash" class="group transition-colors w-full {% if active_collection == 'face-wash' %}font-bold text-primary{% else %}hover:text-primary{% endif %}">
                            Cleansers
                        </a>
                        <a href="/collections/serums" class="group transition-colors w-full {% if active_collection == 'serums' %}font-bold text-primary{% else %}hover:text-primary{% endif %}">
                            Serums & Oils
                        </a>
                        <a href="/collections/creams" class="group transition-colors w-full {% if active_collection == 'creams' %}font-bold text-primary{% else %}hover:text-primary{% endif %}">
                            Moisturizers
                        </a>
                    </div>
                </div>
                <div class="space-y-6 opacity-60">
                    <h3 class="font-headline font-bold text-lg tracking-tight text-primary">Key Ingredients (Tags)</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-secondary-container text-on-surface px-3 py-1.5 rounded-full font-label text-xs">Saffron</span>
                        <span class="bg-secondary-container text-on-surface px-3 py-1.5 rounded-full font-label text-xs">Turmeric</span>
                        <span class="bg-surface-container text-on-surface-variant px-3 py-1.5 rounded-full font-label text-xs">Neem</span>
                    </div>
                    <p class="text-xs italic text-on-surface-variant">Note: Advanced ingredient filtering requires app integration.</p>
                </div>
                <div class="space-y-6 opacity-60">
                    <h3 class="font-headline font-bold text-lg tracking-tight text-primary">Ratings</h3>
                    <div class="space-y-3 font-label text-sm text-on-surface-variant">
                        <label class="flex items-center gap-3 cursor-not-allowed">
                            <input disabled class="form-radio text-primary border-outline-variant focus:ring-primary focus:ring-opacity-20" name="rating" type="radio"/>
                            <div class="flex text-primary">
                                <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                <span class="material-symbols-outlined text-sm text-outline-variant">star</span>
                                <span class="ml-2">& Up</span>
                            </div>
                        </label>
                    </div>
                </div>
            </aside>

            <!-- Product Grid Area -->
            <div class="flex-grow flex flex-col">
                <!-- Top Bar: Title & Sort -->
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-12 gap-4">
                    <h1 class="font-headline text-4xl font-bold tracking-tight text-primary">{{ collection.title | default: 'All Products' }}</h1>
                    <div class="flex items-center gap-3 font-label text-sm">
                        <span class="text-on-surface-variant">Sort by:</span>
                        <select class="bg-surface-container-lowest border-none shadow-sm rounded-md text-primary font-medium focus:ring-1 focus:ring-outline cursor-pointer py-2 pl-3 pr-8">
                            <option>Popularity</option>
                            <option>Price: Low to High</option>
                            <option>Price: High to Low</option>
                            <option>Newest Arrivals</option>
                        </select>
                    </div>
                </div>

                <!-- Grid Component -->
                <shopify-list-context class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-8 gap-y-16" type="product" query="{{ list_query }}" first="24">
                    <template>
                        <!-- Desktop Product Card -->
                        <div class="group flex flex-col custom-product-card">
                            <div class="relative w-full aspect-[4/5] bg-surface-container-low rounded-lg overflow-hidden mb-6">
                                <a shopify-attr--href="product.onlineStoreUrl" class="block w-full h-full mix-blend-multiply image-wrapper">
                                    <shopify-media width="500" height="600" query="product.selectedOrFirstAvailableVariant.image"></shopify-media>
                                </a>
                            </div>
                            <div class="flex-grow flex flex-col">
                                <div class="flex items-center gap-1 mb-2 text-primary">
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                </div>
                                <a shopify-attr--href="product.onlineStoreUrl">
                                    <h3 class="font-headline font-semibold text-lg leading-tight mb-1"><shopify-data query="product.title"></shopify-data></h3>
                                </a>
                                <p class="font-label text-sm text-on-surface-variant mb-4"><shopify-data query="product.vendor"></shopify-data></p>
                                <div class="mt-auto flex items-center justify-between">
                                    <span class="font-label font-semibold text-lg text-primary"><shopify-money query="product.selectedOrFirstAvailableVariant.price"></shopify-money></span>
                                </div>
                                <div class="mt-4 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                                    <button onclick="getElementById('cart').addLine(event).showModal();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" class="flex-1 bg-primary text-on-primary rounded-full py-2 font-label text-sm font-medium hover:bg-inverse-surface transition-colors cursor-pointer text-center">Shop Now</button>
                                    <button onclick="getElementById('cart').addLine(event).showModal();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" aria-label="Quick Add" class="bg-surface-container-high text-on-surface rounded-full w-10 h-10 flex items-center justify-center hover:bg-surface-dim transition-colors cursor-pointer">
                                        <span class="material-symbols-outlined text-[20px] pointer-events-none">add</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </template>
                </shopify-list-context>
            </div>
        </div>
"""

mobile_view = """
        <!-- Mobile UI -->
        <div class="flex md:hidden flex-col w-full max-w-md mx-auto pt-24 pb-28 px-4 gap-6 custom-mobile-layout">
            <!-- Editorial Header & Filter/Sort -->
            <section class="flex flex-col gap-4">
                <div>
                    <h1 class="font-headline text-3xl font-extrabold text-primary tracking-tight">{{ collection.title | default: 'All Products' }}</h1>
                    <p class="font-body text-sm text-on-surface-variant mt-1">{{ section.settings.mobile_subtitle }}</p>
                </div>
                <!-- Filter/Sort Bar -->
                <div class="flex items-center gap-2 mt-2">
                    <button class="flex-1 bg-surface-container-high text-on-surface-variant rounded-xl py-3 px-4 flex items-center justify-center gap-2 font-body text-sm font-medium hover:bg-surface-variant transition-colors">
                        <span class="material-symbols-outlined text-[18px]">tune</span>
                        Filter
                    </button>
                    <button class="flex-1 bg-surface-container-high text-on-surface-variant rounded-xl py-3 px-4 flex items-center justify-center gap-2 font-body text-sm font-medium hover:bg-surface-variant transition-colors">
                        <span class="material-symbols-outlined text-[18px]">sort</span>
                        Sort
                    </button>
                </div>
            </section>

            <!-- Grid Component -->
            <shopify-list-context class="grid grid-cols-2 gap-4 w-full" type="product" query="{{ list_query }}" first="24">
                <template>
                    <!-- Mobile Product Card -->
                    <article class="flex flex-col bg-surface-container-low rounded-xl overflow-hidden relative group custom-product-card">
                        <div class="aspect-[4/5] relative w-full bg-surface-container-highest overflow-hidden">
                            <a shopify-attr--href="product.onlineStoreUrl" class="block w-full h-full mix-blend-multiply image-wrapper">
                                <shopify-media width="300" height="400" query="product.selectedOrFirstAvailableVariant.image"></shopify-media>
                            </a>
                        </div>
                        <div class="p-3 flex flex-col flex-grow justify-between gap-2">
                            <div class="flex flex-col gap-1">
                                <div class="flex items-center gap-1 text-tertiary-container">
                                    <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="font-body text-xs text-on-surface-variant">4.9</span>
                                </div>
                                <a shopify-attr--href="product.onlineStoreUrl">
                                    <h3 class="font-body text-sm font-medium text-on-surface leading-tight line-clamp-2"><shopify-data query="product.title"></shopify-data></h3>
                                </a>
                            </div>
                            <div class="flex items-center justify-between mt-1">
                                <span class="font-headline text-base font-bold text-primary"><shopify-money query="product.selectedOrFirstAvailableVariant.price"></shopify-money></span>
                                <button onclick="getElementById('cart').addLine(event).showModal();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" aria-label="Quick Add" class="bg-primary text-on-primary rounded-full p-2 hover:bg-surface-tint transition-colors shadow-[0_4px_14px_rgba(38,71,36,0.15)] cursor-pointer z-10">
                                    <span class="material-symbols-outlined text-[18px] pointer-events-none">add</span>
                                </button>
                            </div>
                        </div>
                    </article>
                </template>
            </shopify-list-context>
            
            <div class="mt-8 flex justify-center w-full">
                <button class="w-full bg-surface-container-highest text-primary font-headline font-semibold text-sm py-4 rounded-xl hover:bg-surface-variant transition-colors flex items-center justify-center gap-2">
                    Load More Rituals
                    <span class="material-symbols-outlined text-[18px]">expand_more</span>
                </button>
            </div>
        </div>
"""

style_block = """
<style>
    /* Headless Components Reset & Image Fixes */
    .custom-product-card shopify-media {
        display: block;
        width: 100%;
        height: 100%;
    }
    
    .custom-product-card shopify-media::part(image) {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .custom-product-card shopify-media img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .image-wrapper {
        transition: transform 0.7s ease;
    }
    
    .custom-product-card:hover .image-wrapper {
        transform: scale(1.05);
    }
</style>
"""

full_content = schema + style_block + """
<div class="bg-surface text-on-surface">
    {% assign active_collection = collection.handle %}
    {% if active_collection == blank %}
        {% assign active_collection = 'all' %}
    {% endif %}

    {% assign is_global = false %}
    {% if active_collection == 'all' %}
        {% assign is_global = true %}
    {% endif %}

    {% if is_global %}
        {% assign list_query = 'products' %}
        <div class="shopify-global-products-wrapper">
    {% else %}
        {% assign list_query = 'collection.products' %}
        <shopify-context type="collection" handle="{{ active_collection }}">
            <template>
    {% endif %}
""" + desktop_view + mobile_view + """
    {% if is_global %}
        </div>
    {% else %}
            </template>
            <div shopify-loading-placeholder class="w-full min-h-[500px] flex items-center justify-center font-headline text-xl text-primary animate-pulse">Loading Collection...</div>
        </shopify-context>
    {% endif %}
</div>
"""

with open(r"f:\TQS website\tqs-topqualitystore-myshopify-com\sections\tqs-collection-template.liquid", "w", encoding="utf-8") as f:
    f.write(full_content)
