async function validateLoginForm() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch('api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application-json'
      },
      body: JSON.stringify({ email, password })
    });

    const result = await response.json();

    if (result.success) {
      alert("Login Successfully");
      window.location.href = "home.html"
    } else {
      alert("Login Failed");
    }
  } catch {
    console.error("Error: ", error);
  }
}