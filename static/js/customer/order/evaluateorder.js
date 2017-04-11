$(document).ready(function () {
    $(".commodity-price").each(function(){
        let price = parseFloat($(this).html());
        let num = parseInt($($(this).siblings(".commodity-num")[0]).html());
        $($(this).parent().parent().find(".total-price")[0]).html(price*num);
    });
});

var csrfToken = Cookies.get("csrftoken");

$(function () {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        }
    });

    $("[data-toggle='popover']").popover();

    $(".refund").on("click",function(){
        $("#rpid").val($(this).data("id"));
        $("#refundModal").modal("toggle");
    });

    $("#doRefund").on("click",function(){
        $.post(
            "/customer/order/refund",
            {"id":$("#rpid").val(),"refundReason":$("#refundReason").val()},
            function(result){
                alert(result.msg);
                $("#refundModal").modal("toggle");
                setTimeout(function(){location.reload(true);},2000);
            }
        );
    });
});
