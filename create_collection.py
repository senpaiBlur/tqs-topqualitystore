import os

new_collection_liquid = """
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
    /* Hide shopify internal variant selectors */
    shopify-variant-selector { display: none !important; }
</style>

<div class="bg-surface text-on-surface w-full flex justify-center pb-20 pt-16">
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
        <div class="w-full max-w-md lg:max-w-6xl mx-auto px-4 lg:px-8">
    {% else %}
        {% assign list_query = 'collection.products' %}
        <shopify-context type="collection" handle="{{ active_collection }}">
            <template>
            <div class="w-full max-w-md lg:max-w-6xl mx-auto px-4 lg:px-8">
    {% endif %}

        <!-- Editorial Header & Filter/Sort -->
        <section class="flex flex-col gap-4 mb-8">
            <div>
                <h1 class="font-headline text-3xl md:text-5xl font-extrabold text-primary tracking-tight">
                    {% if collection.title %}{{ collection.title }}{% else %}The Apothecary{% endif %}
                </h1>
                <p class="font-body text-sm md:text-base text-on-surface-variant mt-1">{{ section.settings.mobile_subtitle }}</p>
            </div>
            
            <!-- Filter/Sort Bar -->
            <div class="flex items-center gap-2 mt-2 max-w-md">
                <button class="flex-1 bg-surface-container-high text-on-surface-variant rounded-xl py-3 px-4 flex items-center justify-center gap-2 font-body text-sm font-medium hover:bg-surface-variant transition-colors">
                    <span class="material-symbols-outlined text-[18px]">tune</span>
                    Filter
                </button>
                <div class="w-px h-6 bg-outline-variant/30 hidden"></div> <!-- divider -->
                <button class="flex-1 bg-surface-container-high text-on-surface-variant rounded-xl py-3 px-4 flex items-center justify-center gap-2 font-body text-sm font-medium hover:bg-surface-variant transition-colors">
                    <span class="material-symbols-outlined text-[18px]">sort</span>
                    Sort
                </button>
            </div>
        </section>

        <!-- Product Grid (2-Column Mobile, 4-Column Desktop) -->
        <shopify-list-context type="product" query="{{ list_query }}" first="24">
            <template>
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-8">
                    <!-- Product Card -->
                    <article class="flex flex-col bg-surface-container-low rounded-xl overflow-hidden relative group custom-product-card shadow-[0_4px_20px_rgba(30,30,30,0.02)] hover:shadow-[0_12px_36px_rgba(30,30,30,0.06)] transition-all duration-300">
                        <a shopify-attr--href="product.onlineStoreUrl" class="block flex-grow group-link">
                            <!-- Image Container -->
                            <div class="aspect-[4/5] relative w-full bg-surface-container-highest overflow-hidden">
                                <div class="image-wrapper w-full h-full">
                                    <shopify-media query="product.selectedOrFirstAvailableVariant.image"></shopify-media>
                                </div>
                                
                                <!-- Category/Vendor Badge -->
                                <div class="absolute top-2 left-2 bg-secondary-container/90 backdrop-blur-sm text-on-secondary-container font-label text-[10px] font-semibold uppercase tracking-wider px-2 py-1 rounded-full shadow-sm">
                                    <shopify-data query="product.vendor"></shopify-data>
                                </div>
                            </div>
                            
                            <!-- Content -->
                            <div class="p-3 flex flex-col justify-between gap-2 h-full bg-surface-container-lowest">
                                <div class="flex flex-col gap-1">
                                    <!-- Rating Mock -->
                                    <div class="flex items-center gap-1 text-tertiary-container">
                                        <span class="material-symbols-outlined text-[14px] text-primary" style="font-variation-settings: 'FILL' 1;">star</span>
                                        <span class="material-symbols-outlined text-[14px] text-primary" style="font-variation-settings: 'FILL' 1;">star</span>
                                        <span class="material-symbols-outlined text-[14px] text-primary" style="font-variation-settings: 'FILL' 1;">star</span>
                                        <span class="material-symbols-outlined text-[14px] text-primary" style="font-variation-settings: 'FILL' 1;">star</span>
                                        <span class="material-symbols-outlined text-[14px] text-primary" style="font-variation-settings: 'FILL' 1;">star</span>
                                    </div>
                                    <h3 class="font-body text-sm md:text-base font-medium text-on-surface leading-tight line-clamp-2 mt-1">
                                        <shopify-data query="product.title"></shopify-data>
                                    </h3>
                                </div>
                                <div class="flex items-center justify-between mt-auto pt-2">
                                    <div class="flex flex-col gap-0.5">
                                        <span class="font-headline text-base font-bold text-primary">
                                            <shopify-money query="product.selectedOrFirstAvailableVariant.price"></shopify-money>
                                        </span>
                                        <span class="font-body text-[10px] text-outline line-through opacity-60" shopify-attr--style="product.selectedOrFirstAvailableVariant.compareAtPrice.amount > 0 ? 'display:block' : 'display:none'">
                                            <shopify-money query="product.selectedOrFirstAvailableVariant.compareAtPrice"></shopify-money>
                                        </span>
                                    </div>
                                    <!-- Keep Add button outside anchor wrapper or use stopPropagation to avoid navigating when adding to cart -->
                                    <button onclick="document.getElementById('cart').addLine(event).showModal(); event.preventDefault(); event.stopPropagation();" aria-label="Quick Add" class="bg-primary text-on-primary rounded-full p-2.5 hover:bg-surface-tint transition-colors shadow-[0_4px_14px_rgba(0,0,0,0.15)] flex-shrink-0 active:scale-90">
                                        <span class="material-symbols-outlined text-[18px]">add</span>
                                    </button>
                                </div>
                            </div>
                        </a>
                    </article>
                </div>
            </template>
            <!-- Loading Indicator -->
            <div shopify-loading-placeholder class="w-full text-center py-32 text-primary opacity-60">
                <span class="material-symbols-outlined animate-spin mb-4 text-3xl">refresh</span><br/>
                Loading Collection...
            </div>
        </shopify-list-context>

        <!-- Load More Button -->
        <div class="mt-8 flex justify-center w-full">
            <button class="w-full md:w-auto bg-surface-container-highest text-primary font-headline font-semibold text-sm py-4 px-12 rounded-xl hover:bg-surface-variant transition-colors flex items-center justify-center gap-2 active:scale-95">
                Load More Rituals
                <span class="material-symbols-outlined text-[18px]">expand_more</span>
            </button>
        </div>

    {% if is_global %}
        </div>
    {% else %}
            </div>
            </template>
        </shopify-context>
    {% endif %}
</div>
"""

with open(r"f:\TQS website\tqs-topqualitystore-myshopify-com\sections\tqs-collection-template.liquid", "w", encoding="utf-8") as f:
    f.write(new_collection_liquid)
