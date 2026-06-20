document.addEventListener('click', (event) => {
  const toggle = event.target.closest('.nav-toggle');
  if (!toggle) return;
  const nav = document.getElementById(toggle.getAttribute('aria-controls'));
  if (!nav) return;
  const open = nav.classList.toggle('is-open');
  toggle.setAttribute('aria-expanded', String(open));
});

// Animated terminal — stream lines one by one, auto-scroll, then loop
(function() {
  const term = document.getElementById('terminal-stream');
  if (!term) return;
  const lines = [...term.querySelectorAll('.term-line')];
  lines.forEach(l => l.classList.remove('visible'));
  let idx = 0;
  function next() {
    if (idx < lines.length) {
      lines[idx].classList.add('visible');
      // Auto-scroll: keep the latest line visible
      const body = term.parentElement;
      body.scrollTop = body.scrollHeight;
      idx++;
      const cur = lines[idx - 1];
      // Commands: slightly slower (typing feel), output: faster
      const delay = cur.querySelector('.t-prompt') ? 400 + Math.random() * 300 : 180 + Math.random() * 120;
      setTimeout(next, delay);
    } else {
      // Pause, then reset and loop
      setTimeout(() => {
        lines.forEach(l => l.classList.remove('visible'));
        idx = 0;
        term.parentElement.scrollTop = 0;
        setTimeout(next, 400);
      }, 6000);
    }
  }
  setTimeout(next, 800);
})();
