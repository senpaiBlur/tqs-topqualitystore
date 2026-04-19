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
                    <div class="space-y-4 font-label text-sm text-on-surface-variant">
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <input checked class="form-checkbox text-primary border-outline-variant rounded-sm focus:ring-primary focus:ring-opacity-20" type="checkbox"/>
                            <span class="group-hover:text-primary transition-colors">All Skincare</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <input class="form-checkbox text-primary border-outline-variant rounded-sm focus:ring-primary focus:ring-opacity-20" type="checkbox"/>
                            <span class="group-hover:text-primary transition-colors">Cleansers</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <input class="form-checkbox text-primary border-outline-variant rounded-sm focus:ring-primary focus:ring-opacity-20" type="checkbox"/>
                            <span class="group-hover:text-primary transition-colors">Serums & Oils</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group">
                            <input class="form-checkbox text-primary border-outline-variant rounded-sm focus:ring-primary focus:ring-opacity-20" type="checkbox"/>
                            <span class="group-hover:text-primary transition-colors">Moisturizers</span>
                        </label>
                    </div>
                </div>
                <div class="space-y-6">
                    <h3 class="font-headline font-bold text-lg tracking-tight text-primary">Key Ingredients</h3>
                    <div class="flex flex-wrap gap-2">
                        <button class="bg-secondary-container text-on-surface px-3 py-1.5 rounded-full font-label text-xs hover:bg-surface-dim transition-colors">Saffron</button>
                        <button class="bg-secondary-container text-on-surface px-3 py-1.5 rounded-full font-label text-xs hover:bg-surface-dim transition-colors">Turmeric</button>
                        <button class="bg-surface-container text-on-surface-variant px-3 py-1.5 rounded-full font-label text-xs hover:bg-surface-dim transition-colors">Neem</button>
                    </div>
                </div>
                <div class="space-y-6">
                    <h3 class="font-headline font-bold text-lg tracking-tight text-primary">Ratings</h3>
                    <div class="space-y-3 font-label text-sm text-on-surface-variant">
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input class="form-radio text-primary border-outline-variant focus:ring-primary focus:ring-opacity-20" name="rating" type="radio"/>
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
                <shopify-list-context class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-8 gap-y-16" type="product" query="collection.products" first="24">
                    <template>
                        <!-- Desktop Product Card -->
                        <div class="group flex flex-col">
                            <div class="relative w-full aspect-[4/5] bg-surface-container-low rounded-lg overflow-hidden mb-6">
                                <a shopify-attr--href="product.onlineStoreUrl" class="block w-full h-full mix-blend-multiply">
                                    <shopify-media width="500" height="600" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" query="product.selectedOrFirstAvailableVariant.image"></shopify-media>
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
                                    <button onclick="getElementById('cart').addLine(event).showModal();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" class="flex-1 bg-primary text-on-primary rounded-full py-2 font-label text-sm font-medium hover:bg-inverse-surface transition-colors cursor-pointer">Shop Now</button>
                                    <button onclick="getElementById('cart').addLine(event).showModal();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" aria-label="Quick Add" class="bg-surface-container-high text-on-surface rounded-full w-10 h-10 flex items-center justify-center hover:bg-surface-dim transition-colors cursor-pointer">
                                        <span class="material-symbols-outlined text-[20px]">add</span>
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
        <div class="flex md:hidden flex-col w-full max-w-md mx-auto pt-24 pb-28 px-4 gap-6">
            <!-- Editorial Header & Filter/Sort -->
            <section class="flex flex-col gap-4">
                <div>
                    <h1 class="font-headline text-3xl font-extrabold text-primary tracking-tight">{{ collection.title | default: 'The Apothecary' }}</h1>
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
            <shopify-list-context class="grid grid-cols-2 gap-4" type="product" query="collection.products" first="24">
                <template>
                    <!-- Mobile Product Card -->
                    <article class="flex flex-col bg-surface-container-low rounded-xl overflow-hidden relative group">
                        <div class="aspect-[4/5] relative w-full bg-surface-container-highest overflow-hidden">
                            <a shopify-attr--href="product.onlineStoreUrl" class="block w-full h-full mix-blend-multiply">
                                <shopify-media width="300" height="400" class="w-full h-full object-cover mix-blend-multiply" query="product.selectedOrFirstAvailableVariant.image"></shopify-media>
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
                                    <span class="material-symbols-outlined text-[18px]">add</span>
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

full_content = schema + """
<div class="bg-surface text-on-surface">
    {% assign active_collection = collection.handle | default: 'all' %}
    <shopify-context type="collection" handle="{{ active_collection }}">
""" + desktop_view + mobile_view + """
    </shopify-context>
</div>
"""

with open(r"f:\TQS website\tqs-topqualitystore-myshopify-com\sections\tqs-collection-template.liquid", "w", encoding="utf-8") as f:
    f.write(full_content)
