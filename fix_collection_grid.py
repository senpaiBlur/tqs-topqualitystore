import os

file_path = r"f:\TQS website\tqs-topqualitystore-myshopify-com\sections\tqs-collection-template.liquid"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Grid List Context classes
old_list_context = """        <!-- Product Grid (2-Column Mobile, 4-Column Desktop) -->
        <shopify-list-context type="product" query="{{ list_query }}" first="24">
            <template>
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-8">
                    <!-- Product Card -->
                    <article class="flex flex-col bg-surface-container-low rounded-xl overflow-hidden relative group custom-product-card shadow-[0_4px_20px_rgba(30,30,30,0.02)] hover:shadow-[0_12px_36px_rgba(30,30,30,0.06)] transition-all duration-300">"""

new_list_context = """        <!-- Product Grid (2-Column Mobile, 4-Column Desktop) -->
        <shopify-list-context class="grid grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-8" type="product" query="{{ list_query }}" first="24">
            <template>
                    <!-- Product Card -->
                    <article class="flex flex-col bg-surface-container-low rounded-xl overflow-hidden relative group custom-product-card shadow-[0_4px_20px_rgba(30,30,30,0.02)] hover:shadow-[0_12px_36px_rgba(30,30,30,0.06)] transition-all duration-300">"""
content = content.replace(old_list_context, new_list_context)

# Remove the closing div of the old grid
content = content.replace("</article>\n                </div>\n            </template>", "</article>\n            </template>")

# 2. Add SAVE Badge
old_badge = """                                <!-- Category/Vendor Badge -->
                                <div class="absolute top-2 left-2 bg-secondary-container/90 backdrop-blur-sm text-on-secondary-container font-label text-[10px] font-semibold uppercase tracking-wider px-2 py-1 rounded-full shadow-sm">
                                    <shopify-data query="product.vendor"></shopify-data>
                                </div>"""

new_badge = """                                <!-- Category/Vendor Badge -->
                                <div class="absolute top-2 left-2 flex gap-1 items-start flex-col">
                                    <div class="bg-secondary-container/90 backdrop-blur-sm text-on-secondary-container font-label text-[10px] font-semibold uppercase tracking-wider px-2 py-1 rounded-full shadow-sm">
                                        <shopify-data query="product.vendor"></shopify-data>
                                    </div>
                                    <!-- Dynamic Save Badge -->
                                    <div class="px-2 py-1 bg-[#ba1a1a] text-white font-label text-[10px] font-bold uppercase tracking-wider rounded-full shadow-sm" shopify-attr--style="product.selectedOrFirstAvailableVariant.compareAtPrice.amount > product.selectedOrFirstAvailableVariant.price.amount ? 'display:block' : 'display:none'">
                                        SAVE <shopify-text text="Math.round(((product.selectedOrFirstAvailableVariant.compareAtPrice.amount - product.selectedOrFirstAvailableVariant.price.amount) / product.selectedOrFirstAvailableVariant.compareAtPrice.amount) * 100) + '%'"></shopify-text>
                                    </div>
                                </div>"""
content = content.replace(old_badge, new_badge)

# 3. Add Buy Now Button inside card padding
old_price = """                                <div class="flex items-center justify-between mt-auto pt-2">
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
                                </div>"""

new_price = """                                <div class="flex flex-col gap-3 mt-auto pt-2">
                                    <div class="flex flex-wrap gap-x-2 gap-y-0.5 items-end">
                                        <span class="font-headline text-base md:text-lg font-bold text-primary">
                                            <shopify-money query="product.selectedOrFirstAvailableVariant.price"></shopify-money>
                                        </span>
                                        <span class="font-body text-[10px] md:text-sm text-outline line-through opacity-60 pb-0.5" shopify-attr--style="product.selectedOrFirstAvailableVariant.compareAtPrice.amount > 0 ? 'display:inline' : 'display:none'">
                                            <shopify-money query="product.selectedOrFirstAvailableVariant.compareAtPrice"></shopify-money>
                                        </span>
                                    </div>
                                    
                                    <!-- Action Buttons -->
                                    <div class="flex gap-2 w-full">
                                        <button onclick="document.querySelector('shopify-store').buyNow(event); event.preventDefault(); event.stopPropagation();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" class="flex-grow py-2 rounded-full bg-primary text-on-primary font-headline font-bold text-[10px] md:text-xs uppercase tracking-wide hover:opacity-90 flex justify-center items-center shadow-sm transition-transform active:scale-95">
                                            Buy Now
                                        </button>
                                        <button onclick="document.getElementById('cart').addLine(event).showModal(); event.preventDefault(); event.stopPropagation();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" aria-label="Add to cart" class="flex-shrink-0 w-[32px] h-[32px] md:w-[36px] md:h-[36px] bg-transparent border-2 border-primary text-primary rounded-full hover:bg-primary/5 transition-all flex justify-center items-center">
                                            <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 0;">shopping_bag</span>
                                        </button>
                                    </div>
                                </div>"""
content = content.replace(old_price, new_price)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
