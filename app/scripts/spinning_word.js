const spinText = document.querySelector('#spin-text');
const spinningText = document.querySelector('#spinning-text');

spinText.addEventListener('input', () => {
    spinningText.textContent = spinText.value;
});
