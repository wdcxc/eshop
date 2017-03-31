/**
 * Created by zihang on 2017/3/21.
 */
$(document).ready(function () {
    var image=$(".commodity-image");
    var number=$(".number");
    $(".commodity-list").find("li").click(function () {
        $(this).addClass("image-selected").siblings().removeClass("image-selected");
        image.find("img").attr("src",$(this).find("img").attr("src"));
        image.find("img").attr("alt",$(this).find("img").attr("alt"));
    });
    $(".reduce").attr('disabled',true);
    $(".add").click(function () {
        number.val(parseInt(number.val())+1);
        if(parseInt(number.val())!=1){
            $(".reduce").attr('disabled',false);
        }
    });

    $(".reduce").click(function () {
        number.val(parseInt(number.val())-1);
        if(parseInt(number.val())==1){
           $(".reduce").attr('disabled',true);
       }
    });

    $(".option-list").find("li").click(function(){
		$(".option-list").find("li").css("background-color","#fff");
		$(this).css("background-color","#F5F5F5");
	});
});
