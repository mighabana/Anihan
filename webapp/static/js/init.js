
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.parallax');
  var instances = M.Parallax.init(elems);

  var sel = document.querySelectorAll('select');
  var sel_instances = M.FormSelect.init(sel);

  var mod = document.querySelectorAll('.modal');
  var mod_instances = M.Modal.init(mod);
});


  