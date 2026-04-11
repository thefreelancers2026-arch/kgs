import re

def add_cart_functionality():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Product Card JSX Injection
    card_regex = r"(const isWish = wishlist\.includes\(prod\.name\) \? 'wish-active' : '';)\s+(const html = `)(.*?)(\$\{tagHtml\})"
    
    def card_replacer(match):
        pre = match.group(1) + "\n                const inCart = cart.includes(prod.name) ? 'cart-active' : '';\n                "
        start = match.group(2)
        inner = match.group(3)
        tag = match.group(4)
        
        cart_btn = """
                        <button class="cart-btn ${inCart} absolute top-[64px] left-4 z-20 p-2.5 transition-all duration-500 group/cart flex items-center justify-center rounded-full hover:bg-onyx-900/50 min-h-[44px] min-w-[44px]" aria-label="Add to Cart" data-product="${prod.name}" data-price="${prod.price}">
                            <span class="material-symbols-outlined text-white/40 group-hover/cart:text-gold-500 text-[22px] transition-all duration-500 cart-icon">${inCart ? 'check' : 'shopping_cart'}</span>
                        </button>"""
        return pre + start + inner + cart_btn + "\n                        " + tag

    html = re.sub(card_regex, card_replacer, html, flags=re.DOTALL)

    # 2. Append Cart logic directly after attachWishlistListeners is called in renderProducts
    render_regex = r"(// Re-attach wishlist listeners for the newly injected buttons\s*attachWishlistListeners\(\);\s*)"
    html = re.sub(render_regex, r"\1attachCartListeners();\n        ", html)


    # 3. Add Cart Javascript system next to Wishlist system
    wishlist_vars_regex = r"(const wishUserName = document.getElementById\(\"wishUserName\"\);\s*const wishUserPhone = document.getElementById\(\"wishUserPhone\"\);\s*)"
    cart_vars = """
        // ── CART SYSTEM ──
        const cart = JSON.parse(localStorage.getItem("kgs_cart") || "[]");
        const fabCart = document.getElementById("fabCart");
        const fabCartBadge = document.getElementById("fabCartBadge");
        const cartModal = document.getElementById("cartModal");
        const closeCartModal = document.getElementById("closeCartModal");
        const cartItemsWrapper = document.getElementById("cartItems");
        const emptyCartMsg = document.getElementById("emptyCartMsg");
        const cartTotalEl = document.getElementById("cartTotal");
"""
    html = re.sub(wishlist_vars_regex, r"\1" + cart_vars, html)

    # 4. Add attachCartListeners and updateCartUI next to updateWishlistUI
    wishlist_func_regex = r"(function renderWishlistItems\(\) \{.*?wishlistItems\.appendChild\(item\);\s*\}\);\s*wishlistItems\.querySelectorAll\(\"\.wish-remove\"\)\.forEach\(btn => \{.*?\}\);\s*\})"
    
    cart_funcs = """

        function attachCartListeners() {
            document.querySelectorAll(".cart-btn").forEach(btn => {
                const productName = btn.getAttribute("data-product") || "";
                
                btn.addEventListener("click", (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const idx = cart.indexOf(productName);
                    const icon = btn.querySelector('.cart-icon');
                    
                    if (idx === -1) {
                        cart.push(productName);
                        btn.classList.add("cart-active");
                        // Micro-animation
                        icon.style.transform = "scale(0.8)";
                        setTimeout(() => {
                            icon.innerText = "check";
                            icon.style.transform = "scale(1.1)";
                            icon.classList.add("text-gold-500");
                            icon.classList.remove("text-white/40");
                            setTimeout(() => icon.style.transform = "scale(1)", 150);
                        }, 150);
                    } else {
                        cart.splice(idx, 1);
                        btn.classList.remove("cart-active");
                        icon.style.transform = "scale(0.8)";
                        setTimeout(() => {
                            icon.innerText = "shopping_cart";
                            icon.style.transform = "scale(1.1)";
                            icon.classList.remove("text-gold-500");
                            icon.classList.add("text-white/40");
                            setTimeout(() => icon.style.transform = "scale(1)", 150);
                        }, 150);
                    }
                    localStorage.setItem("kgs_cart", JSON.stringify(cart));
                    updateCartUI();
                });
            });
        }

        function updateCartUI() {
            const count = cart.length;
            if (count > 0) {
                fabCart.classList.remove("hidden");
                fabCartBadge.classList.remove("hidden");
                fabCartBadge.innerText = count;
                fabCartBadge.style.transform = "scale(1.3)";
                setTimeout(() => fabCartBadge.style.transform = "scale(1)", 250);
            } else {
                fabCart.classList.add("hidden");
                fabCartBadge.classList.add("hidden");
            }
            renderCartItems();
        }

        function renderCartItems() {
            if (!cartItemsWrapper) return;
            cartItemsWrapper.querySelectorAll(".cart-item").forEach(el => el.remove());
            
            if (cart.length === 0) { 
                emptyCartMsg.classList.remove("hidden"); 
                if(cartTotalEl) cartTotalEl.innerText = "₹0";
                return; 
            }
            emptyCartMsg.classList.add("hidden");

            let total = 0;
            cart.forEach(name => {
                const prod = DEMO_PRODUCTS.find(p => p.name === name);
                if (!prod) return;
                
                const priceNum = parseInt(prod.price.replace(/[^0-9]/g, ''));
                total += priceNum;

                const item = document.createElement("div");
                item.className = "cart-item flex items-center gap-4 bg-onyx-700/20 border border-onyx-600/30 rounded-lg p-3";
                item.innerHTML = `
                    <img src="${prod.img}" class="w-12 h-12 rounded object-cover flex-shrink-0 opacity-80" alt="${name}">
                    <div class="flex-1">
                        <h4 class="text-white/90 text-xs font-medium">${name}</h4>
                        <p class="text-gold-500/80 text-[11px] tracking-wider mt-1">${prod.price}</p>
                    </div>
                    <button class="cart-remove text-sand-200/20 hover:text-red-400 transition-colors duration-400 min-h-[36px] min-w-[36px] flex items-center justify-center rounded-full hover:bg-onyx-700/40" data-name="${name}">
                        <span class="material-symbols-outlined text-sm">close</span>
                    </button>
                `;
                cartItemsWrapper.appendChild(item);
            });

            if(cartTotalEl) {
                cartTotalEl.innerText = "₹" + total.toLocaleString('en-IN');
            }

            cartItemsWrapper.querySelectorAll(".cart-remove").forEach(btn => {
                btn.addEventListener("click", () => {
                    const name = btn.getAttribute("data-name");
                    const idx = cart.indexOf(name);
                    if (idx !== -1) cart.splice(idx, 1);
                    localStorage.setItem("kgs_cart", JSON.stringify(cart));
                    
                    document.querySelectorAll('.cart-btn').forEach(hb => {
                        if (hb.getAttribute("data-product") === name) {
                            hb.classList.remove("cart-active");
                            const icon = hb.querySelector('.cart-icon');
                            if(icon) {
                                icon.innerText = "shopping_cart";
                                icon.classList.remove("text-gold-500");
                                icon.classList.add("text-white/40");
                            }
                        }
                    });
                    updateCartUI();
                });
            });
        }
"""
    html = re.sub(wishlist_func_regex, r"\1" + cart_funcs, html, flags=re.DOTALL)


    # 5. Add Cart FAB
    fab_regex = r"(<button class=\"fab-btn fab-wishlist hidden\" id=\"fabWishlist\" aria-label=\"Open Wishlist\">)"
    fab_cart = """<button class="fab-btn hidden" id="fabCart" aria-label="Open Cart" style="background: rgba(26,26,26,0.9); border: 1px solid rgba(212,175,55,0.2);">
            <span class="material-symbols-outlined text-gold-500/90 text-[18px]">shopping_cart</span>
            <span class="wish-badge hidden" id="fabCartBadge" style="background: #D4AF37; color: #0A0A0A;">0</span>
        </button>
        """
    html = re.sub(fab_regex, fab_cart + r"\1", html)

    # 6. Add Cart Modal UI (Copy Wishlist Modal but edit it)
    modal_regex = r"(<!-- ═══════════════════════════════════════\s*FLOATING ACTION BUTTONS\s*═══════════════════════════════════════ -->)"
    cart_modal_html = """<!-- ═══════════════════════════════════════
         CART MODAL
         ═══════════════════════════════════════ -->
    <div class="wishlist-modal-overlay" id="cartModal">
        <div class="wishlist-modal">
            <!-- Drag handle for mobile -->
            <div class="sm:hidden flex justify-center pt-3 pb-1">
                <div class="w-10 h-1 rounded-full bg-onyx-600/60"></div>
            </div>
            <div class="flex justify-between items-start p-6 pb-4 border-b" style="border-color: rgba(212,175,55,0.08);">
                <div>
                    <h3 class="text-lg font-display font-medium text-white mb-1">Your Shopping Cart</h3>
                    <p class="text-sand-200/40 text-[11px] tracking-[0.05em] mt-1 font-sans leading-[1.6]">Ready to proceed to checkout?</p>
                </div>
                <button id="closeCartModal" class="text-sand-200/40 hover:text-white transition-colors duration-500 min-h-[44px] min-w-[44px] flex items-center justify-center rounded-full hover:bg-onyx-700/40 flex-shrink-0 ml-2">
                    <span class="material-symbols-outlined text-lg">close</span>
                </button>
            </div>
            <div id="cartItems" class="p-5 space-y-3 max-h-[300px] overflow-y-auto">
                <p class="text-sand-200/30 text-sm text-center py-8 font-light" id="emptyCartMsg">Your cart is empty.<br><span class="text-[10px] tracking-wider uppercase mt-1 block">Add premium items to continue</span></p>
            </div>
            <div class="px-5 pb-2">
                <div class="border-t pt-4 flex justify-between items-center" style="border-color: rgba(212,175,55,0.06);">
                    <p class="text-sand-200/50 text-xs tracking-[0.1em] uppercase font-sans font-medium">Subtotal</p>
                    <p class="text-gold-500 text-lg font-medium" id="cartTotal">₹0</p>
                </div>
            </div>
            <div class="p-5 pt-4">
                <button onclick="alert('Proceeding to Shopify Checkout... (Coming Soon in Main Build, Client can test this UI design)')" class="btn-primary w-full bg-gold-400 hover:bg-gold-500 text-onyx-900 py-4 rounded-lg text-[11px] uppercase tracking-[0.2em] font-bold flex justify-center items-center gap-2.5 min-h-[52px]">
                    <span class="material-symbols-outlined text-[18px]">lock</span> Secure Checkout
                </button>
            </div>
        </div>
    </div>
    
    """
    html = re.sub(modal_regex, cart_modal_html + r"\1", html)

    # 7. Add Cart Modal Listeners at the end of the script block
    evt_regex = r"(document\.getElementById\(\"wishlistModal\"\)\.addEventListener\(\"click\", \(e\) => \{\s*if \(e\.target === wishlistModal\) \{\s*wishlistModal\.classList\.remove\(\"show\"\);\s*document\.body\.style\.overflow = '';\s*\}\s*\}\);\s*\})"
    cart_evt = """
        // Cart interactions
        if(fabCart) {
            fabCart.addEventListener("click", () => {
                cartModal.classList.add("show");
                document.body.style.overflow = 'hidden';
            });
            closeCartModal.addEventListener("click", () => {
                cartModal.classList.remove("show");
                document.body.style.overflow = '';
            });
            document.getElementById("cartModal").addEventListener("click", (e) => {
                if (e.target === cartModal) {
                    cartModal.classList.remove("show");
                    document.body.style.overflow = '';
                }
            });
            updateCartUI(); // initial call
        }"""
    html = re.sub(evt_regex, r"\1" + cart_evt, html, flags=re.DOTALL)


    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    add_cart_functionality()
    print("Cart injected.")
