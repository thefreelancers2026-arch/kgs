import re

def update_calls():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Hero CTA
    hero_target = r'<a href="tel:\+919789182921" class="btn-outline[^>]*>\s*<span class="material-symbols-outlined[^>]*>call</span> Call Now\s*</a>'
    hero_repl = """<a href="#showroom" class="btn-outline inline-flex items-center justify-center gap-2 border border-gold-500/30 text-gold-400 px-7 py-3.5 lg:px-9 text-[11px] tracking-[0.2em] uppercase w-full sm:w-auto min-h-[48px] font-medium">
                        <span class="material-symbols-outlined text-sm">storefront</span> Visit Showroom
                    </a>"""
    html = re.sub(hero_target, hero_repl, html)

    # 2. Update Bottom Collection CTA
    bottom_target = r'<p class="text-sand-200/20 text-\[10px\] tracking-\[0.2em\][^>]*>Available at our Virudhachalam showroom</p>\s*<a href="tel:\+919789182921" class="btn-primary[^>]*>\s*<span class="material-symbols-outlined[^>]*>call</span> Call Now to Check Availability\s*</a>'
    bottom_repl = """<p class="text-sand-200/20 text-[10px] tracking-[0.2em] uppercase mb-8 font-sans">100% Secure Checkout &middot; Express Delivery</p>
                    <button onclick="document.getElementById('fabCart').click()" class="btn-primary inline-flex items-center justify-center gap-2.5 bg-gold-500 text-onyx-900 px-8 md:px-10 py-4 text-[11px] font-semibold tracking-[0.2em] uppercase min-h-[52px] w-full sm:w-auto max-w-sm mx-auto">
                        <span class="material-symbols-outlined text-sm">shopping_cart_checkout</span> View Your Cart
                    </button>"""
    html = re.sub(bottom_target, bottom_repl, html)

    # 3. Mobile Menu Call Button (Optional: change to WhatsApp or Keep as Support)
    mob_menu_target = r'<a href="tel:\+919789182921" class="mt-2 inline-flex items-center justify-center gap-2 bg-gold-500[^>]*>\s*<span class="material-symbols-outlined[^>]*>call</span> Call Now\s*</a>'
    mob_menu_repl = """<a href="https://wa.me/919789182921" class="mt-2 inline-flex items-center justify-center gap-2 bg-gold-500 text-onyx-900 px-6 py-3 text-xs tracking-widest uppercase font-semibold min-h-[44px]">
                    <span class="material-symbols-outlined text-sm">forum</span> Chat Support
                </a>"""
    html = re.sub(mob_menu_target, mob_menu_repl, html)

    # 4. Remove Call FAB, just keep Whatsapp, Cart, Wishlist
    # Note: earlier we put them in fabContactGroup.
    # We will remove the Call FAB entirely.
    call_fab_target = r'<a href="tel:\+919789182921" class="fab-btn fab-call" aria-label="Call Us">\s*<span class="material-symbols-outlined text-sand-200 text-\[20px\]">call</span>\s*</a>'
    html = re.sub(call_fab_target, '', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_calls()
