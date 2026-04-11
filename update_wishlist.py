import re

def update_wishlist():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Wishlist Modal HTML using regex between `id="wishlistItems"` closing div and `CART MODAL` comment.
    wish_html_regex = r'(<div id="wishlistItems"[^>]*>.*?</div>)(\s*)<div class="px-5 pb-2">.*?<div class="border-t pt-5 space-y-4".*?<!-- ═══════════════════════════════════════\s*CART MODAL'
    
    wish_checkout_html = r"""\1\2<div class="px-5 pb-2">
                <div class="border-t pt-4 flex justify-between items-center" style="border-color: rgba(212,175,55,0.06);">
                    <p class="text-sand-200/50 text-xs tracking-[0.1em] uppercase font-sans font-medium">Subtotal</p>
                    <p class="text-gold-500 text-lg font-medium" id="wishTotal">₹0</p>
                </div>
            </div>
            <div class="p-5 pt-4">
                <button onclick="alert('Proceeding to Shopify Checkout... (Coming Soon in Main Build, Client can test this UI design)')" class="btn-primary w-full bg-gold-400 hover:bg-gold-500 text-onyx-900 py-4 rounded-lg text-[11px] uppercase tracking-[0.2em] font-bold flex justify-center items-center gap-2.5 min-h-[52px]">
                    <span class="material-symbols-outlined text-[18px]">lock</span> Secure Checkout
                </button>
            </div>
        </div>
    </div>

    <!-- ═══════════════════════════════════════
         CART MODAL"""

    html = re.sub(wish_html_regex, wish_checkout_html, html, flags=re.DOTALL)

    # 2. Update JS: Remove `wishUserName`, `wishUserPhone`, `sendWishlistWhatsApp` const declarations.
    html = re.sub(r'const\s+sendWishlistWhatsApp\s*=\s*document\.getElementById\("sendWishlistWhatsApp"\);\s*', '', html)
    html = re.sub(r'const\s+wishUserName\s*=\s*document\.getElementById\("wishUserName"\);\s*', '', html)
    html = re.sub(r'const\s+wishUserPhone\s*=\s*document\.getElementById\("wishUserPhone"\);\s*', '', html)

    # 3. Update JS: Remove the `sendWishlistWhatsApp.addEventListener` block
    wa_target = r'\s*sendWishlistWhatsApp\.addEventListener\("click", \(\) => \{.*?window\.open\(.*?\);\s*\}\);'
    html = re.sub(wa_target, '', html, flags=re.DOTALL)

    # 4. Update JS: renderWishlistItems dynamic price logic
    # Currently it just does: item.innerHTML = `<img> <span>${name}</span> <button>...`;
    # Replace the inner `wishlist.forEach` entirely to include price calculation.

    render_wishlist_regex = r'(wishlist\.forEach\(name => \{.*?wishlistItems\.appendChild\(item\);\s*\}\);)'
    
    new_loop = """let total = 0;
            wishlist.forEach(name => {
                const prod = DEMO_PRODUCTS.find(p => p.name === name);
                let priceStr = "";
                if (prod && prod.price) {
                    const priceNum = parseInt(prod.price.replace(/[^0-9]/g, ''));
                    total += priceNum;
                    priceStr = `<p class="text-gold-500/80 text-[11px] tracking-wider mt-1">${prod.price}</p>`;
                }

                const item = document.createElement("div");
                item.className = "wish-item flex items-center gap-4 bg-onyx-700/20 border border-onyx-600/30 rounded-lg p-3";
                const imgSrc = prod ? prod.img : (productImages[name] || "");
                item.innerHTML = `
                    ${imgSrc ? `<img src="${imgSrc}" class="w-12 h-12 rounded object-cover flex-shrink-0 opacity-80" alt="${name}">` : ''}
                    <div class="flex-1">
                        <h4 class="text-white/90 text-xs font-medium">${name}</h4>
                        ${priceStr}
                    </div>
                    <button class="wish-remove text-sand-200/20 hover:text-red-400 transition-colors duration-400 min-h-[36px] min-w-[36px] flex items-center justify-center rounded-full hover:bg-onyx-700/40" data-name="${name}">
                        <span class="material-symbols-outlined text-sm">close</span>
                    </button>
                `;
                wishlistItems.appendChild(item);
            });
            
            const wishTotalEl = document.getElementById("wishTotal");
            if(wishTotalEl) {
                wishTotalEl.innerText = "₹" + total.toLocaleString('en-IN');
            }"""

    html = re.sub(render_wishlist_regex, new_loop, html, flags=re.DOTALL)

    # 5. Fix empty Wishlist total reset
    empty_wish_regex = r'if \(wishlist\.length === 0\) \{ emptyWishMsg\.classList\.remove\("hidden"\); return; \}'
    empty_wish_replacement = r'if (wishlist.length === 0) { emptyWishMsg.classList.remove("hidden"); const wTotal = document.getElementById("wishTotal"); if(wTotal) wTotal.innerText = "₹0"; return; }'
    html = re.sub(empty_wish_regex, empty_wish_replacement, html)


    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_wishlist()
    print("Wishlist updated to Checkout mode")
