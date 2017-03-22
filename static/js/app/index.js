$(document).ready(function () {
    $(".category-item").hover(function () {
        $(".category-content .category-list li .menu-in").css("display", "none");
        $(".category-content .category-list li").removeClass("hover");
        $(this).addClass("hover");
        $(this).children("div.menu-in").css("display", "block")
    }, function () {
        $(this).removeClass("hover")
        $(this).children("div.menu-in").css("display", "none")
    });
});

$(function () {
    $('.go-top').hide();
    $(window).scroll(function () {
        if ($(window).scrollTop() > 560) {
            $('.go-top').css('display', 'block');
        }
        else {
            $('.go-top').css('display', 'none');
        }
    });
});