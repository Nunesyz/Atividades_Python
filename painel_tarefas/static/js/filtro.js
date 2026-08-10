const listaTarefas = document.getElementById('listaTarefas');
const itensFiltro = document.querySelectorAll('[data-status]');

function classeStatus(status) {
    if (status === 'Pendente') return 'tarefa-pendente';
    if (status === 'Em andamento') return 'tarefa-andamento';
    if (status === 'Concluída') return 'tarefa-concluida';
    return '';
}

function renderizarTarefas(tarefas) {
    listaTarefas.innerHTML = '';
    tarefas.forEach(tarefa => {
        const coluna = document.createElement('div');
        coluna.className = 'col-md-4';
        coluna.innerHTML = `
            <div class="card ${classeStatus(tarefa.status)}">
                <div class="card-body">
                    <h5 class="card-title">${tarefa.titulo}</h5>
                    <p class="card-text">${tarefa.descricao ?? ''}</p>
                    <span class="badge bg-secondary">${tarefa.status}</span>
                    <div class="mt-3">
                        <a href="/editar/${tarefa.id}" class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i></a>
                        <a href="/concluir/${tarefa.id}" class="btn btn-sm btn-outline-success"><i class="bi bi-check-lg"></i></a>
                        <a href="/excluir/${tarefa.id}" class="btn btn-sm btn-outline-danger"><i class="bi bi-trash"></i></a>
                    </div>
                </div>
            </div>
        `;
        listaTarefas.appendChild(coluna);
    });
}

itensFiltro.forEach(item => {
    item.addEventListener('click', (evento) => {
        evento.preventDefault();
        const status = item.getAttribute('data-status');
        const url = status === 'todas' ? '/api/tarefas' : `/api/tarefas?status=${encodeURIComponent(status)}`;
        fetch(url)
            .then(resposta => resposta.json())
            .then(dados => renderizarTarefas(dados));
    });
});
