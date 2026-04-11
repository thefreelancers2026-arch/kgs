/**
 * KGS Home Decors - Premium Dark Luxury Theme
 * Custom JavaScript for Wishlist, Cart, and Interactions
 */

document.addEventListener('DOMContentLoaded', function() {
  // ========================================
  // WISHLIST SYSTEM (localStorage)
  // ========================================
  const wishlist = JSON.parse(localStorage.getItem('kgs_wishlist') || '[]');
  const fabWishlist = document.getElementById('fabWishlist');
  const fabWishBadge = document.getElementById('fabWishBadge');
  const wishlistModal = document.getElementById('wishlistModal');
  const closeWishlistModal = document.getElementById('closeWishlistModal');
  const wishlistItems = document.getElementById('wishlistItems');
  const emptyWishMsg = document.getElementById('emptyWishMsg');

  // ========================================
  // CART SYSTEM (Shopify Cart API)
  // ========================================
  const cart = JSON.parse(localStorage.getItem('kgs_cart') || '[]');
  const fabCart = document.getElementById('fabCart');
  const fabCartBadge = document.getElementById('fabCartBadge');
  const cartModal = document.getElementById('cartModal');
  const closeCartModal = document.getElementById('closeCartModal');
  const cartItemsWrapper = document.getElementById('cartItems');
  const emptyCartMsg = document.getElementById('emptyCartMsg');
  const cartTotalEl = document.getElementById('cartTotal');

  // Demo products for preview (matches section data)
  const DEMO_PRODUCTS = [
    { name: "Velvet 3-Seater Sofa", category: "Sofas & Seating", price: "₹24,999", img: "sofa_img.png" },
    { name: "Premium Lounger", category: "Sofas & Seating", price: "₹18,500", img: "sofa_img.png" },
    { name: "Executive Mesh Chair", category: "Office Chairs & Tables", price: "₹4,200", img: "office_chair_img.png" },
    { name: "Antique Sweep Clock", category: "Wall Clocks", price: "₹2,100", img: "wall_clock_img.png" },
    { name: "Collage Frame Set", category: "Photo Frames", price: "₹1,200", img: "photo_frame_img.png" },
    { name: "Golden Buddha", category: "Decorative Statues", price: "₹3,200", img: "statue_img.png" },
    { name: "Indoor Table Fountain", category: "Water Fountains", price: "₹5,600", img: "fountain_img.png" },
    { name: "Bonsai Tree Plant", category: "Artificial Plants", price: "₹950", img: "plant_indian.png" },
    { name: "Crystal Tier Chandelier", category: "LED Chandeliers", price: "₹18,500", img: "chandelier_img.png" }
  ];

  // ========================================
  // WISHLIST FUNCTIONS
  // ========================================
  function attachWishlistListeners() {
    document.querySelectorAll('.wishlist-btn').forEach(btn => {
      const productName = btn.getAttribute('data-product');
      const variantId = btn.getAttribute('data-variant-id');
      const handle = btn.getAttribute('data-handle');
      
      if (wishlist.includes(productName)) btn.classList.add('wish-active');

      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const idx = wishlist.indexOf(productName);
        if (idx === -1) {
          wishlist.push(productName);
          btn.classList.add('wish-active');
          
          // If Shopify product, add to Shopify wishlist app
          if (variantId && typeof window.Shopify !== 'undefined') {
            // Wishlist app integration would go here
            console.log('Added to wishlist:', productName);
          }
        } else {
          wishlist.splice(idx, 1);
          btn.classList.remove('wish-active');
        }
        
        localStorage.setItem('kgs_wishlist', JSON.stringify(wishlist));
        updateWishlistUI();
      });
    });
  }

  function updateWishlistUI() {
    const count = wishlist.length;
    if (count > 0) {
      fabWishlist.classList.remove('hidden');
      fabWishBadge.classList.remove('hidden');
      fabWishBadge.innerText = count;
      fabWishBadge.style.transform = 'scale(1.3)';
      setTimeout(() => fabWishBadge.style.transform = 'scale(1)', 250);
    } else {
      fabWishlist.classList.add('hidden');
      fabWishBadge.classList.add('hidden');
    }
    renderWishlistItems();
  }

  function renderWishlistItems() {
    if (!wishlistItems) return;
    wishlistItems.querySelectorAll('.wish-item').forEach(el => el.remove());
    
    if (wishlist.length === 0) { 
      if (emptyWishMsg) emptyWishMsg.classList.remove('hidden'); 
      const wTotal = document.getElementById('wishTotal');
      if (wTotal) wTotal.innerText = '₹0';
      return; 
    }
    if (emptyWishMsg) emptyWishMsg.classList.add('hidden');

    let total = 0;
    wishlist.forEach(name => {
      const prod = DEMO_PRODUCTS.find(p => p.name === name) || { price: '₹0', img: 'sofa_img.png' };
      let priceStr = '';
      if (prod.price) {
        const priceNum = parseInt(prod.price.replace(/[^0-9]/g, '')) || 0;
        total += priceNum;
        priceStr = `<p class="text-gold-500/80 text-[11px] tracking-wider mt-1">${prod.price}</p>`;
      }

      const item = document.createElement('div');
      item.className = 'wish-item flex items-center gap-4 bg-onyx-700/20 border border-onyx-600/30 rounded-lg p-3';
      item.innerHTML = `
        <img src="${prod.img}" class="w-12 h-12 rounded object-cover flex-shrink-0 opacity-80" alt="${name}">
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

    const wishTotalEl = document.getElementById('wishTotal');
    if (wishTotalEl) {
      wishTotalEl.innerText = '₹' + total.toLocaleString('en-IN');
    }

    wishlistItems.querySelectorAll('.wish-remove').forEach(btn => {
      btn.addEventListener('click', function() {
        const name = btn.getAttribute('data-name');
        const idx = wishlist.indexOf(name);
        if (idx !== -1) {
          wishlist.splice(idx, 1);
          localStorage.setItem('kgs_wishlist', JSON.stringify(wishlist));
          
          document.querySelectorAll('.wishlist-btn').forEach(hb => {
            if (hb.getAttribute('data-product') === name) {
              hb.classList.remove('wish-active');
            }
          });
          
          updateWishlistUI();
        }
      });
    });
  }

  // ========================================
  // CART FUNCTIONS (Shopify Cart API)
  // ========================================
  function attachCartListeners() {
    document.querySelectorAll('.cart-btn, .quick-add-btn').forEach(btn => {
      const productName = btn.getAttribute('data-product');
      const variantId = btn.getAttribute('data-variant-id');
      const productId = btn.getAttribute('data-product-id');
      const quantity = btn.getAttribute('data-quantity') || 1;
      
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        // Shopify Cart API integration
        if (variantId && typeof Shopify !== 'undefined') {
          addToCartShopify(variantId, quantity);
        } else {
          // Demo mode - use localStorage
          const idx = cart.indexOf(productName);
          const icon = btn.querySelector('.cart-icon');
          
          if (idx === -1) {
            cart.push(productName);
            btn.classList.add('cart-active');
            icon.style.transform = 'scale(0.8)';
            setTimeout(() => {
              icon.innerText = 'check';
              icon.style.transform = 'scale(1.1)';
              icon.classList.add('text-gold-500');
              icon.classList.remove('text-white/40');
              setTimeout(() => icon.style.transform = 'scale(1)', 150);
            }, 150);
          } else {
            cart.splice(idx, 1);
            btn.classList.remove('cart-active');
            icon.style.transform = 'scale(0.8)';
            setTimeout(() => {
              icon.innerText = 'shopping_cart';
              icon.style.transform = 'scale(1.1)';
              icon.classList.remove('text-gold-500');
              icon.classList.add('text-white/40');
              setTimeout(() => icon.style.transform = 'scale(1)', 150);
            }, 150);
          }
          
          localStorage.setItem('kgs_cart', JSON.stringify(cart));
          updateCartUI();
        }
      });
    });
  }

  function addToCartShopify(variantId, quantity) {
    fetch(window.Shopify.routes.root + 'cart/add.js', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        items: [{
          id: variantId,
          quantity: parseInt(quantity)
        }]
      })
    })
    .then(response => response.json())
    .then(data => {
      console.log('Added to cart:', data);
      updateCartShopify();
    })
    .catch(error => {
      console.error('Error adding to cart:', error);
    });
  }

  function updateCartUI() {
    const count = cart.length;
    if (count > 0) {
      fabCart.classList.remove('hidden');
      fabCartBadge.classList.remove('hidden');
      fabCartBadge.innerText = count;
      fabCartBadge.style.transform = 'scale(1.3)';
      setTimeout(() => fabCartBadge.style.transform = 'scale(1)', 250);
    } else {
      fabCart.classList.add('hidden');
      fabCartBadge.classList.add('hidden');
    }
    renderCartItems();
  }

  function updateCartShopify() {
    fetch(window.Shopify.routes.root + 'cart.js')
      .then(response => response.json())
      .then(cart => {
        document.querySelectorAll('.cart-count').forEach(el => {
          el.innerText = cart.item_count;
        });
      });
  }

  function renderCartItems() {
    if (!cartItemsWrapper) return;
    cartItemsWrapper.querySelectorAll('.cart-item').forEach(el => el.remove());
    
    if (cart.length === 0) { 
      if (emptyCartMsg) emptyCartMsg.classList.remove('hidden'); 
      if (cartTotalEl) cartTotalEl.innerText = '₹0';
      return; 
    }
    if (emptyCartMsg) emptyCartMsg.classList.add('hidden');

    let total = 0;
    cart.forEach(name => {
      const prod = DEMO_PRODUCTS.find(p => p.name === name) || { price: '₹0', img: 'sofa_img.png' };
      
      if (prod.price) {
        const priceNum = parseInt(prod.price.replace(/[^0-9]/g, '')) || 0;
        total += priceNum;
      }

      const item = document.createElement('div');
      item.className = 'cart-item flex items-center gap-4 bg-onyx-700/20 border border-onyx-600/30 rounded-lg p-3';
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

    if (cartTotalEl) {
      cartTotalEl.innerText = '₹' + total.toLocaleString('en-IN');
    }

    cartItemsWrapper.querySelectorAll('.cart-remove').forEach(btn => {
      btn.addEventListener('click', function() {
        const name = btn.getAttribute('data-name');
        const idx = cart.indexOf(name);
        if (idx !== -1) {
          cart.splice(idx, 1);
          localStorage.setItem('kgs_cart', JSON.stringify(cart));
          
          document.querySelectorAll('.cart-btn').forEach(hb => {
            if (hb.getAttribute('data-product') === name) {
              hb.classList.remove('cart-active');
              const icon = hb.querySelector('.cart-icon');
              if (icon) {
                icon.innerText = 'shopping_cart';
                icon.classList.remove('text-gold-500');
                icon.classList.add('text-white/40');
              }
            }
          });
          
          updateCartUI();
        }
      });
    });
  }

  // ========================================
  // MODAL HANDLERS
  // ========================================
  if (fabWishlist) {
    fabWishlist.addEventListener('click', function() {
      renderWishlistItems();
      wishlistModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  }

  function closeWishlistModalHandler() {
    if (wishlistModal) wishlistModal.classList.remove('open');
    document.body.style.overflow = '';
  }
  
  if (closeWishlistModal) {
    closeWishlistModal.addEventListener('click', closeWishlistModalHandler);
  }
  
  if (wishlistModal) {
    wishlistModal.addEventListener('click', function(e) {
      if (e.target === wishlistModal) closeWishlistModalHandler();
    });
  }

  if (fabCart) {
    fabCart.addEventListener('click', function() {
      cartModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
    
    if (closeCartModal) {
      closeCartModal.addEventListener('click', function() {
        cartModal.classList.remove('open');
        document.body.style.overflow = '';
      });
    }
    
    if (cartModal) {
      cartModal.addEventListener('click', function(e) {
        if (e.target === cartModal) {
          cartModal.classList.remove('open');
          document.body.style.overflow = '';
        }
      });
    }
    
    updateCartUI();
  }

  // ========================================
  // CATEGORY FILTERING
  // ========================================
  const categoryTabs = document.querySelectorAll('.category-tab');
  
  categoryTabs.forEach(tab => {
    tab.addEventListener('click', function() {
      if (tab.classList.contains('active')) return;
      
      categoryTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      
      const filter = tab.getAttribute('data-filter');
      filterProducts(filter);
    });
  });

  function filterProducts(category) {
    const grid = document.getElementById('dynamic-product-grid');
    if (!grid) return;
    
    const products = grid.querySelectorAll('.product-card');
    
    products.forEach((product, index) => {
      const productCategory = product.getAttribute('data-category');
      
      if (category === 'All' || productCategory === category) {
        product.style.display = 'block';
        product.style.animationDelay = (index * 0.08) + 's';
      } else {
        product.style.display = 'none';
      }
    });
  }

  // ========================================
  // SCROLL REVEAL (IntersectionObserver)
  // ========================================
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.06, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(el => {
    revealObserver.observe(el);
  });

  // ========================================
  // INITIALIZE
  // ========================================
  attachWishlistListeners();
  attachCartListeners();
  updateWishlistUI();
  
  // Update cart from Shopify if available
  if (typeof Shopify !== 'undefined') {
    updateCartShopify();
  }

  console.log('KGS Home Decors Theme Loaded');
});