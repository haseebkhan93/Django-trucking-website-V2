function toggleMenu() {
  const menu = document.getElementById("navbarMenu");
  menu.classList.toggle("active");
}

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


document.addEventListener("DOMContentLoaded", function () {
  if (window.innerWidth <= 768) {
    const teamCards = document.querySelectorAll(".team-card");

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // Remove effect from all other cards
            teamCards.forEach(card => card.classList.remove("hover-effect"));
            // Add effect to current visible card
            entry.target.classList.add("hover-effect");
          }
        });
      },
      {
        threshold: 1.0, // You can tweak this if needed
      }
    );

    teamCards.forEach((card) => observer.observe(card));
  }
});
