/**
 * Toggles the class of the <header> element
 * when the user clicks on the tag 'DIV#toggle_header'
 */
$('DIV#toggle_header').bind('click', function () {
  $('header').toggleClass('red green');
});
