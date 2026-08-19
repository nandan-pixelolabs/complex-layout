// Mobile menu / banner interactions
document.addEventListener('DOMContentLoaded', () => {
  const closeBannerBtn = document.querySelector('.close-banner');
  if (closeBannerBtn) {
    closeBannerBtn.addEventListener('click', () => {
      const banner = document.querySelector('.announcement-banner');
      if (banner) banner.style.display = 'none';
    });
  }
});
