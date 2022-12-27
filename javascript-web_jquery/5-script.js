$(document).ready(function () {
  $('#add_item').click(function (e) {
    e.preventDefault();
    $('header').toggleClass('green red');
  });
});
