/**
 * Created by Artur on 09.05.17.
 */

var $window = $(window),
    $document = $(document),
    $htmlBody = $('html,body'),
    $body = $('body'),
    $header = $('header'),
    winWidth,
    winHeight,
    docHeight,
    headerHeight;

function responsive() {
    winWidth = $window.width();
    winHeight = window.innerHeight ? window.innerHeight : $window.height();
    docHeight = $document.height();
    headerHeight = $header.height();
}

// scrolling behaviors need landing pos and scrolling pos,
// so let's wrap a function to use it in both places
var scrollPos,
    secTopPos,
    secHeight,
    secBot,
    secBotPos;
var offset = 20;

function scrolling() {

    scrollPos = $window.scrollTop();
    // console.log(scrollPos);
    // define animations for each section based on scrolling positions

    var $section_snap = $('.section-snap');

    if ($section_snap.length) {
        $section_snap.each(function () {
            secTopPos = $(this).offset().top;
            secHeight = $(this).innerHeight();
            secBot = secTopPos + secHeight;
            secBotPos = secBot - winHeight;

            if (scrollPos >= secBotPos + offset) { // define end-of-scroll point first

                if (winWidth >= 930) { // 930 is break from 1 to 2 column
                    $(this).addClass('bottom').removeClass('fixed');
                } else {
                    $(this).removeClass('fixed bottom');
                }

            } else if (scrollPos < secBotPos + offset) { // define begin-of-scroll next

                if (winWidth >= 930) { // 930 is break from 1 to 2 column
                    $(this).addClass('fixed').removeClass('bottom');
                } else {
                    $(this).removeClass('fixed bottom');
                }
            } else { // define pre-scroll-to resets last
                $(this).removeClass('fixed bottom');
            }
        });
    }
}

$document.ready(function () {

    // initialize things
    responsive();

    // initial landing position
    scrolling();

    // move based on scroll position
    $window.on('scroll', function () {
        scrolling();
    });

    // run again on resize
    $window.on('resize', function () {
        responsive();
    });
});