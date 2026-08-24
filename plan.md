# CSS Architecture Refactoring

## Problem Statement
The current CSS uses a "cascading base" approach where global rules apply to all breakpoints, and larger screens (like `1601px+`) override them. This causes conflicts: modifying base rules for desktop unintentionally affects extra-wide screens, and users with 1920px monitors fall into the "extra-wide" bucket, causing confusion.

## Proposed Changes
I will implement a **Strict Isolation Architecture** for the layout of the Hero Section and Product Cards.

1. **Clean Base Rules**: Strip layout properties (`left`, `width`, `margin`, `flex` sizes) from the global base rules for `.hero-content` and `.product-details`. Keep only shared cosmetics (fonts, colors).
2. **Explicit Breakpoint Blocks**: Create strictly bounded media queries at the end of the file.
   - `@media (max-width: 768px)` -> Mobile only
   - `@media (min-width: 769px) and (max-width: 1024px)` -> Tablet only
   - `@media (min-width: 1025px) and (max-width: 1600px)` -> Normal Desktop
   - `@media (min-width: 1601px)` -> Extra Wide (Ultrawide)
3. **Move Layout Logic**: Place the specific positioning (`left: 10px`, `width: 610px`, etc.) strictly inside the `Normal Desktop` block. Place the scaled-up values (`left: 15vw`) strictly inside the `Extra Wide` block.

This guarantees that editing properties in the "Normal Desktop" block will **never** cascade or bleed into the "Extra Wide" block, and vice-versa.

## Verification
- Editing Desktop `left` will immediately reflect on screens <= 1600px.
- Editing Extra Wide `left` will independently reflect on screens >= 1601px.
- No bleeding of layout rules across breakpoints.
