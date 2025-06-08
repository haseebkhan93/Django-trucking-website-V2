function toggleMenu() {
  const menu = document.getElementById("navbarMenu");
  menu.classList.toggle("active");
}


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


document.addEventListener("DOMContentLoaded", function () {
  if (window.innerWidth <= 768) {
    const serviceItems = document.querySelectorAll(".service-item");

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // Remove hover-effect from all other items
            serviceItems.forEach(item => item.classList.remove("hover-effect"));
            // Add hover-effect to the currently visible one
            entry.target.classList.add("hover-effect");
          }
        });
      },
      {
        threshold: 1.0, // Adjust this if you want more or less of the item to be visible before triggering
      }
    );

    serviceItems.forEach((item) => observer.observe(item));
  }
});


document.addEventListener("DOMContentLoaded", function () {
  if (window.innerWidth <= 768) {
    const driverItems = document.querySelectorAll(".driver-item");

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // Remove hover-effect from all other driver-items
            driverItems.forEach(item => item.classList.remove("hover-effect"));
            // Add hover-effect to the currently visible one
            entry.target.classList.add("hover-effect");
          }
        });
      },
      {
        threshold: 1.0, // Adjust sensitivity as needed
      }
    );

    driverItems.forEach((item) => observer.observe(item));
  }
});





function toggleChat() {
  const chatbot = document.getElementById("chatbot");
  chatbot.style.display = chatbot.style.display === "flex" ? "none" : "flex";
}

// Show price calculator option
function showCalculator() {
  const content = document.getElementById("chat-content");
  content.innerHTML = `
    <h5>📦 Load Price Calculator</h5>
    <input type="number" id="distance" placeholder="Distance (miles)">
    <input type="number" id="weight" placeholder="Weight (lbs)">
    <button onclick="calculatePrice()">Calculate</button>
    <div id="price-result" style="margin-top:10px;"></div>
  `;
}


// Show FAQ option
function showFAQ() {
  const content = document.getElementById("chat-content");
  content.innerHTML = `
    <h5>❓ Frequently Asked Questions</h5>
    <ul>
      <li><strong>Q:</strong> How long does delivery take?<br><em>A:</em> It usually takes 2-5 days depending on distance.</li>
      <li><strong>Q:</strong> Can I track my load?<br><em>A:</em> Yes, via your account dashboard.</li>
      <li><strong>Q:</strong> How do I contact support?<br><em>A:</em> Email us at support@example.com</li>
    </ul>
  `;
}


function toggleChat() {
  const chatbot = document.getElementById("chatbot");
  chatbot.style.display = chatbot.style.display === "flex" ? "none" : "flex";
}

// Load Price Calculator form
function showCalculator() {
  const content = document.getElementById("chat-content");
  content.innerHTML = `
    <h5>📦 Load Price Calculator</h5>
    <input type="number" id="distance" placeholder="Distance (miles)">
    <input type="number" id="weight" placeholder="Weight (lbs)">
    <button onclick="calculatePrice()">Calculate</button>
    <div id="price-result" style="margin-top:10px;"></div>
  `;
}

// Load FAQs
function showFAQ() {
  const content = document.getElementById("chat-content");
  content.innerHTML = `
    <h5>❓ FAQs</h5>
    <ul>
      <li><strong>Q:</strong> How long does delivery take?<br><em>A:</em> 1-3 days based on location.</li>
      <li><strong>Q:</strong> Can I track my shipment?<br><em>A:</em> Yes — via SMS & email notifications.</li>
      <li><strong>Q:</strong> How is pricing calculated?<br><em>A:</em> Based on distance and load weight.</li>
    </ul>
  `;
}


function calculatePrice() {
  const distance = document.getElementById("distance").value;
  const weight = document.getElementById("weight").value;
  const pricePerMile = 5;
  const pricePerLb = 2;

  const resultDiv = document.getElementById("price-result");

  if (distance && weight) {
    const total = (distance * pricePerMile) + (weight * pricePerLb);
    resultDiv.innerHTML = `<strong>Total Price:</strong> $${total.toFixed(2)} (for ${distance} miles, ${weight} lbs)`;
  } else {
    resultDiv.innerHTML = `<span style="color:#f87171;">Please enter both values.</span>`;
  }
}

