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
    function calTotalPrice(){
        let totalMoney=0;
        $(".commodity-price").each(function(){
            let price = parseFloat($(this).text());
            let amount = parseInt($(this).siblings(".commodity-num").text());
            $(this).siblings(".commodity-total-price").text(price*amount);
            totalMoney += price*amount;
        });
        $(".pay-sum").text(totalMoney);
    };
    calTotalPrice();
});

var addrModal = new Vue({
    el:"#addrModal",
    data:{
        address:{
            id:"",
            name:"",
            address:"",
            mobile:"",
            province:"",
            city:"",
            dist:"",
        },
        provinces:[],
        citys:[],
        dists:[],
    },
    methods:{
        submitForm:function(){
            this.$http.post("/customer/information/addAddress",this.address,{"headers":{"X-CSRFToken":Cookies.get("csrftoken")}})
                      .then(success=>{
                        alert(success.body.msg);
                        setTimeout(function(){location.reload(true)},1000);
                      },error=>{
                        console.log(error);
                      });
        },
        updateProvince:function(){
            var that = this;
            this.$http.get("/customer/information/citys?province="+this.address.province)
                      .then(success=>{
                        that.citys = success.body.data.citys
                      },error=>{
                        console.log(error);
                      });
        },
        updateCity:function(){
            var that = this;
            this.$http.get("/customer/information/dists?province="+this.address.province+"&city="+this.address.city)
                      .then(success=>{
                        that.dists = success.body.data.dists
                      },error=>{
                        console.log(error);
                      });
        }
    }
});