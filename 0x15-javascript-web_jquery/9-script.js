/**
 * Script fetches from a URL and displays the value of
 * 'hello' from that fetch in the HTML tag 'DIV#hello'
 */
$(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
