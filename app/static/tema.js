
// Verifica se existe um tema salvo
(function() {
    const temaSalvo = localStorage.getItem("tema");
    document.documentElement.setAttribute("tema", temaSalvo == "claro"? "claro": "escuro");
})();

const botao = document.getElementById("iconeTema");

if (document.documentElement.getAttribute("tema") == "claro") {
    botao.src = SOLCORTADO_CAMINHO;
    localStorage.setItem("tema", "claro");
} else {
    botao.src = SOL_CAMINHO;
    localStorage.setItem("tema", "escuro");
}

botao.addEventListener("click", () => {

    document.documentElement.setAttribute("tema",
        document.documentElement.getAttribute("tema") == "claro"?
        "escuro":
        "claro"
    );

    if (document.documentElement.getAttribute("tema") == "claro") {
        botao.src = SOLCORTADO_CAMINHO;
        localStorage.setItem("tema", "claro");
    } else {
        botao.src = SOL_CAMINHO;
        localStorage.setItem("tema", "escuro");
    }
});
