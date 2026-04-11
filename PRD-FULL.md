# PRODUCT REQUIREMENTS DOCUMENT
## KGS Home Decors — E-Commerce Website (Full Build)
### Version 2.0 | April 2026 | Prepared by Avinash A, The Freelancers

---

## 1. PROJECT OVERVIEW

| Item | Details |
|------|---------|
| **Project Name** | KGS Home Decors — Full E-Commerce Website |
| **Client** | KGS Home Decors, Virudhachalam, Tamil Nadu |
| **Platform** | Shopify |
| **Payment Gateway** | Razorpay (UPI, Cards, Net Banking, COD) |
| **Languages** | English and Tamil |
| **Target Audience** | Home decor customers across Tamil Nadu |
| **Delivery Scope** | All Tamil Nadu |
| **Estimated Timeline** | 8-10 weeks from approval |

---

## 2. PROJECT GOALS

The KGS Home Decors website must:

1. ✅ Allow customers to **browse 500+ home decor products** online
2. ✅ Enable **direct purchases** through the website via Razorpay
3. ✅ Generate **WhatsApp enquiries** for customers who prefer not to pay online
4. ✅ Give KGS owner **full control** to manage products, orders, and discounts
5. ✅ Make KGS appear on **Google** when customers search for home decor in Tamil Nadu
6. ✅ **Automate notifications** so the owner is alerted instantly on WhatsApp and email
7. ✅ Provide **customer accounts** for order tracking and wishlist

---

## 3. USER ROLES

| Role | Description |
|------|-------------|
| **Customer** | Any person visiting to browse or purchase products |
| **Registered Customer** | Can track orders, save wishlist, view order history |
| **Admin (KGS Owner)** | Manage products, orders, discounts, and customer data |
| **Developer (Avinash A)** | Build, deploy, and maintain the website |

---

## 4. FUNCTIONAL REQUIREMENTS — CUSTOMER

### 4.1 Product Browsing

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| C-01 | Browse all products on homepage | Must Have | Default view |
| C-02 | Filter products by category (8 categories) | Must Have | Sofas, Clocks, Plants, etc. |
| C-03 | **Search products by name or keyword** | Must Have | ✅ Added to demo |
| C-04 | View individual product page with photos, price, description | Must Have | Full PDP |
| C-05 | View product in English and Tamil | Should Have | Language toggle |
| C-06 | Related products on product page | Nice to Have | Increases AOV |

### 4.2 Cart & Checkout

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| C-07 | Add product to cart | Must Have | ✅ From product page or listing |
| C-08 | View and edit cart | Must Have | Change quantity, remove items |
| C-09 | Enter delivery address at checkout | Must Have | All Tamil Nadu addresses |
| C-10 | Apply coupon/discount code | Must Have | Code validation |
| C-11 | See order summary before payment | Must Have | Items, delivery, total |
| C-12 | **Payment: UPI, Card, Net Banking, COD** | Must Have | All via Razorpay |
| C-13 | **WhatsApp order without online payment** | Must Have | ✅ Button exists |
| C-14 | Email confirmation after order | Must Have | Auto email via Shopify |
| C-15 | SMS confirmation after order | Should Have | Shopify SMS integration |

### 4.3 Customer Account

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| C-16 | Register with email and password | Must Have | Standard signup |
| C-17 | Log in and log out | Must Have | Session management |
| C-18 | View order history | Must Have | All past orders |
| C-19 | Track current order status | Must Have | Pending → Shipped → Delivered |
| C-20 | Save products to wishlist | Must Have | ✅ Heart icon on product |
| C-21 | Manage saved addresses | Should Have | For repeat orders |
| C-22 | Reset password via email | Must Have | Forgot password flow |

---

## 5. FUNCTIONAL REQUIREMENTS — ADMIN PANEL

### 5.1 Product Management

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| A-01 | Add new product with photos, price, description, category | Must Have | Shopify admin |
| A-02 | Edit existing product details | Must Have | Any field editable |
| A-03 | Delete a product | Must Have | With confirmation |
| A-04 | Manage product stock quantity | Must Have | Stock level visible |
| A-05 | Low stock alert when below threshold | Should Have | WhatsApp or email |
| A-06 | Organize products into categories | Must Have | 8 categories minimum |
| A-07 | Mark product as featured on homepage | Should Have | Homepage spotlight |

