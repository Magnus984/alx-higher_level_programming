/**
 * Updates the text color of the <header> element to red
 * when the user clicks on the tag 'DIV#red_header'
 */
$('DIV#red_header').bind('click', function () {
  $('header').attr('style', 'color: #FF0000');
});
