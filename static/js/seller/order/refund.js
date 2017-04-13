var csrfToken = Cookies.get("csrftoken");

var form = new Vue({
    el:"#form",
    data:{
        refund:{
            id:document.getElementById("id").value,
            status:"8",
            refundDealResult:"",
        }
    },
    methods:{
        submitForm:function(){
            this.$http.post("/seller/order/refund",this.refund,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $(".modal-body").html(success.body.msg);
                        $("#submitModal").modal("toggle");
                        setTimeout(function(){
                            location.reload(true);
                        },2000);
                      },error=>{
                        console.log(error);
                      });
        }
    }
});

$(function(){
    var price = parseInt($(".price").html());
    var num = parseFloat($(".num").html());
    var totalPrice = price*num;
    $(".total-price").html(totalPrice);
    $("#price").val(totalPrice);

});