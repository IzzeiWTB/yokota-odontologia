document.addEventListener("DOMContentLoaded", function () {
  var form = document.querySelector(".form");

  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      alert("Pedido de agendamento enviado. Substitua por uma integração real.");
      form.reset();
    });
  }
});
