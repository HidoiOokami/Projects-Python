
/* JAVASCRIPT */
var debounce = function (func, wait, immediate) {
  let timeout
  return function (...args) {
    const context = this
    const later = function () {
      timeout = null
      if (!immediate) func.apply(context, args)
    }
    const callNow = immediate && !timeout
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
    if (callNow) func.apply(context, args)
  }
}
var target = document.querySelectorAll('[data-anime]')
var animationClass = 'animate'
function animeScroll () {
  var windowTop = window.pageYOffset + (window.innerHeight * 0.75)
  target.forEach((element) => {
    if (windowTop > element.offsetTop) {
      element.classList.add(animationClass)
    } else {
      element.classList.remove(animationClass)
    }
  })
}
animeScroll()
var handleScroll = debounce(animeScroll, 200)

if (target.length) window.addEventListener('scroll', handleScroll)
