$(document).ready(function () {
    $(".commodity-price").each(function(){
        let price = parseFloat($(this).html());
        let num = parseInt($($(this).siblings(".commodity-num")[0]).html());
        $($(this).parent().parent().find(".total-price")[0]).html(price*num);
    });
})