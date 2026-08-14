const detailsField = document.querySelector('#detalhes');

function resizeDetailsField() {
  detailsField.style.height = 'auto';
  detailsField.style.height = `${detailsField.scrollHeight}px`;
}

detailsField.addEventListener('input', resizeDetailsField);
resizeDetailsField();
