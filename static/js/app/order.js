/**
 * Created by zihang on 2017/3/20.
 */
$(document).ready(function () {
    // 显示订单支付地址
    function changeAddress(){
        let addr = $(".address-selected .address-detail");
        $(".desAddr.province").html($(addr.children(".province")[0]).html());
        $(".desAddr.city").html($(addr.children(".city")[0]).html());
        $(".desAddr.dist").html($(addr.children(".dist")[0]).html());
        $(".desAddr.street").html($(addr.children(".street")[0]).html());
        let user = $(".address-selected .user-detail");
        $(".desAddr.receiver-name").html($(user.children(".user-name")[0]).html());
        $(".desAddr.receiver-phone").html($(user.children(".user-phone")[0]).html());
    };

    changeAddress();

   $(".user-addresslist").click(function () {
       $(this).addClass("address-selected").siblings().removeClass("address-selected");
       changeAddress();
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

    // 支付订单
    $("#pay").on("click",function(){
        let addressId = $(".address-selected").attr("id");
        $.get(
            "/app/order/payOrder"+location.search+"&addressId="+addressId+"&customerMsg="+$("#customerMsg").val(),
            function(result){
                if(result.code == 200){
                    location.href = "/app/order/success"+location.search;
                }else{
                    alert(result.msg);
                }
            });
    });

    // 取消支付订单
    $("#cancel").on("click",function(){
        $.get("/app/order/cancelOrder"+location.search,function(result){
             if(result.code == 200){
                location.href = "/app/order/fail"+location.search;
            }else{
                alert(result.msg);
            }
        });
    });

    /*统计订单总价格*/
    let totalMoney=0;
    totalMoney=($(".commodity-price").text()*$(".commodity-num").text()).toFixed(2);
    $(".commodity-total-price").text(totalMoney);
    $(".pay-sum").text(totalMoney);
});