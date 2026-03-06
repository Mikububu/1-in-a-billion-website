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
        // Auto-close mobile menu on scroll down
        if (hamburger && navLinks && hamburger.classList.contains('active')) {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        }
    } else if (currentScroll < lastScroll) {
        // Scroll up - show nav
        globalNav.classList.remove('scrolled-down');
    }

    lastScroll = currentScroll;
});

/* =========================================================================
   HAMBURGER MENU BEHAVIOR
   ========================================================================= */
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!hamburger.contains(e.target) && !navLinks.contains(e.target) && navLinks.classList.contains('active')) {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        }
    });

    // Close menu when clicking a link
    const links = navLinks.querySelectorAll('.nav-link');
    links.forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });
}
