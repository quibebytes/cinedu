const btnConfig = document.getElementById('btnConfig'); // Seu ícone de engrenagem
const modalConfig = document.getElementById('modalConfig');
const btnFecharModal = document.getElementById('btnFecharModal');

// Quando clicar na engrenagem, abre o modal
btnConfig.addEventListener('click', () => {
    modalConfig.showModal(); // Função nativa do HTML para abrir o <dialog>
});

// Quando clicar no 'X', fecha o modal
btnFecharModal.addEventListener('click', () => {
    modalConfig.close(); // Função nativa do HTML para fechar o <dialog>
});

// Opcional: Fecha se clicar do lado de fora do modal
modalConfig.addEventListener('click', (e) => {
    const dialogDimensions = modalConfig.getBoundingClientRect();
    if (
        e.clientX < dialogDimensions.left ||
        e.clientX > dialogDimensions.right ||
        e.clientY < dialogDimensions.top ||
        e.clientY > dialogDimensions.bottom
    ) {
        modalConfig.close();
    }
});