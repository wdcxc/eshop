/**
 * Created by zihang on 2017/3/20.
 */
$(document).ready(function () {
   $(".user-addresslist").click(function () {
       $(this).addClass("address-selected").siblings().removeClass("address-selected");
   });
});