### 5.2 Order Management

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| A-08 | View all orders with customer name, items, amount, status | Must Have | Orders dashboard |
| A-09 | Update order status — confirmed, shipped, delivered, cancelled | Must Have | Customer notified |
| A-10 | **WhatsApp notification when new order** | Must Have | n8n automation |
| A-11 | View customer contact details | Must Have | Name, phone, address |
| A-12 | Filter orders by status or date | Should Have | Daily management |

### 5.3 Discount Management

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| A-13 | Create discount codes (%, fixed) | Must Have | Shopify discounts |
| A-14 | Set expiry date on discount codes | Must Have | Seasonal offers |
| A-15 | Limit discount usage count | Should Have | e.g., first 50 customers |

### 5.4 Customer Management

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| A-16 | View all registered customers | Must Have | Name, email, order count |
| A-17 | View individual customer order history | Should Have | Repeat tracking |

---

## 6. PRODUCT CATEGORIES

| # | Category Name | Examples |
|---|---------------|-----------|
| 1 | Sofas and Seating | 3-seater sofas, recliners, sofa sets, chairs |
| 2 | Office Chairs and Tables | Executive chairs, study tables, computer desks |
| 3 | Wall Clocks | Wooden clocks, metal clocks, designer clocks |
| 4 | Photo Frames | Single frames, collage frames, digital frames |
| 5 | Decorative Statues | Figurines, animal statues, abstract sculptures |
| 6 | Water Fountains | Indoor fountains, tabletop fountains, wall fountains |
| 7 | Artificial Plants | Succulents, bonsai, flower arrangements, hanging plants |
| 8 | LED Chandeliers | Ceiling lights, pendant lights, decorative lighting |

---

## 7. NOTIFICATION REQUIREMENTS

| Event | Customer Gets | Admin Gets | How |
|-------|---------------|------------|-----|
| New order placed | Email + SMS | **WhatsApp alert** | Shopify + n8n |
| Order status updated | Email notification | — | Shopify auto |
| Order delivered | Email confirmation | — | Shopify auto |
| Order cancelled | Email + refund info | — | Shopify auto |
| **Low stock** | — | **WhatsApp alert** | n8n |
| New customer registered | Welcome email | — | Shopify auto |

---

## 8. NON-FUNCTIONAL REQUIREMENTS

| Area | Requirement |
|------|-------------|
| **Performance** | Website loads under 3 seconds on mobile. All images compressed. |
| **Mobile First** | Fully responsive. 90% of Tamil Nadu customers browse on phone. |
| **Security** | Payments via Razorpay — no card data on server. SSL mandatory. |
| **Uptime** | Shopify guarantees 99.9% uptime. 24/7/365 accessible. |
| **SEO** | SEO title, meta description, alt text on images. On Google within 30 days. |
| **Browser Support** | Chrome, Safari, Firefox. Android and iOS. |
| **Language** | English primary. Tamil support for product names via language toggle. |
| **Accessibility** | Color contrast sufficient. Font sizes min 14px. WhatsApp always visible. |

---

## 9. OUT OF SCOPE — VERSION 1.0

- Product reviews and ratings by customers
- Live chat support on website
- Loyalty points or rewards programme
- Multi-vendor or marketplace features
- Custom mobile app (Android/iOS)
- Pan-India shipping with courier APIs

---

## 10. ASSUMPTIONS AND DEPENDENCIES

- Client will provide **Razorpay business account** with GST and bank details before Phase 3
- Client will be available for **one full day product photoshoot** within first 2 weeks
- Client will provide **complete product list** with names and prices before data entry
- Client will provide **WhatsApp number** for order notifications
- **Domain name** purchased and DNS configured by The Freelancers
- **Shopify monthly subscription** included in monthly maintenance

---

## APPROVAL

| Role | Signature | Date |
|------|-----------|------|
| Client (KGS Home Decors) | _________________ | __________ |
| Developer (The Freelancers) | Avinash A | April 2026 |

---

**Document Version**: 2.0  
**Prepared by**: Avinash A  
**Contact**: +91 88381 95254 | thefreelancers2026@gmail.com