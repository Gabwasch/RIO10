export default function validation() {
    'use strict';

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');
    const btn = document.getElementById('btn');

    // Function to handle form submission
    function handleFormSubmission(event) {
        const form = event.currentTarget;

        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        } else {
            // Validation passed, redirect to another page
            window.location.href = "./cadastroAtributos.html";
        }

        form.classList.add('was-validated');
    }

    // Loop over forms and attach event listeners
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', handleFormSubmission, false);
    });

    // Optional: If you also want to trigger the validation on button click
    btn.addEventListener('click', () => {
        const activeForm = document.querySelector('.needs-validation');
        activeForm.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
    });
}
