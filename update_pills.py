import re

def update_pills():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update CSS
    css_regex = r"/\*\s*══════════════════════════════════════════════\s*CATEGORY TABS\s*══════════════════════════════════════════════\s*\*/.*?@keyframes fadeInScale \{.*?\}\n\s*</style>"
    
    css_replace = """/* ══════════════════════════════════════════════
           CATEGORY TABS (Minimal & Elegant Glass)
           ══════════════════════════════════════════════ */
        .category-tab {
            white-space: nowrap;
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            padding: 10px 22px;
            border-radius: 40px;
            border: 1px solid rgba(255, 255, 255, 0.04);
            background: rgba(255, 255, 255, 0.015);
            font-size: 10px;
            font-weight: 500;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: rgba(213, 206, 196, 0.5); /* sand-300 fading */
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            cursor: pointer;
        }
        .category-tab:hover {
            color: #FAFAF8;
            border-color: rgba(212, 175, 55, 0.2);
            background: rgba(255, 255, 255, 0.04);
            transform: translateY(-1px);
        }
        .category-tab.active {
            color: #0A0A0A;
            background: #D4AF37;
            border-color: #D4AF37;
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.2);
            font-weight: 600;
            transform: translateY(0);
        }

        .cat-scroll-container {
            position: relative;
        }
        .cat-scroll-container::after {
            content: '';
            position: absolute;
            top: 0; right: 0; bottom: 0;
            width: 60px;
            background: linear-gradient(to right, transparent, #0A0A0A);
            pointer-events: none;
        }

        .cat-scroll::-webkit-scrollbar { display: none; }
        .cat-scroll { -ms-overflow-style: none; scrollbar-width: none; }
        
        .fade-in-scale {
            opacity: 0;
            animation: fadeInBlur 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        @keyframes fadeInBlur {
            0% { opacity: 0; transform: scale(0.96) translateY(20px); filter: blur(8px); }
            100% { opacity: 1; transform: scale(1) translateY(0); filter: blur(0); }
        }
    </style>"""
    html = re.sub(css_regex, css_replace, html, flags=re.DOTALL)

    # 2. Update HTML Tabs
    tabs_regex = r"<!-- Category Tabs -->\s*<div class=\"mb-10 w-full overflow-hidden reveal\">\s*<div class=\"cat-scroll flex gap-6 sm:gap-10 overflow-x-auto pb-4 items-center\" id=\"categoryTabs\">.*?</div>\s*</div>"
    
    tabs_replace = """<!-- Category Tabs -->
                <div class="mb-12 w-full overflow-hidden reveal cat-scroll-container">
                    <div class="cat-scroll flex gap-3 sm:gap-4 overflow-x-auto pb-6 pt-2 px-1 items-center" id="categoryTabs">
                        <button class="category-tab active" data-filter="All">All</button>
                        <button class="category-tab" data-filter="Sofas & Seating">Sofas</button>
                        <button class="category-tab" data-filter="Office Chairs & Tables">Office Desks</button>
                        <button class="category-tab" data-filter="Wall Clocks">Clocks</button>
                        <button class="category-tab" data-filter="Photo Frames">Frames</button>
                        <button class="category-tab" data-filter="Decorative Statues">Statues</button>
                        <button class="category-tab" data-filter="Water Fountains">Fountains</button>
                        <button class="category-tab" data-filter="Artificial Plants">Plants</button>
                        <button class="category-tab" data-filter="LED Chandeliers">Lighting</button>
                    </div>
                </div>"""
    html = re.sub(tabs_regex, tabs_replace, html, flags=re.DOTALL)

    # 3. Update JS Logic (Tabs)
    js_tabs_regex = r"categoryTabs\.forEach\(tab => {\s*tab\.addEventListener\(\"click\", \(\) => \{\s*categoryTabs\.forEach\(t => t\.classList\.remove\(\"active\", \"text-white/90\"\)\);\s*categoryTabs\.forEach\(t => t\.classList\.add\(\"text-sand-300\"\)\);\s*tab\.classList\.remove\(\"text-sand-300\"\);\s*tab\.classList\.add\(\"active\", \"text-white/90\"\);\s*renderProducts\(tab\.getAttribute\(\"data-filter\"\)\);\s*\}\);\s*\}\);"
    js_tabs_replace = """categoryTabs.forEach(tab => {
            tab.addEventListener("click", () => {
                if (tab.classList.contains("active")) return;
                categoryTabs.forEach(t => t.classList.remove("active"));
                tab.classList.add("active");
                renderProducts(tab.getAttribute("data-filter"));
            });
        });"""
    html = re.sub(js_tabs_regex, js_tabs_replace, html)

    # 4. Update JS Logic (Staggered Animation)
    delay_regex = r"const delayClass = ''; // Remove delay for instant feeling on filter.*?<div class=\"\$\{prod\.col\} group relative product-card product-card-\$\{prod\.type\} \$\{hClass\} bg-onyx-800 reveal active \$\{delayClass\} rounded-sm fade-in-scale\">"
    delay_replace = """const staggerDelay = index * 0.08; // 80ms stagger
                const hClass = prod.type === 'lg' ? 'h-[420px] sm:h-[520px] lg:h-[560px]' : 'h-[320px] sm:h-[420px] lg:h-[460px]';
                const tagHtml = prod.tag ? `<div class="absolute top-5 right-5"><span class="text-[9px] tracking-[0.2em] uppercase bg-gold-500/10 border border-gold-500/25 text-gold-300 px-3 py-1 font-sans font-medium">${prod.tag}</span></div>` : '';
                const titleHtml = prod.type === 'lg'
                    ? `<div class="transform translate-y-3 group-hover:translate-y-0 transition-transform duration-1000 ease-[cubic-bezier(0.16,1,0.3,1)]">
                            <h3 class="text-2xl sm:text-3xl font-display font-medium text-white mb-1">${prod.name}</h3>
                            <p class="text-sand-300 text-[11px] tracking-[0.2em] uppercase font-sans">${prod.price}</p>
                       </div>
                       <span class="w-10 h-10 sm:w-11 sm:h-11 rounded-full border border-gold-500/20 flex items-center justify-center text-gold-500 group-hover:bg-gold-500 group-hover:text-onyx-900 transition-all duration-800 transform translate-x-3 opacity-0 group-hover:opacity-100 group-hover:translate-x-0 flex-shrink-0">
                            <span class="material-symbols-outlined text-lg">east</span>
                       </span>`
                    : `<h3 class="text-xl sm:text-2xl font-display font-medium text-white mb-1">${prod.name}</h3>
                       <p class="text-gold-400 text-[10px] tracking-[0.15em] uppercase font-sans">${prod.price}</p>`;
                
                const bottomClass = prod.type === 'lg' 
                    ? 'bottom-8 sm:bottom-10 left-6 sm:left-10 right-6 sm:right-10 flex justify-between items-end'
                    : 'bottom-6 sm:bottom-8 left-6 sm:left-8';
                    
                const isWish = wishlist.includes(prod.name) ? 'wish-active' : '';

                const html = `
                    <div class="${prod.col} group relative product-card product-card-${prod.type} ${hClass} bg-onyx-800 reveal active rounded-sm fade-in-scale" style="animation-delay: ${staggerDelay}s;">"""
    html = re.sub(delay_regex, delay_replace, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_pills()
    print("Updated pills successfully")
