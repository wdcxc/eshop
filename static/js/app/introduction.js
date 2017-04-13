/**
 * Created by zihang on 2017/3/21.
 */
$(document).ready(function () {
    let image=$(".commodity-image");
    let number=$(".number");
    let stock=parseInt($(".stock").text());
    $(".commodity-list").find("li").click(function () {
        $(this).addClass("image-selected").siblings().removeClass("image-selected");
        image.find("img").attr("src",$(this).find("img").attr("src"));
        image.find("img").attr("alt",$(this).find("img").attr("alt"));
    });
    $(".add").click(function () {
        number.val(parseInt(number.val())+1);
        if(parseInt(number.val())!=1){
            $(".reduce").attr('disabled',false);
        }
        if(parseInt(number.val())>=stock){
            $(".add").attr('disabled',true);
        }
    });

    $(".reduce").on('click',function () {
        number.val(parseInt(number.val())-1);
        if(parseInt(number.val())==1){
           $(".reduce").attr('disabled',true);
       };
    });

    $(".option-list").find("li").click(function(){
		$(".option-list").find("li").css("background-color","#fff");
		$(this).css("background-color","#F5F5F5");
	});

	$("#order").on("click",function(){
	    id = $("#id").val();
	    num = $(".number").val();
	    location.href = "/app/common/order?id="+id+"&num="+num;
	});

	$("#shopcart").on("click",function(){
        id = $("#id").val();
	    num = $(".number").val();
	    $.get("/app/common/addShopcart?id="+id+"&num="+num,
	        function(result){
	            alert(result.msg);
	            if(result.code==200){
	                location.href = "/app/common/shopcart";
	            }
	        }
	    );
	    return false;
	});

	$("#buynow").on("click",function(){
        id = $("#id").val();
	    num = $(".number").val();
	    $.get("/app/common/buynow?id="+id+"&num="+num,
	        function(result){
	            alert(result.msg);
	            if(result.code==200){
	                location.href = "/app/order/order?id="+result.data.oid;
	            }
	        }
	    );
	    return false;
	});

    number.on('change',function () {
        if(number.val()<1){
            alert("商品数量至少选择1");
            number.val(1);
            $('.add').attr('disabled',false);
        }
        else if(number.val()>stock){
            alert("商品数量不能超过库存量");
            number.val(stock);
            $('.reduce').attr('disabled',false);
        }
    })
});

$(function () {
    $("[data-toggle='popover']").popover();
    $("#collect").on("click",function(){
        var that = $(this);
        $.get("/app/common/addCollection?pid="+$(this).data("id"),
            function(result){
                if(result.code==200){
                    that.popover("toggle");
                    setTimeout(function(){
                        that.popover("toggle");
                        $(".collect").toggleClass("hidden");
                        $(".collected").toggleClass("hidden");
                    },1000);
                }else{
                    alert(result.msg);
                }
            }
        );

    });
    $("#collected").on("click",function(){
       var that = $(this);
       $.get(
           "/app/common/deleteCollection?id="+$(this).data("id"),
           function(result){
               if(result.code==200){
                  that.popover("toggle");
                   setTimeout(function(){
                       that.popover("toggle");
                       $(".collected").toggleClass("hidden");
                       $(".collect").toggleClass("hidden");
                   },1000);
               }else{
                   alert(result.msg);
               }
           }
       );
    });
});
