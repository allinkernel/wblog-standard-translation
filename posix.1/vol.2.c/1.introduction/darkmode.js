function setTheme(isDark) {
  if (isDark) {
    document.body.classList.add("dark-mode");
    localStorage.setItem("theme", "dark");
  } else {
    document.body.classList.remove("dark-mode");
    localStorage.setItem("theme", "light");
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("themeToggle");

  if (button) {
    button.addEventListener("click", function () {
      const isDark = !document.body.classList.contains("dark-mode");
      setTheme(isDark);
    });
  }

  // Load saved theme
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
  }
});

window.addEventListener("storage", function (event) {
  if (event.key === "theme") {
    if (event.newValue === "dark") {
      document.body.classList.add("dark-mode");
    } else {
      document.body.classList.remove("dark-mode");
    }
  }
});

