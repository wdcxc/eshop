/**
 * Created by zihang on 2017/3/27.
 */
$(document).ready(function () {
    $(".good-evaluate").click(function () {
        $(this).css("background-image","url('/static/images/customer/iconfont-good.png')");
        $(this).siblings(".middle-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");
        $(this).siblings(".bad-evaluate").css("background-image","url('/static/images/customer/iconfont-bad.png')");
    });
    $(".middle-evaluate").click(function () {
        $(this).css("background-image","url('/static/images/customer/iconfont-middle.png')");
        $(this).siblings(".good-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");
        $(this).siblings(".bad-evaluate").css("background-image","url('/static/images/customer/iconfont-bad.png')");
    });
    $(".bad-evaluate").click(function () {
        $(this).css("background-image","url('/static/images/customer/iconfont-badon.png')");
        $(this).siblings(".good-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");
        $(this).siblings(".middle-evaluate").css("background-image","url('/static/images/customer/iconfont-evaluate.png')");

    });
});

var form = new Vue({
    el:"#form",
    data:{
        product:{
            id:document.getElementById("id").value,
            eGrade:"101",
            evaluation:"",
        }
    },
    methods:{
        submitForm:function(){
            this.$http.post("/customer/order/goodsevaluate",this.product,{"headers":{"X-CSRFToken":Cookies.get("csrftoken")}})
                      .then(success=>{
                        $(".modal-body").html(success.body.msg);
                        $("#submitModal").modal("toggle");
                        setTimeout(function(){
                            location.href="/customer/order/evaluateorder"
                        },2000);
                      },error=>{
                        console.log(error);
                      })
        }
    }
});