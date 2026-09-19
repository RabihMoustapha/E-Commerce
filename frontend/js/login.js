function validateLoginForm() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  if (username === "" || password === "") {
    alert("Please fill in all fields.");
    return false;
  }

  window.location.href = "welcome.html";
  return true;
}