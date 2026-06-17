/* ═══════════════════════════════════════════════════════════
   SMJED motion — scroll reveal, staggered children, stat count-up.
   Zero dependencies. Fully no-op under prefers-reduced-motion.
   ═══════════════════════════════════════════════════════════ */
(function () {
    "use strict";

    var reduceMotion = window.matchMedia &&
        window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var hasIO = "IntersectionObserver" in window;

    // ─── Reveal: fade/slide sections in on scroll ──────────────
    var revealEls = document.querySelectorAll("[data-reveal]");

    function show(el) { el.classList.add("is-visible"); }

    if (reduceMotion || !hasIO) {
        for (var i = 0; i < revealEls.length; i++) show(revealEls[i]);
        revealChildren();
    } else {
        var revealObserver = new IntersectionObserver(function (entries, obs) {
            for (var i = 0; i < entries.length; i++) {
                if (entries[i].isIntersecting) {
                    show(entries[i].target);
                    obs.unobserve(entries[i].target);
                }
            }
        }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

        for (var j = 0; j < revealEls.length; j++) revealObserver.observe(revealEls[j]);
        revealChildren();
    }

    // ─── Staggered children: animate cards/items one by one ───
    // Containers marked [data-reveal-stagger] reveal their direct
    // children in sequence when the container enters the viewport.
    function revealChildren() {
        var groups = document.querySelectorAll("[data-reveal-stagger]");
        if (!groups.length) return;

        function staggerIn(group) {
            var kids = group.children;
            for (var i = 0; i < kids.length; i++) {
                kids[i].style.transitionDelay = (i * 90) + "ms";
                kids[i].classList.add("is-visible");
            }
        }

        if (reduceMotion || !hasIO) {
            for (var i = 0; i < groups.length; i++) staggerIn(groups[i]);
            return;
        }

        var groupObserver = new IntersectionObserver(function (entries, obs) {
            for (var i = 0; i < entries.length; i++) {
                if (entries[i].isIntersecting) {
                    staggerIn(entries[i].target);
                    obs.unobserve(entries[i].target);
                }
            }
        }, { rootMargin: "0px 0px -8% 0px", threshold: 0.1 });

        for (var k = 0; k < groups.length; k++) groupObserver.observe(groups[k]);
    }

    // ─── Count-up: animate numeric stats when they enter view ──
    var countEls = document.querySelectorAll("[data-countup]");

    function formatValue(value) {
        return (Math.round(value * 10) / 10).toString();
    }

    function runCount(el) {
        var target = parseFloat(el.getAttribute("data-target"));
        if (isNaN(target)) return;

        if (reduceMotion) { el.textContent = formatValue(target); return; }

        var duration = 1100;
        var start = null;

        function tick(timestamp) {
            if (start === null) start = timestamp;
            var progress = Math.min((timestamp - start) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3); // easeOutCubic
            el.textContent = formatValue(target * eased);
            if (progress < 1) window.requestAnimationFrame(tick);
            else el.textContent = formatValue(target);
        }
        window.requestAnimationFrame(tick);
    }

    if (countEls.length) {
        if (reduceMotion || !hasIO) {
            for (var k = 0; k < countEls.length; k++) runCount(countEls[k]);
        } else {
            var countObserver = new IntersectionObserver(function (entries, obs) {
                for (var i = 0; i < entries.length; i++) {
                    if (entries[i].isIntersecting) {
                        runCount(entries[i].target);
                        obs.unobserve(entries[i].target);
                    }
                }
            }, { threshold: 0.5 });
            for (var m = 0; m < countEls.length; m++) countObserver.observe(countEls[m]);
        }
    }

    // ─── Availability border-light: drive the conic gradient angle ──
    // The @property CSS animation can stall under reduced-motion
    // duration clamps, so we drive --avail-angle via rAF instead.
    // It's a gentle in-place glow (nothing displaces), safe to run.
    var pill = document.querySelector(".landing .hero .availability");
    if (pill && window.requestAnimationFrame) {
        var angle = 0;
        // ~one full rotation every 4s → 360deg / 4000ms * 16ms ≈ 1.44deg/frame
        var step = 1.44;
        function spin() {
            angle = (angle + step) % 360;
            pill.style.setProperty("--avail-angle", angle + "deg");
            window.requestAnimationFrame(spin);
        }
        window.requestAnimationFrame(spin);
    }
})();
