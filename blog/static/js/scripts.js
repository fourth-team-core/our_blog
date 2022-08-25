// Just a little bit of JS for the clicks.
// Everything else is CSS.
// Could be 100% CSS.

$(function(){
  $('.like-toggle').click(function(){
    $(this).toggleClass('like-active');
    $(this).next().toggleClass('hidden');
  });
});