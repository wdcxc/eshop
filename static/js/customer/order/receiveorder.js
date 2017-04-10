$(document).ready(function () {
    $(".commodity-price").each(function(){
        let price = parseFloat($(this).html());
        let num = parseInt($($(this).siblings(".commodity-num")[0]).html());
        $($(this).parent().parent().find(".total-price")[0]).html(price*num);
    });
})

$(function () {
    $("[data-toggle='popover']").popover();

    $(".receive").on("click",function(){
        let that = $(this);
        $.get(
            "/customer/order/receiveProduct?id="+$(this).data("id"),
            function(result){
                if(result.code == 200){
                    that.popover("toggle");
                    setTimeout(function(){location.reload(true);},2000);
                }else{
                    alert(result.msg);
                }
            }
        );
    });
});