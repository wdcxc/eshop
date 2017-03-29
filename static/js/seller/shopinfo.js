/**
 * Created by zihang on 2017/3/28.
 */
$(document).ready(function () {
   $(".shop-addresslist").click(function () {
       $(this).addClass("shop-selected").siblings().removeClass("shop-selected");
   });
    $(".set-default").click(function () {
        $(this).addClass("hidden");
        $(this).parents("li").find(".deftip").removeClass("hidden");
        $(".set-default").not(this).removeClass("hidden");
        $(".set-default").not(this).parents("li").find(".deftip").addClass("hidden");
    });
    $(".delete-shop").click(function () {
       $(this).parents("li").css("display","none");
    });
});
