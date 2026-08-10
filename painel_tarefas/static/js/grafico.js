fetch('/api/progresso')
    .then(resposta => resposta.json())
    .then(dados => {
        const ctx = document.getElementById('graficoStatus');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Pendente', 'Em andamento', 'Concluída'],
                datasets: [{
                    data: [dados.pendente, dados.andamento, dados.concluida],
                    backgroundColor: ['#ffc107', '#0d6efd', '#198754']
                }]
            }
        });
    });
