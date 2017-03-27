/**
 * Created by zihang on 2017/3/27.
 */
$(document).ready(function () {
    $(".good-evaluate").click(function () {
        $(this).css("background-image","url('/static/images/customer/iconfont-good.png')");
        $(this).siblings(".middle-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");
        $(this).siblings(".bad-evaluate").css("background-image","url('/static/images/customer/iconfont-bad.png')");
    });
    $(".middle-evaluate").click(function () {
        $(this).css("background-image","url('/static/images/customer/iconfont-middle.png')");
        $(this).siblings(".good-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");
        $(this).siblings(".bad-evaluate").css("background-image","url('/static/images/customer/iconfont-bad.png')");
    });
    $(".bad-evaluate").click(function () {
        $(this).css("background-image","url('/static/images/customer/iconfont-badon.png')");
        $(this).siblings(".good-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");
        $(this).siblings(".middle-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");

    });
});