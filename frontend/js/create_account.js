async function validateLoginForm() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch('/api/create_account', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });

        const result = await response.text();

        if (response.ok) {
            alert("Account Created Successfully");
            window.location.href = "home.html";
        } else {
            alert("Account Creation Failed: " + result);
        }
    } catch (error) {
        console.error("Error: ", error);
        alert("Creation Failed");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", (event) => {
            event.preventDefault();
            validateLoginForm();
        });
    }
});