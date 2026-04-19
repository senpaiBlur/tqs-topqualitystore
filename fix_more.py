import os

file_path = r"f:\TQS website\tqs-topqualitystore-myshopify-com\sections\tqs-more-products.liquid"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Grid
content = content.replace(
    '<div class="flex overflow-x-auto gap-6 px-6 md:px-12 pb-12 snap-x snap-mandatory gallery-scroll w-full max-w-7xl mx-auto">',
    '<div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6 px-6 md:px-12 pb-12 w-full max-w-7xl mx-auto">'
)

# 2. Update Card Class
content = content.replace(
    '<div class="group min-w-[280px] w-[280px] md:min-w-[320px] md:w-[320px] bg-surface-container-lowest rounded-3xl overflow-hidden flex flex-col snap-center ghost-border shadow-[0_10px_30px_rgba(26,28,28,0.03)] hover:shadow-[0_20px_40px_rgba(26,28,28,0.06)] transition-all duration-300 transform hover:-translate-y-1 relative">',
    '<div class="group w-full bg-surface-container-lowest rounded-xl md:rounded-3xl overflow-hidden flex flex-col ghost-border shadow-[0_10px_30px_rgba(26,28,28,0.03)] hover:shadow-[0_20px_40px_rgba(26,28,28,0.06)] transition-all duration-300 transform md:hover:-translate-y-1 relative">'
)

# 3. Update Image Height
content = content.replace(
    '<div class="w-full h-[320px] bg-surface-container-low relative overflow-hidden">',
    '<div class="w-full aspect-[4/5] bg-surface-container-low relative overflow-hidden">'
)

# 4. Update Header Paddings
content = content.replace(
    '<div class="p-6 bg-surface-container-lowest">',
    '<div class="p-4 md:p-6 bg-surface-container-lowest flex-grow flex flex-col justify-end">'
)

content = content.replace(
    '<h4 class="font-headline text-xl font-bold text-primary tracking-tight mb-2 truncate">',
    '<h4 class="font-headline text-base md:text-xl font-bold text-primary tracking-tight mb-2 truncate">'
)

# 5. Add MRP inside price container
old_price = """                        <div class="flex justify-between items-end">
                            <span class="font-body text-sm font-semibold tracking-widest text-secondary uppercase"><shopify-data query="product.vendor"></shopify-data></span>
                            <span class="font-headline text-lg font-bold text-primary">
                                <shopify-money query="product.selectedOrFirstAvailableVariant.price"></shopify-money>
                            </span>
                        </div>"""

new_price = """                        <div class="flex flex-col justify-between items-start gap-1">
                            <span class="font-body text-[10px] md:text-xs font-semibold tracking-widest text-secondary uppercase"><shopify-data query="product.vendor"></shopify-data></span>
                            <div class="flex items-center gap-2 flex-wrap">
                                <span class="font-headline text-base md:text-lg font-bold text-primary">
                                    <shopify-money query="product.selectedOrFirstAvailableVariant.price"></shopify-money>
                                </span>
                                <span class="font-body text-[10px] md:text-sm text-outline line-through opacity-60" shopify-attr--style="product.selectedOrFirstAvailableVariant.compareAtPrice.amount > 0 ? 'display:inline' : 'display:none'">
                                    <shopify-money query="product.selectedOrFirstAvailableVariant.compareAtPrice"></shopify-money>
                                </span>
                            </div>
                        </div>"""

content = content.replace(old_price, new_price)

# 6. Update action buttons sizing
old_buttons = """                    <!-- Explicit Action Buttons -->
                    <div class="px-6 pb-6 pt-2 bg-surface-container-lowest flex gap-3 w-full">
                        <button onclick="document.querySelector('shopify-store').buyNow(event); event.stopPropagation();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" class="flex-grow py-3 rounded-full bg-primary text-on-primary font-headline font-bold text-xs uppercase tracking-wide hover:opacity-90 flex justify-center items-center shadow-md transition-transform active:scale-95">
                            Buy Now
                        </button>
                        <button onclick="document.getElementById('cart').addLine(event).showModal(); event.stopPropagation();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" aria-label="Add to cart" class="flex-shrink-0 w-[44px] h-[44px] bg-transparent border-2 border-primary text-primary rounded-full hover:bg-primary/5 transition-all flex justify-center items-center">
                            <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 0;">shopping_bag</span>
                        </button>
                    </div>"""

new_buttons = """                    <!-- Explicit Action Buttons -->
                    <div class="px-4 md:px-6 pb-4 md:pb-6 pt-2 bg-surface-container-lowest flex gap-2 md:gap-3 w-full">
                        <button onclick="document.querySelector('shopify-store').buyNow(event); event.stopPropagation();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" class="flex-grow py-2.5 md:py-3 rounded-full bg-primary text-on-primary font-headline font-bold text-[10px] md:text-xs uppercase tracking-wide hover:opacity-90 flex justify-center items-center shadow-md transition-transform active:scale-95">
                            Buy Now
                        </button>
                        <button onclick="document.getElementById('cart').addLine(event).showModal(); event.stopPropagation();" shopify-attr--disabled="!product.selectedOrFirstAvailableVariant.availableForSale" aria-label="Add to cart" class="flex-shrink-0 w-[36px] h-[36px] md:w-[44px] md:h-[44px] bg-transparent border-2 border-primary text-primary rounded-full hover:bg-primary/5 transition-all flex justify-center items-center">
                            <span class="material-symbols-outlined text-[16px] md:text-[18px]" style="font-variation-settings: 'FILL' 0;">shopping_bag</span>
                        </button>
                    </div>"""

content = content.replace(old_buttons, new_buttons)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
