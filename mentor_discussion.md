# Mentor Discussion Points: Front-End Architecture & Industry Standards

This document contains a list of professional, industry-standard questions based on the technical challenges faced during the development of the Montana Casting Co. complex layout project. These questions focus on architecture, scalability, and best practices.

## 1. Design Handoff & Implementation (Figma/Zeplin)

**Context:** During development, there was ambiguity between structural constraints (e.g., Zeplin's 1400px bounding boxes) and actual UI borders.
*   **Question:** "When implementing designs from tools like Zeplin or Figma, there can sometimes be confusion between component bounding boxes and actual design borders. What is the industry standard process for resolving these ambiguities during the design-to-development handoff?"

## 2. Handling Ultra-Wide Screens (Responsive Design)

**Context:** We had to ensure the full-width Instagram image grid looked correct without stretching infinitely on extremely large monitors (1710px+).
*   **Question:** "With ultra-wide monitors becoming more common, what is the best practice when a design calls for 'full-width' elements? Is it preferred to strictly cap them with a `max-width` (e.g., 1600px) and a safe padding edge, or should certain visual components be allowed to stretch 100vw?"

## 3. Responsive Backgrounds & Aspect-Ratios

**Context:** The footer landscape mountain image was initially getting cropped by overlapping cards. We resolved this by manipulating the container's `aspect-ratio` and pinning the `background-position` to the bottom to dynamically create vertical breathing room.
*   **Question:** "For complex responsive background images that need to scale predictably without cropping critical parts of the image, what is the most robust approach used in production today? Is using modern CSS `aspect-ratio` now the universal standard over the legacy padding-bottom aspect-ratio hack?"

## 4. DOM Manipulation vs. CSS Reordering for Mobile

**Context:** The desktop footer layout (Logo Left, Newsletter Center, Links Right) had to be completely restructured for mobile (Newsletter Top, Links Middle, Logo Bottom) while also converting links to accordions. We achieved this entirely via CSS Flexbox `order`.
*   **Question:** "When a mobile layout drastically differs in visual order from the desktop layout, is it considered better practice to heavily rely on CSS Flexbox/Grid ordering, or does the industry prefer rendering conditionally separate DOM components (or duplicating nodes) to maintain structural simplicity?"

## 5. Managing Complex Stacking Contexts (Z-Index)

**Context:** The design featured decorative elements (fishing lures) that floated across multiple sections, requiring precise absolute positioning and negative margins.
*   **Question:** "In large-scale projects, when dealing with absolutely positioned decorative elements that overlap multiple distinct layout sections, what rules or frameworks do teams follow to manage `z-index` and stacking contexts to prevent future rendering bugs?"

## 6. Asset Resolution and Formats

**Context:** We utilized high-resolution PNGs (`@2x`, `@3x`) for small UI elements like the banner close icon to ensure crispness on retina displays.
*   **Question:** "In modern enterprise front-end development, is the use of SVG strictly enforced for all UI icons and logos, or is there still a valid use case for serving high-res (`@2x`/`@3x`) raster images in production?"
