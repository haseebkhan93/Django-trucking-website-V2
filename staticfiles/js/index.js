document.addEventListener('DOMContentLoaded', () => {
  // ========== NAVBAR ========== //
  const hamburger = document.getElementById('hamburger');
  const navbar = document.getElementById('navbar');

  if (hamburger && navbar) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navbar.classList.toggle('show');
    });
  }

  // ========== SLIDER ========== //
  const slides = document.querySelectorAll('.slider-img');
  let currentIndex = 0;
  let slideInterval;
  const intervalTime = 8000;

  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === index);
    });
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    showSlide(currentIndex);
  }

  function startSlider() {
    slideInterval = setInterval(nextSlide, intervalTime);
  }

  function stopSlider() {
    clearInterval(slideInterval);
  }

  if (slides.length > 0) {
    showSlide(currentIndex);
    startSlider();

    slides.forEach(slide => {
      slide.addEventListener('mouseenter', stopSlider);
      slide.addEventListener('mouseleave', startSlider);
    });

    const sliderContainer = document.querySelector('.slider-container');
    if (sliderContainer) {
      const prevBtn = document.createElement('button');
      const nextBtn = document.createElement('button');

      prevBtn.textContent = '‹';
      nextBtn.textContent = '›';

      prevBtn.className = 'slider-nav slider-prev';
      nextBtn.className = 'slider-nav slider-next';

      sliderContainer.appendChild(prevBtn);
      sliderContainer.appendChild(nextBtn);

      prevBtn.addEventListener('click', () => {
        prevSlide();
        stopSlider();
        startSlider();
      });

      nextBtn.addEventListener('click', () => {
        nextSlide();
        stopSlider();
        startSlider();
      });
    }
  }

  // ========== FORM TOGGLING ========== //
  const bookBtn = document.getElementById('bookTruckBtn');
  const contactBtn = document.getElementById('contactUsBtn');
  const bookForm = document.getElementById('bookTruckForm');
  const contactForm = document.getElementById('contactUsForm');

  if (bookBtn && contactBtn && bookForm && contactForm) {
    // Hide both forms first
    bookForm.style.display = 'none';
    contactForm.style.display = 'none';

    // Add button listeners
    bookBtn.addEventListener('click', () => {
      bookForm.style.display = 'block';
      contactForm.style.display = 'none';
    });

    contactBtn.addEventListener('click', () => {
      bookForm.style.display = 'none';
      contactForm.style.display = 'block';
    });

    // Show default form
    bookForm.style.display = 'block';
  }
});
