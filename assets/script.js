/*=========================================================
LIAN ENGENHARIA — SCRIPT.JS
=========================================================*/

/*========================================
HEADER (efeito ao rolar a página)
========================================*/

const header = document.querySelector("header");

window.addEventListener("scroll", () => {
    if (window.scrollY > 60) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});

/*========================================
MENU MOBILE
========================================*/

const menuToggle = document.querySelector(".menu-toggle");
const nav = document.querySelector("nav");

menuToggle?.addEventListener("click", () => {
    const isActive = nav.classList.toggle("active");
    menuToggle.classList.toggle("active", isActive);
    menuToggle.setAttribute("aria-expanded", isActive ? "true" : "false");
});

/*========================================
MENU: SCROLL SUAVE E FECHAMENTO NO MOBILE
========================================*/

document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener("click", (e) => {
        const href = link.getAttribute("href");

        if (href.startsWith("#")) {
            e.preventDefault();
            const target = document.querySelector(href);

            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        }

        nav?.classList.remove("active");
        menuToggle?.classList.remove("active");
        menuToggle?.setAttribute("aria-expanded", "false");
    });
});

/*========================================
REVELAÇÃO DE SEÇÕES AO ROLAR
========================================*/

const reveals = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("active");
            revealObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: .15
});

reveals.forEach(section => {
    revealObserver.observe(section);
});

/*========================================
BARRA DE PROGRESSO DE LEITURA
========================================*/

const progress = document.querySelector(".progress-bar");

window.addEventListener("scroll", () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progressWidth = totalHeight > 0 ? (window.pageYOffset / totalHeight) * 100 : 0;

    if (progress) {
        progress.style.width = progressWidth + "%";
    }
});

/*========================================
ANO DINÂMICO NO RODAPÉ
========================================*/

const anoEl = document.getElementById("ano");
if (anoEl) {
    anoEl.textContent = new Date().getFullYear();
}
