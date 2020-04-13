/* eslint-disable space-before-blocks */

/* JQuery */
// eslint-disable-next-line no-undef
$(function () {
  // eslint-disable-next-line no-undef
  $(window).scroll(function () {
    // eslint-disable-next-line no-undef
    if ($(this).scrollTop() > 390) {
      // eslint-disable-next-line no-undef
      $('.bar').css('background-color', '#232323')
    } else {
      // eslint-disable-next-line no-undef
      $('.bar').css('background-color', '#F2F2F2')
    }
  })

  // eslint-disable-next-line no-undef
  $('.modal-trigger').click(function (e) {
    e.preventDefault()
    // eslint-disable-next-line no-undef
    dataModal = $(this).attr('data-modal')
    // eslint-disable-next-line no-undef
    $('#' + dataModal).css({ 'display': 'block' })
    // $("body").css({"overflow-y": "hidden"}); //Prevent double scrollbar.
  })

  // eslint-disable-next-line no-undef
  $('.close-modal, .modal-sandbox').click(function () {
    // eslint-disable-next-line no-undef
    $('.modal').css({ 'display': 'none' })
    // $("body").css({"overflow-y": "auto"}); //Prevent double scrollbar.
  })
})

/*
  CODIGO ORIGINAL Tom Michew
  -> https://medium.com/wdstack/bootstrap-4-custom-carousel-94a537364fde
  EDITADO POR MIM -> BED
*/
// eslint-disable-next-line no-undef
$('#carouselExample').on('slide.bs.carousel', function (e) {
  // eslint-disable-next-line no-undef
  var $e = $(e.relatedTarget)
  var idx = $e.index()
  var itemsPerSlide = 4
  // eslint-disable-next-line no-undef
  var totalItems = $('.carousel-item').length

  if (idx >= totalItems - (itemsPerSlide - 1)) {
    var it = itemsPerSlide - (totalItems - idx)
    for (var i = 0; i < it; i++) {
      // eslint-disable-next-line eqeqeq
      if (e.direction == 'left') {
        // eslint-disable-next-line no-undef
        $('.carousel-item').eq(i).appendTo('.carousel-inner')
      } else {
        // eslint-disable-next-line no-undef
        $('.carousel-item').eq(0).appendTo('.carousel-inner')
      }
    }
  }
})

/* Scroll Suave */
// eslint-disable-next-line no-undef
jQuery(document).ready(function ($){
  // eslint-disable-next-line space-before-blocks
  $('.scroll').click(function (event){
    event.preventDefault()
    $('html,body').animate({ scrollTop: $(this.hash).offset().top }, 600)
  })
})
