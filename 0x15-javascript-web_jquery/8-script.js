/**
 * Script that fetches and lists the 'title' for all movies
 * from a specified URL
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (data) {
    const movieList = $('UL#list_movies');
    for (const film of data.results) {
      movieList.append(`<li>${film.title}</li>`);
    }
  }
});
