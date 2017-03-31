/**
 * Created by zihang on 2017/3/27.
 */
var csrftoken = Cookies.get("csrftoken");
var captchaUrl = "/seller/common/generateCaptcha/";

var registerForm = new Vue({
    el: "#registerForm",
    data: {
        seller: {
            idno:"",
            name:"",
            password:"",
            mobile:"",
            email:"",
            confirmPwd:"",
            captchaCode: '',
        },
        captcha: {
            imageUrl: captchaUrl
        }
    },
    methods: {
        updateCaptcha: function () {
            this.captcha.imageUrl = captchaUrl + Math.random();
            return false;
        },
        doRegister: function () {
            if(this.seller.password!=this.seller.confirmPwd){
                $("#modalInfo").html("密码不一致");
                $("#registerModal").modal("toggle");
                return
            }
            var that = this;
            this.$http.post("/seller/common/doRegister", that.seller, {"headers": {"X-CSRFToken": csrftoken}}).then(success=> {
                $("#modalInfo").html(success.body.msg);
                $("#registerModal").modal("toggle");
                if(success.body.code == 200){
                    setTimeout(function(){
                        window.location.href = "/seller/common/login";
                    },2000);
                }else{
                    that.updateCaptcha();
                }

            }, responser=> {
                console.log(response.body.msg)
            });

        }
    }
});