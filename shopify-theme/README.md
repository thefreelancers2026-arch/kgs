# KGS Home Decors - Shopify 2.0 Theme

Premium dark luxury e-commerce theme for KGS Home Decors - Home decor shop in Virudhachalam, Tamil Nadu.

## Theme Features

- **Dark Luxury Design**: Onyx (#0A0A0A) background with Gold (#D4AF37) accents
- **Typography**: Cormorant Garamond (headings), Montserrat (body)
- **8 Product Categories**: Sofas, Office Chairs, Wall Clocks, Photo Frames, Statues, Fountains, Plants, Lighting
- **Wishlist System**: LocalStorage-based wishlist with modal
- **Cart System**: Shopify Cart API integration + local demo mode
- **WhatsApp Checkout**: Direct WhatsApp order button
- **Contact Form**: Shopify native contact form
- **Mobile Responsive**: Mobile-first design
- **Scroll Animations**: IntersectionObserver-based reveal effects

## Installation

1. **Create Shopify Store**
   - Sign up at shopify.com
   - Create new store or use existing

2. **Upload Theme**
   - Go to Online Store > Themes
   - Add theme > Upload theme file (zip)
   - Or use Shopify CLI: `shopify theme push`

3. **Configure Settings**
   - Go to Theme Settings
   - Set colors, fonts, logo text
   - Configure contact info (phone, WhatsApp)

4. **Create Collections**
   - Create 8 collections matching PRD categories:
     - Sofas and Seating
     - Office Chairs and Tables
     - Wall Clocks
     - Photo Frames
     - Decorative Statues
     - Water Fountains
     - Artificial Plants
     - LED Chandeliers

5. **Add Products**
   - Upload product images and details
   - Set prices and inventory

## Theme Structure

```
shopify-theme/
├── config/
│   ├── settings_schema.json    # Theme settings
│   └── theme.json               # Theme configuration
├── layout/
│   └── theme.liquid             # Main layout
├── sections/
│   ├── header.liquid            # Navigation
│   ├── hero.liquid              # Hero section
│   ├── product-grid.liquid      # Product grid with filters
│   ├── showroom.liquid          # About/showroom section
│   ├── marquee.liquid           # Scrolling banner
│   ├── contact-form.liquid      # Contact form
│   ├── footer.liquid            # Footer
│   ├── fab-buttons.liquid       # Floating action buttons
│   ├── main-product.liquid      # Product page
│   ├── main-collection.liquid   # Collection page
│   └── main-cart.liquid         # Cart page
├── snippets/
│   ├── product-card.liquid      # Product card component
│   └── language-toggle.liquid   # Language switcher
├── assets/
│   ├── styles.css               # Custom styles
│   └── script.js                # Custom JS
├── templates/
│   ├── index.json               # Homepage
│   ├── product.json             # Product page
│   ├── collection.json          # Collection page
│   └── cart.json                # Cart page
└── locales/
    └── en.default.json          # Translations
```

## Demo Mode

The theme includes demo products for preview. To enable real Shopify products:
1. Create collections in Shopify admin
2. Add products to collections
3. Update `product-grid.liquid` section to use actual collection

## Payment Gateway

- **Razorpay**: Configure in Shopify Settings > Payments
- **COD**: Enable Cash on Delivery in Shopify Settings

## Notifications (n8n Ready)

Webhooks for order notifications:
- New order: Send WhatsApp to admin
- Order status updates: Email to customer

## Support

- Theme Author: The Freelancers (Avinash A)
- Email: thefreelancers2026@gmail.com
- Phone: +91 88381 95254

## License

MIT License - KGS Home Decors

---

Built with Shopify 2.0 Theme Architecture