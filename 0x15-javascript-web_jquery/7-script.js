/**
 * Script that fetches the character 'name' from
 * url:'https://swapi-api.alx-tools.com/api/people/5/?format=json'
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  success: function (data) {
    $('DIV#character').text(data.name);
  }
});
