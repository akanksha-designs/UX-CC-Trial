// Fade-in sections on scroll
const observer = new IntersectionObserver(
  (entries) => entries.forEach(e => e.target.classList.toggle('visible', e.isIntersecting)),
  { threshold: 0.1 }
);

document.querySelectorAll('.card, .about-inner, .hero').forEach(el => {
  el.classList.add('fade-target');
  observer.observe(el);
});
