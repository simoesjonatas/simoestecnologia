(function () {
    const header = document.querySelector("[data-header]");
    const navToggle = document.querySelector("[data-nav-toggle]");
    const navPanel = document.querySelector("[data-nav-panel]");

    function syncHeader() {
        if (!header) return;
        header.classList.toggle("is-scrolled", window.scrollY > 24);
    }

    function closeMenu() {
        if (!navToggle || !navPanel || !header) return;
        navToggle.setAttribute("aria-expanded", "false");
        navPanel.classList.remove("is-open");
        header.classList.remove("nav-active");
        document.body.classList.remove("nav-open");
    }

    if (header) {
        syncHeader();
        window.addEventListener("scroll", syncHeader, { passive: true });
    }

    if (navToggle && navPanel && header) {
        navToggle.addEventListener("click", function () {
            const isOpen = navToggle.getAttribute("aria-expanded") === "true";
            navToggle.setAttribute("aria-expanded", String(!isOpen));
            navPanel.classList.toggle("is-open", !isOpen);
            header.classList.toggle("nav-active", !isOpen);
            document.body.classList.toggle("nav-open", !isOpen);
        });

        navPanel.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", closeMenu);
        });

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") closeMenu();
        });
    }

    const revealItems = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.14 }
        );

        revealItems.forEach(function (item) {
            observer.observe(item);
        });
    } else {
        revealItems.forEach(function (item) {
            item.classList.add("is-visible");
        });
    }

    const contactForm = document.querySelector("[data-contact-form]");
    if (!contactForm) return;

    const submitButton = contactForm.querySelector("[data-submit-button]");
    const messages = {
        name: "Informe seu nome.",
        organization: "Informe a empresa ou organização.",
        email: "Informe um e-mail válido.",
        whatsapp: "Informe um WhatsApp para contato.",
        solution_type: "Escolha o tipo de solução.",
        message: "Conte brevemente o que você precisa resolver.",
    };

    function clearClientErrors() {
        contactForm.querySelectorAll("[data-client-error]").forEach(function (error) {
            error.remove();
        });
        contactForm.querySelectorAll(".has-error").forEach(function (field) {
            field.classList.remove("has-error");
        });
        contactForm.querySelectorAll("[aria-invalid='true']").forEach(function (input) {
            input.removeAttribute("aria-invalid");
        });
    }

    function addFieldError(input, message) {
        const field = input.closest(".field");
        if (!field) return;
        const error = document.createElement("p");
        const id = input.id ? input.id + "-client-error" : "client-error-" + Date.now();
        error.className = "field-error";
        error.id = id;
        error.textContent = message;
        error.setAttribute("data-client-error", "true");
        field.appendChild(error);
        field.classList.add("has-error");
        input.setAttribute("aria-invalid", "true");
        input.setAttribute("aria-describedby", id);
    }

    function isValidEmail(value) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }

    contactForm.addEventListener("submit", function (event) {
        clearClientErrors();

        const website = contactForm.querySelector("input[name='website']");
        if (website && website.value.trim()) {
            event.preventDefault();
            return;
        }

        let firstInvalid = null;
        contactForm.querySelectorAll("[required]").forEach(function (input) {
            const value = input.value.trim();
            let errorMessage = "";

            if (!value) {
                errorMessage = messages[input.name] || "Preencha este campo.";
            } else if (input.type === "email" && !isValidEmail(value)) {
                errorMessage = messages.email;
            }

            if (errorMessage) {
                addFieldError(input, errorMessage);
                if (!firstInvalid) firstInvalid = input;
            }
        });

        const lastSubmit = Number(window.sessionStorage.getItem("simoes-contact-submit") || 0);
        if (!firstInvalid && Date.now() - lastSubmit < 25000) {
            event.preventDefault();
            const message = document.createElement("div");
            message.className = "form-alert";
            message.setAttribute("role", "alert");
            message.setAttribute("data-client-error", "true");
            message.innerHTML = "<p>Aguarde alguns segundos antes de enviar uma nova mensagem.</p>";
            contactForm.prepend(message);
            return;
        }

        if (firstInvalid) {
            event.preventDefault();
            firstInvalid.focus();
            return;
        }

        window.sessionStorage.setItem("simoes-contact-submit", String(Date.now()));
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.textContent = submitButton.dataset.loadingText || "Enviando...";
        }
    });
})();
