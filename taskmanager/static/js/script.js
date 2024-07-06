document.addEventListener('DOMContentLoaded', function() {
  // sidenav initialisation
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);
});

document.addEventListener('DOMContentLoaded', function() {
  // date picker initialisation
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmmm yyyy",
    i18n: {done: "Select"}
  });
});

document.addEventListener('DOMContentLoaded', function() {
  // select initialisation
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);
});

document.addEventListener('DOMContentLoaded', function() {
  // collapsible initialisation
  let collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);
});