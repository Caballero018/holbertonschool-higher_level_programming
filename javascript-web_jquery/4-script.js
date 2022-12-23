$(document).ready(function () {
  $('#toggle_header').click(function (e) {
    e.preventDefault();
    $('header').toggleClass('green red');
  });
});
