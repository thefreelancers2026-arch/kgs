import re

def update_fabs():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    target_regex = r'<div class="fixed bottom-5 right-4[^>]*id="fabContainer">.*?</div>\s*<!-- ═══════════════════════════════════════\s*SCRIPTS'
    
    replacement = """<div class="fixed bottom-5 right-4 sm:bottom-8 sm:right-6 md:right-10 z-50 flex flex-col items-end gap-[10px] sm:gap-3" id="fabContainer">
        <!-- eCommerce Group -->
        <div class="flex items-center gap-[10px] sm:gap-3 flex-row sm:flex-col" id="fabEcommerceGroup">
            <button class="fab-btn hidden" id="fabCart" aria-label="Open Cart" style="background: rgba(26,26,26,0.9); border: 1px solid rgba(212,175,55,0.2);">
                <span class="material-symbols-outlined text-gold-500/90 text-[18px]">shopping_cart</span>
                <span class="wish-badge hidden" id="fabCartBadge" style="background: #D4AF37; color: #0A0A0A;">0</span>
            </button>
            <button class="fab-btn fab-wishlist hidden" id="fabWishlist" aria-label="Open Wishlist">
                <span class="material-symbols-outlined text-gold-500/70 text-[18px]" style="font-variation-settings: 'FILL' 1;">favorite</span>
                <span class="wish-badge hidden" id="fabWishBadge">0</span>
            </button>
        </div>
        <!-- Contact Group -->
        <div class="flex items-center gap-[10px] sm:gap-3 flex-row sm:flex-col" id="fabContactGroup">
            <a href="tel:+919789182921" class="fab-btn fab-call" aria-label="Call Us">
                <span class="material-symbols-outlined text-sand-200 text-[20px]">call</span>
            </a>
            <a href="https://wa.me/919789182921" target="_blank" class="fab-btn fab-whatsapp" aria-label="WhatsApp">
                <svg class="w-[20px] h-[20px] fill-current text-onyx-900" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51h-.57c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            </a>
        </div>
    </div>

    <!-- ═══════════════════════════════════════
         SCRIPTS"""

    new_html = re.sub(target_regex, replacement, html, flags=re.DOTALL)
    
    if html == new_html:
        print("Error: No regex match found!")
    else:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Success: Appended 2x2 grid FAB to DOM")

if __name__ == '__main__':
    update_fabs()
