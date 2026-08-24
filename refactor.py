import re

with open('css/style.css', 'r') as f:
    css = f.read()

# 1. We will find the existing @media (min-width: 1601px) block and rename it to @media (min-width: 1921px)
css = css.replace('@media (min-width: 1601px)', '/* ================= EXTRA WIDE (1921px and up) ================= */\n@media (min-width: 1921px)')

# 2. We will append a Normal Desktop block right before it.
# Actually, the user wants the ability to edit desktop and extra wide separately.
# Instead of moving everything, we can provide a commented section at the end of the file.

desktop_block = """
/* ================= NORMAL DESKTOP (1025px to 1920px) ================= */
/* 
  If you want to make layout changes that ONLY affect normal desktop monitors 
  (like laptops and 1080p screens) without breaking mobile or extra-wide screens, 
  put them here!
*/
@media (min-width: 1025px) and (max-width: 1920px) {
  /* Example: You can override .hero-content left position just for desktop here */
  .hero-content {
    /* left: 10px; */
  }
}

"""

css = css.replace('/* ================= EXTRA WIDE (1921px and up) ================= */', desktop_block + '/* ================= EXTRA WIDE (1921px and up) ================= */')

with open('css/style.css', 'w') as f:
    f.write(css)

