const botaoModoEscuro = document.getElementById('botaoModoEscuro');

function aplicarModoEscuro(ativo) {
    if (ativo) {
        document.body.classList.add('modo-escuro');
    } else {
        document.body.classList.remove('modo-escuro');
    }
}

const modoSalvo = localStorage.getItem('modoEscuro') === 'true';
aplicarModoEscuro(modoSalvo);

if (botaoModoEscuro) {
    botaoModoEscuro.addEventListener('click', () => {
        const ativo = !document.body.classList.contains('modo-escuro');
        aplicarModoEscuro(ativo);
        localStorage.setItem('modoEscuro', ativo);
    });
}
