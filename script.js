// Você pode adicionar scripts JavaScript aqui para interatividade.
console.log("Script carregado com sucesso!");
// Adiciona um evento que será executado quando a página for carregada
document.addEventListener('DOMContentLoaded', () => {
    alert('Bem-vindo ao meu portfólio!');
});
document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('myButton');
    const message = document.getElementById('message');

    button.addEventListener('click', () => {
        message.textContent = 'Você clicou no botão!';
    });
});
