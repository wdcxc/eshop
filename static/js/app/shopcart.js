/**
 * Created by zihang on 2017/4/2.
 */
$(document).ready(function(){
    var csrfToken = Cookies.get("csrftoken");

    $.ajaxSetup({
        beforeSend:function(xhr,settings){
            if(!this.crossDomain){
                xhr.setRequestHeader("X-CSRFToken",csrfToken);
            }
        }
    });

    $(".add").each(function(){
        var number=$(this).siblings(".number");
        number.val(parseInt(number.val()));
        $(this).parents('.table-content').find('.commodity-total-price').text((parseFloat($(this).parents('.table-content').find('.commodity-price').text())*parseInt(number.val())).toFixed(2));
    });

    /*商品数量加减*/
    $(".add").click(function () {
        var number=$(this).siblings(".number");
        number.val(parseInt(number.val())+1);
        $(this).parents('.table-content').find('.commodity-total-price').text((parseFloat($(this).parents('.table-content').find('.commodity-price').text())*parseInt(number.val())).toFixed(2));
        if(parseInt(number.val())>1){
            $(this).siblings(".reduce").attr('disabled',false);
        }
    });

    $(".reduce").click(function () {
        var number=$(this).siblings(".number");
        number.val(parseInt(number.val())-1);
        $(this).parents('.table-content').find('.commodity-total-price').text((parseFloat($(this).parents('.table-content').find('.commodity-price').text())*parseInt(number.val())).toFixed(2));
        if(parseInt(number.val())<=1){
           $(this).attr('disabled',true);
       }
    });

    var order = {};

    /*全选*/
    $(".select-all").click(function () {
        if (this.checked) {
            $(".checkbox").prop('checked', true);
            $(".select").each(function(){
                $(this).change();
            });
        } else {
            $(".checkbox").prop('checked', false);
            $(".select").each(function(){
                $(this).change();
            });
        }
    });

    $(".select").on("change",function(){
        if($(this).prop("checked")){
            order[$(this).data("id")] = {
                "num":$(this).parent().parent().find(".number")[0].value,
                "price":$($(this).parent().parent().children(".commodity-total-price")[0]).html(),
                };
        }else{
            delete order[$(this).data("id")];
        }

        let selectNum = 0;
        let totalPrice = 0.0;
        for(i in order){
            selectNum++;
            totalPrice += parseFloat(order[i]["price"]);
        }
        $(".select-num .num").html(selectNum);
        $(".total-price .num").html(totalPrice);
    });

    $("#pay").on("click",function(){
        url = "/app/order/addOrder";
        data = "";
        for(i in order){
            data += i + ":" + order[i]["num"] + ",";
        }
        $.post(
            url,
            {"order":data},
            function(result){
                if(result.code==200){
                    location.href = "/app/order/order?id="+result.data.id;
                }else{
                    alert(result.msg);
                }
            }
        );
        return false;
    });

    $(".delete").on("click",function(){
        $.get("/app/common/deleteShopcart?id="+$(this).data("id"),function(result){
            alert(result.msg);
            if(result.code==200){
                location.reload(true);
            }
        });
        return false;
    });

    $(".add-collection").on("click",function(){
        $.get("/app/common/addCollection?pid="+$(this).data("id"),
            function(result){
                alert(result.msg);
            }
        )
    });

});
