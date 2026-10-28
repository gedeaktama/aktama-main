import './bootstrap';
import 'bootstrap';

document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Navbar Dynamic Glassmorphism on Scroll
    const navbar = document.querySelector('.navbar.sticky-top');
    if (navbar) {
        let isScrolled = false;
        const updateNavbar = () => {
            const shouldBeScrolled = window.scrollY > 20;
            if (shouldBeScrolled !== isScrolled) {
                isScrolled = shouldBeScrolled;
                navbar.classList.toggle('navbar-scrolled', isScrolled);
            }
        };
        window.addEventListener('scroll', updateNavbar, { passive: true });
        updateNavbar();
    }

    // 2. High-Performance IntersectionObserver for Scroll Animations
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -40px 0px',
            threshold: 0.1
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-revealed');
                    observer.unobserve(entry.target); // Unobserve to free CPU/GPU resources
                }
            });
        }, observerOptions);

        // Target cards, headers, features, and explicit animation classes
        const animatedTargets = document.querySelectorAll(
            '.reveal-on-scroll, [data-animate], .card-feature, .hover-lift, section > .container > .text-center'
        );

        animatedTargets.forEach(el => {
            el.classList.add('reveal-init');

            // Stagger animations for elements inside grid columns
            const col = el.closest('.col-md-6, .col-lg-4, .col-md-4, .col-lg-3, .col-sm-6');
            if (col && col.parentElement) {
                const siblings = Array.from(col.parentElement.children);
                const colIndex = siblings.indexOf(col);
                if (colIndex > 0) {
                    el.style.transitionDelay = `${(colIndex % 4) * 100}ms`;
                }
            }

            revealObserver.observe(el);
        });
    } else {
        // Fallback for browsers without IntersectionObserver support
        document.querySelectorAll('.reveal-on-scroll, [data-animate], .card-feature, .hover-lift').forEach(el => {
            el.classList.add('is-revealed');
        });
    }

    // 3. Smooth offset scrolling for internal section anchors
    document.querySelectorAll('a[href^="#"]:not([href="#"]):not([data-bs-toggle])').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (!targetId || targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const navOffset = navbar ? navbar.offsetHeight : 70;
                const elementPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
                window.scrollTo({
                    top: Math.max(0, elementPosition - navOffset - 16),
                    behavior: 'smooth'
                });
            }
        });
    });
});
