// theme-toggle.js — перемикач світла/темна тема з пам'яттю (localStorage)

(function () {
  function applyTheme(isDark) {
    document.documentElement.classList.toggle('dark', isDark);
    var toggle = document.getElementById('theme-toggle-checkbox');
    if (toggle) toggle.checked = isDark;
  }

  function initToggle() {
    var toggle = document.getElementById('theme-toggle-checkbox');
    if (!toggle) return;
    toggle.addEventListener('change', function () {
      var isDark = toggle.checked;
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      applyTheme(isDark);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initToggle);
  } else {
    initToggle();
  }
})();
