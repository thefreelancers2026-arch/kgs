import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add CSS
    css_target = "    </style>"
    css_replace = """        /* ══════════════════════════════════════════════
           CATEGORY TABS
           ══════════════════════════════════════════════ */
        .category-tab {
            white-space: nowrap;
            transition: all 0.4s ease;
            border-bottom: 2px solid transparent;
            padding-bottom: 8px;
        }
        .category-tab.active {
            color: #D4AF37;
            border-bottom: 2px solid #D4AF37;
        }
        .cat-scroll::-webkit-scrollbar { display: none; }
        .cat-scroll { -ms-overflow-style: none; scrollbar-width: none; }
        
        .fade-in-scale {
            animation: fadeInScale 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        @keyframes fadeInScale {
            0% { opacity: 0; transform: scale(0.98) translateY(10px); }
            100% { opacity: 1; transform: scale(1) translateY(0); }
        }
    </style>"""
    html = html.replace(css_target, css_replace)

    # 2. Replace Product grid
    grid_regex = r"<!-- Product Grid -->\s*<div class=\"product-grid grid grid-cols-1 md:grid-cols-12 gap-4 sm:gap-5 lg:gap-6\">.*?<!-- Premium Mobile swipe hint -->"
    grid_replace = """<!-- Category Tabs -->
                <div class="mb-10 w-full overflow-hidden reveal">
                    <div class="cat-scroll flex gap-6 sm:gap-10 overflow-x-auto pb-4 items-center" id="categoryTabs">
                        <button class="category-tab active text-xs tracking-[0.2em] uppercase font-sans font-medium text-white/90" data-filter="All">All</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="Sofas & Seating">Sofas</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="Office Chairs & Tables">Office Desks</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="Wall Clocks">Clocks</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="Photo Frames">Frames</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="Decorative Statues">Statues</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="Water Fountains">Fountains</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="Artificial Plants">Plants</button>
                        <button class="category-tab text-xs tracking-[0.2em] uppercase font-sans font-medium text-sand-300 hover:text-white/80" data-filter="LED Chandeliers">Lighting</button>
                    </div>
                </div>

                <!-- Product Grid Container (Injected by JS) -->
                <div id="dynamic-product-grid" class="product-grid grid grid-cols-1 md:grid-cols-12 gap-4 sm:gap-5 lg:gap-6 min-h-[400px]">
                    <!-- Products rendered via JS -->
                </div>

                <!-- Premium Mobile swipe hint -->"""
    html = re.sub(grid_regex, grid_replace, html, flags=re.DOTALL)

    # 3. Add Script array and functions
    # Using regex to replace the old wishlist logic start up to the foreach binding
    script_regex = r"const productImages = \{.*?\};\s*document\.querySelectorAll\(\"\.wishlist-btn\"\)\.forEach\([^\{]+\{"
    script_replace = """// --- DYNAMIC PRODUCT DATA (From PRD) ---
        const DEMO_PRODUCTS = [
            { name: "Velvet 3-Seater Sofa", category: "Sofas & Seating", price: "₹24,999", img: "assets/sofa_indian_1775734816101.png", tag: "Best Seller", col: "md:col-span-6", type: "lg" },
            { name: "Premium Lounger", category: "Sofas & Seating", price: "₹18,500", img: "assets/sofa_indian_1775734816101.png", tag: "", col: "md:col-span-6", type: "lg" },
            { name: "Luxury Recliner", category: "Sofas & Seating", price: "₹32,000", img: "assets/sofa_indian_1775734816101.png", tag: "Premium", col: "md:col-span-6", type: "lg" },
            { name: "Executive Mesh Chair", category: "Office Chairs & Tables", price: "₹4,200", img: "assets/office_chair_indian_1775734837287.png", tag: "In Store", col: "md:col-span-6", type: "lg" },
            { name: "Wooden Study Desk", category: "Office Chairs & Tables", price: "₹9,800", img: "assets/office_chair_indian_1775734837287.png", tag: "", col: "md:col-span-6", type: "lg" },
            { name: "Antique Sweep Clock", category: "Wall Clocks", price: "₹2,100", img: "assets/wall_clock_indian_1775734853010.png", tag: "Best Seller", col: "md:col-span-4", type: "md" },
            { name: "Minimalist Metal Clock", category: "Wall Clocks", price: "₹1,850", img: "assets/wall_clock_indian_1775734853010.png", tag: "New", col: "md:col-span-4", type: "md" },
            { name: "Designer Pendulum", category: "Wall Clocks", price: "₹3,400", img: "assets/wall_clock_indian_1775734853010.png", tag: "", col: "md:col-span-4", type: "md" },
            { name: "Collage Frame Set", category: "Photo Frames", price: "₹1,200", img: "assets/photo_frame_indian_1775734866964.png", tag: "New", col: "md:col-span-4", type: "md" },
            { name: "Minimal Wood Frame", category: "Photo Frames", price: "₹650", img: "assets/photo_frame_indian_1775734866964.png", tag: "", col: "md:col-span-4", type: "md" },
            { name: "Silver Elegance Frame", category: "Photo Frames", price: "₹890", img: "assets/photo_frame_indian_1775734866964.png", tag: "In Store", col: "md:col-span-4", type: "md" },
            { name: "Golden Buddha", category: "Decorative Statues", price: "₹3,200", img: "assets/statue_indian_1775734881322.png", tag: "In Store", col: "md:col-span-4", type: "md" },
            { name: "Abstract Couple", category: "Decorative Statues", price: "₹2,800", img: "assets/statue_indian_1775734881322.png", tag: "", col: "md:col-span-4", type: "md" },
            { name: "Brass Ganesha", category: "Decorative Statues", price: "₹4,500", img: "assets/statue_indian_1775734881322.png", tag: "Best Seller", col: "md:col-span-4", type: "md" },
            { name: "Indoor Table Fountain", category: "Water Fountains", price: "₹5,600", img: "assets/fountain_indian_1775734897565.png", tag: "Best Seller", col: "md:col-span-6", type: "lg" },
            { name: "Zen Rock Fountain", category: "Water Fountains", price: "₹7,200", img: "assets/fountain_indian_1775734897565.png", tag: "New", col: "md:col-span-6", type: "lg" },
            { name: "Bonsai Tree Plant", category: "Artificial Plants", price: "₹950", img: "assets/plant_indian_1775734912222.png", tag: "New", col: "md:col-span-4", type: "md" },
            { name: "Monstera Floor Plant", category: "Artificial Plants", price: "₹2,400", img: "assets/plant_indian_1775734912222.png", tag: "", col: "md:col-span-4", type: "md" },
            { name: "Hanging Vines", category: "Artificial Plants", price: "₹600", img: "assets/plant_indian_1775734912222.png", tag: "", col: "md:col-span-4", type: "md" },
            { name: "Crystal Tier Chandelier", category: "LED Chandeliers", price: "₹18,500", img: "assets/chandelier_img_1775732840371.png", tag: "In Store", col: "md:col-span-6", type: "lg" },
            { name: "Modern Ring Pendant", category: "LED Chandeliers", price: "₹12,400", img: "assets/chandelier_img_1775732840371.png", tag: "New", col: "md:col-span-6", type: "lg" }
        ];

        // Ensure productImages map exists for wishlist UI
        const productImages = {};
        DEMO_PRODUCTS.forEach(p => productImages[p.name] = p.img);

        const dynamicGrid = document.getElementById("dynamic-product-grid");
        const categoryTabs = document.querySelectorAll(".category-tab");

        function renderProducts(filterCategory) {
            dynamicGrid.innerHTML = '';
            
            const filtered = filterCategory === 'All' 
                ? DEMO_PRODUCTS 
                : DEMO_PRODUCTS.filter(p => p.category === filterCategory);

            filtered.forEach((prod, index) => {
                const delayClass = ''; // Remove delay for instant feeling on filter
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
                    <div class="${prod.col} group relative product-card product-card-${prod.type} ${hClass} bg-onyx-800 reveal active ${delayClass} rounded-sm fade-in-scale">
                        <img src="${prod.img}" loading="lazy" class="w-full h-full object-cover opacity-60 group-hover:opacity-85" alt="${prod.name}">
                        <div class="absolute inset-0 bg-gradient-to-t ${prod.type === 'lg' ? 'from-onyx-900 via-onyx-900/30' : 'from-onyx-900 via-transparent'} to-transparent opacity-80 group-hover:opacity-${prod.type === 'lg' ? '60' : '55'} transition-opacity duration-1000"></div>
                        <button class="wishlist-btn ${isWish} absolute top-4 left-4 z-20 p-2.5 transition-all duration-500 group/wish flex items-center justify-center rounded-full hover:bg-onyx-900/50 min-h-[44px] min-w-[44px]" aria-label="Add to Wishlist" data-product="${prod.name}">
                            <span class="material-symbols-outlined text-white/40 group-hover/wish:text-gold-500 text-[24px] transition-all duration-500">favorite</span>
                        </button>
                        ${tagHtml}
                        <div class="absolute ${bottomClass}">
                            ${titleHtml}
                        </div>
                    </div>
                `;
                dynamicGrid.insertAdjacentHTML('beforeend', html);
            });
            
            // Re-attach wishlist listeners for the newly injected buttons
            attachWishlistListeners();
        }

        // Handle category clicks
        categoryTabs.forEach(tab => {
            tab.addEventListener("click", () => {
                categoryTabs.forEach(t => t.classList.remove("active", "text-white/90"));
                categoryTabs.forEach(t => t.classList.add("text-sand-300"));
                tab.classList.remove("text-sand-300");
                tab.classList.add("active", "text-white/90");
                renderProducts(tab.getAttribute("data-filter"));
            });
        });

        // Initialize grid
        renderProducts("All");

        function attachWishlistListeners() {
            document.querySelectorAll(".wishlist-btn").forEach(btn => {"""
    
    html = re.sub(script_regex, script_replace, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_html()
    print("Updated index.html")
