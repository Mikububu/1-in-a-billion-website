document.addEventListener('DOMContentLoaded', () => {
    // Scroll Animation Observer for fading in elements
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animElements = document.querySelectorAll('.fade-in-up');
    animElements.forEach(el => scrollObserver.observe(el));
});

/* =========================================================================
   GLOBAL NAVIGATION SCROLL BEHAVIOR
   ========================================================================= */
let lastScroll = 0;
const globalNav = document.getElementById('globalNav');

window.addEventListener('scroll', () => {
    if (!globalNav) return;
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
        globalNav.classList.remove('scrolled-down');
    }

    if (currentScroll > lastScroll && currentScroll > 70) {
        // Scroll down - hide nav
        globalNav.classList.add('scrolled-down');
    } else if (currentScroll < lastScroll) {
        // Scroll up - show nav
        globalNav.classList.remove('scrolled-down');
    }

    lastScroll = currentScroll;
});
