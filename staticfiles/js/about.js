
  document.addEventListener("DOMContentLoaded", () => {
    const paths = document.querySelectorAll("svg path");

    const observer = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            paths.forEach(path => {
              path.style.animationPlayState = "running";
            });
            observer.disconnect(); // Stop observing after animation starts
          }
        });
      },
      {
        root: null,
        threshold: 0.1, // Trigger when 10% of the SVG is visible
      }
    );

    const svgElement = document.querySelector("svg");
    if (svgElement) {
      observer.observe(svgElement);
    }
  });
