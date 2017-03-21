/**
 * Created by zihang on 2017/3/20.
 */
$(document).ready(function () {
   $(".user-addresslist").click(function () {
       $(this).addClass("address-selected").siblings().removeClass("address-selected");
   });
    $(".set-default").click(function () {
        $(this).addClass("hidden");
        $(this).parents("li").find(".deftip").removeClass("hidden");
        $(".set-default").not(this).removeClass("hidden");
        $(".set-default").not(this).parents("li").find(".deftip").addClass("hidden");
    });
    $(".delete-address").click(function () {
       $(this).parents("li").css("display","none");
    });
});