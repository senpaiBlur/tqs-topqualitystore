import os

file_path = r"f:\TQS website\tqs-topqualitystore-myshopify-com\layout\theme.liquid"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the CSS for the shopify-cart::part(dialog)
old_css = """    /* Cart Customizations Based on Instructions */
    shopify-cart::part(dialog) {
      border-radius: 0.5rem;
    }"""

new_css = """    /* Cart Customizations Based on Instructions */
    shopify-cart::part(dialog) {
      margin: 0;
      margin-top: auto;
      width: 100vw;
      max-width: 100vw;
      height: 90vh;
      max-height: 90vh;
      border-radius: 1.5rem 1.5rem 0 0;
      animation: slideUpCart 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 -10px 40px rgba(0,0,0,0.1);
    }
    
    @keyframes slideUpCart {
       from { transform: translateY(100%); }
       to { transform: translateY(0); }
    }"""

content = content.replace(old_css, new_css)

# 2. Inject the Drawer HTML before </body>
drawer_html_and_js = """
    <!-- Drag to Checkout Bottom Handle -->
    <div id="checkout-drawer-handle" class="fixed bottom-0 left-0 w-full z-[45] bg-surface-container-lowest rounded-t-3xl shadow-[0_-4px_30px_rgba(0,0,0,0.08)] cursor-grab touch-none flex flex-col items-center pb-safe transform transition-transform duration-300">
        <div class="w-12 h-1.5 bg-outline-variant/40 rounded-full mt-3 mb-2"></div>
        <div class="flex justify-between items-center w-full px-6 pb-4 pt-1">
            <div class="font-headline font-bold text-primary flex items-center gap-2">
                <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">shopping_bag</span>
                <span class="text-sm tracking-tight">Checkout View</span>
            </div>
            <span class="text-[10px] font-label font-bold uppercase tracking-widest text-primary bg-primary/5 px-3 py-1.5 rounded-full flex gap-1 items-center">
               Swipe Up <span class="material-symbols-outlined text-[14px]">expand_less</span>
            </span>
        </div>
    </div>

    <script>
      document.addEventListener("DOMContentLoaded", () => {
          const handle = document.getElementById('checkout-drawer-handle');
          let startY = 0;
          let currentY = 0;
          let isDragging = false;
          
          const handleDragStart = (clientY) => {
              isDragging = true;
              startY = clientY;
              handle.style.transition = 'none';
              handle.style.cursor = 'grabbing';
          };
          
          const handleDragMove = (clientY) => {
              if (!isDragging) return;
              currentY = clientY;
              const diff = currentY - startY;
              
              // Only allow dragging up
              if (diff < 0) {
                  handle.style.transform = `translateY(${diff}px)`;
                  // Trigger open if pulled up 50px
                  if (diff < -50) {
                      isDragging = false;
                      handle.style.transform = 'translateY(0)';
                      handle.style.transition = 'transform 0.3s';
                      document.getElementById('cart').showModal();
                  }
              }
          };
          
          const handleDragEnd = () => {
              if (!isDragging) return;
              isDragging = false;
              handle.style.cursor = 'grab';
              handle.style.transition = 'transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
              handle.style.transform = 'translateY(0)';
          };

          // Mouse Events
          handle.addEventListener('mousedown', (e) => handleDragStart(e.clientY));
          document.addEventListener('mousemove', (e) => handleDragMove(e.clientY));
          document.addEventListener('mouseup', handleDragEnd);

          // Touch Events
          handle.addEventListener('touchstart', (e) => handleDragStart(e.touches[0].clientY), {passive: true});
          document.addEventListener('touchmove', (e) => handleDragMove(e.touches[0].clientY), {passive: false});
          document.addEventListener('touchend', handleDragEnd);

          // Tap to open fallback
          handle.addEventListener('click', () => {
              document.getElementById('cart').showModal();
          });
      });
    </script>
</body>"""

content = content.replace("</body>", drawer_html_and_js)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
