document.addEventListener('DOMContentLoaded', function(){
  var form = document.querySelector('.form');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      alert('Pedido de agendamento enviado. Substitua com integração real.');
      form.reset();
    });
  }
});
