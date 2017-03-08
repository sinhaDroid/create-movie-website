// Pause the video when the card is closed
$(document).on('click', '.close, .modal-backdrop, .modal', function (event) {
  $("#trailer-video-container").empty();
});

// Animate in the movies when the page loads
$(document).ready(function () {
  $('.card').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.card', function (event) {
  var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
  var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
  $("#trailer-video-container").empty().append($("<iframe></iframe>", {
    'id': 'trailer-video',
    'type': 'text-html',
    'src': sourceUrl,
    'frameborder': 0
  }));
});