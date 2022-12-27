$(document).ready(function () {
  $('#update_header').click(function (e) {
    e.preventDefault();
    $('header').html('New Header!!!');
  });
});
