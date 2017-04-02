/**
 * Created by zihang on 2017/4/2.
 */
$(document).ready(function(){
    /*商品数量加减*/
    $(".add").click(function () {
        var number=$(this).siblings(".number");
        number.val(parseInt(number.val())+1);
        $(this).parents('.table-content').find('.commodity-total-price').text((parseFloat($(this).parents('.table-content').find('.commodity-price').text())*parseInt(number.val())).toFixed(2));
        if(parseInt(number.val())!=1){
            $(this).siblings(".reduce").attr('disabled',false);
        }
    });

    $(".reduce").click(function () {
        var number=$(this).siblings(".number");
        number.val(parseInt(number.val())-1);
        $(this).parents('.table-content').find('.commodity-total-price').text((parseFloat($(this).parents('.table-content').find('.commodity-price').text())*parseInt(number.val())).toFixed(2));
        if(parseInt(number.val())==1){
           $(this).attr('disabled',true);
       }
    });
    /*全选*/
    $(".select-all").click(function () {
        if (this.checked) {
            $(".checkbox").prop('checked', true);
        } else {
            $(".checkbox").prop('checked', false);
        }
    });

});
