/* ============================================================
   MS FIRE SOLUTIONS — MAIN JAVASCRIPT
   Navigation, accordion, interactions
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Navbar Scroll Behavior ────────────────────────────── */
  const nav = document.querySelector('.nav');
  const scrollThreshold = 80;

  function handleNavScroll() {
    if (window.scrollY > scrollThreshold) {
      nav?.classList.add('scrolled');
    } else {
      nav?.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleNavScroll, { passive: true });
  handleNavScroll();

  /* ── Mobile Menu ───────────────────────────────────────── */
  const hamburger = document.querySelector('.nav-hamburger');
  const mobileMenu = document.querySelector('.nav-mobile');

  hamburger?.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileMenu?.classList.toggle('open');
    document.body.style.overflow =
      mobileMenu?.classList.contains('open') ? 'hidden' : '';
  });

  document.querySelectorAll('.nav-mobile a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger?.classList.remove('open');
      mobileMenu?.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  /* ── Active Nav Link ───────────────────────────────────── */
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .nav-mobile a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* ── Smooth Scroll ─────────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const navH = parseInt(getComputedStyle(document.documentElement)
          .getPropertyValue('--nav-height')) || 80;
        const top = target.getBoundingClientRect().top + window.scrollY - navH - 20;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ── FAQ Accordion ─────────────────────────────────────── */
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');

      // Close all
      document.querySelectorAll('.faq-item.open').forEach(openItem => {
        openItem.classList.remove('open');
      });

      // Toggle clicked
      if (!isOpen) {
        item.classList.add('open');
      }
    });
  });

  /* ── Hero Background Kenburns ──────────────────────────── */
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    setTimeout(() => heroBg.classList.add('loaded'), 100);
  }

  /* ── Parallax Hero ─────────────────────────────────────── */
  const heroBgs = document.querySelectorAll('.hero-bg, .page-hero-bg');
  function handleParallax() {
    const scrolled = window.scrollY;
    heroBgs.forEach(bg => {
      bg.style.transform = `translateY(${scrolled * 0.35}px)`;
    });
  }
  if (heroBgs.length) {
    window.addEventListener('scroll', handleParallax, { passive: true });
  }

});
