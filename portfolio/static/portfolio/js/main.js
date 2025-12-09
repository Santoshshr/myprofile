// Moved from template
// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Contact form submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };

        const csrftokenEl = document.querySelector('[name=csrfmiddlewaretoken]');
        const csrftoken = csrftokenEl ? csrftokenEl.value : '';

        try {
            const response = await fetch('/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            const messageDiv = document.getElementById('formMessage');

            if (data.status === 'success') {
                messageDiv.textContent = data.message;
                messageDiv.className = 'form-message success';
                document.getElementById('contactForm').reset();
            } else {
                messageDiv.textContent = data.message;
                messageDiv.className = 'form-message error';
            }

            setTimeout(() => {
                messageDiv.style.display = 'none';
            }, 5000);
        } catch (error) {
            const messageDiv = document.getElementById('formMessage');
            messageDiv.textContent = 'An error occurred. Please try again.';
            messageDiv.className = 'form-message error';
        }
    });
}
