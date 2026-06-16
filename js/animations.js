/* ============================================================
   MS FIRE SOLUTIONS — ANIMATIONS JAVASCRIPT
   Scroll reveal, counters, stagger effects
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Scroll Reveal (Intersection Observer) ─────────────── */
  const revealClasses = ['.reveal', '.reveal-left', '.reveal-right', '.reveal-scale'];
  const revealEls = document.querySelectorAll(revealClasses.join(', '));

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach(el => revealObserver.observe(el));

  /* ── Stagger Children ──────────────────────────────────── */
  document.querySelectorAll('.stagger').forEach(container => {
    const children = Array.from(container.children);
    children.forEach((child, i) => {
      child.classList.add('reveal');
      child.style.transitionDelay = `${i * 0.1}s`;
      revealObserver.observe(child);
    });
  });

  /* ── Counter Animation ─────────────────────────────────── */
  function animateCounter(el, from, to, duration, suffix = '') {
    const start = performance.now();
    const isFloat = String(to).includes('.');
    const decimals = isFloat ? String(to).split('.')[1].length : 0;

    function update(time) {
      const elapsed = time - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      const current = from + (to - from) * eased;
      el.textContent = isFloat
        ? current.toFixed(decimals) + suffix
        : Math.floor(current) + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseFloat(el.dataset.count);
        const suffix = el.dataset.suffix || '';
        const from   = parseFloat(el.dataset.from  || '0');
        animateCounter(el, from, target, 2000, suffix);
        counterObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-count]').forEach(el => {
    counterObserver.observe(el);
  });

  /* ── Typewriter for Hero Label ─────────────────────────── */
  const typeEl = document.querySelector('[data-typewrite]');
  if (typeEl) {
    const words = typeEl.dataset.typewrite.split(',');
    let wIdx = 0, cIdx = 0, deleting = false;

    function type() {
      const word = words[wIdx];
      if (deleting) {
        typeEl.textContent = word.substring(0, cIdx--);
        if (cIdx < 0) {
          deleting = false;
          wIdx = (wIdx + 1) % words.length;
          setTimeout(type, 400);
          return;
        }
      } else {
        typeEl.textContent = word.substring(0, ++cIdx);
        if (cIdx === word.length) {
          deleting = true;
          setTimeout(type, 2200);
          return;
        }
      }
      setTimeout(type, deleting ? 50 : 90);
    }
    type();
  }

  /* ── Tilt on Service Cards ─────────────────────────────── */
  document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width  - 0.5;
      const y = (e.clientY - rect.top)  / rect.height - 0.5;
      card.style.transform = `translateY(-8px) rotateX(${-y * 6}deg) rotateY(${x * 6}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });

  /* ── Reduced Motion Guard ──────────────────────────────── */
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    revealEls.forEach(el => el.classList.add('visible'));
  }

});
