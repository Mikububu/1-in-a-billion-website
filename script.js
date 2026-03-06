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
