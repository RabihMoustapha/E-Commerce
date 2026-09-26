async function validateLoginForm() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    const result = await response.text();

    if (response.ok) {
      alert("Login Successfully");
      window.location.href = "home.html";
    } else {
      alert("Login Failed: " + result);
    }
  } catch (error) {
    console.error("Error: ", error);
    alert("Login Failed");
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