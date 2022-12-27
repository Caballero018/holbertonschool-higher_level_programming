const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (datas, textStatus, jqXHR) {
  for (data of datas.results) $('#list_movies').append('<li>' + data.title + '</li>');
});
