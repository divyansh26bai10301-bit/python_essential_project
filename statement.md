# Project Statement: FreshMart Grocery Billing System

## 1. Problem Statement
In small local grocery stores, billing is usually done on paper or with small handheld calculators. During morning and evening rush hours when many people come to buy milk, vegetables, or eggs, cashiers can easily make calculation mistakes when subtracting discounts or calculating 5% gst. Also, sometimes items run out of stock on the shelves and the cashier still bills them, which annoys customers. So I made a simple python command line billing system where the cashier can add items to a sale, check that enough stock is available, apply discount coupon codes, and print out an accurate receipt automatically.

## 2. Scope of the Project
This project handles the everyday checkout and billing tasks for a grocery shop:
- Showing the store catalog with product codes, names, categories, prices, and stock numbers.
- Adding multiple grocery items in a continuous loop until the customer is done.
- Checking that the requested quantity is actually available in stock before adding.
- Applying coupon discounts like SAVE10 (10% off) or GROCERY20 (20% off).
- Calculating the subtotal, coupon savings, 5% gst, and final total.
- Deducting the sold quantities from store stock.
- Printing a neat receipt and letting the user reprint the last receipt if needed.

## 3. Target Users
- Small grocery shop owners and cashiers who want an easy terminal billing system.
- Customers who want a clear printed receipt showing their items, discounts, and gst breakdown.

## 4. High-Level Features
- Catalog Viewer: Displays product codes, descriptions, categories, rates, current stock, and valid coupon codes.
- Order Loop: Lets the cashier add products in a while loop and validates stock limits.
- Coupon Discounts: Checks coupon codes using if-elif statements and applies percentage discounts.
- Automatic Billing: Calculates subtotals, discounts, 5% gst, and grand total without manual math.
- In-Memory Stock Tracking: Automatically deducts purchased quantities from stock upon successful checkout.
- Receipt Printing: Prints a clean guest check invoice in the terminal with option to view last bill.
