/**
 * Created by wdcxc on 2017/2/21.
 */
var csrftoken = Cookies.get("csrftoken");
var captchaUrl = "/customer/common/generateCaptcha/";

customerForm = new Vue({
    el: "#customerForm",
    data: {
        customer: {
            name:"",
            password:"",
            email:"",
            mobile:"",
            captchaCode:"",
        },
        captcha: {
            imageUrl: captchaUrl,
        },
    },
    methods: {
        updateCaptcha: function () {
            this.captcha.imageUrl = captchaUrl + Math.random();
            return false;
        },
        registCustomer: function () {
            var that = this;
            this.$http.post("/customer/common/doRegister", that.customer, {"headers": {"X-CSRFToken": csrftoken}}).then(success=> {
                $("#modalInfo").html(success.body.msg);
                $("#registerModal").modal("toggle");
                if(success.body.code == 200){
                    setTimeout(function(){
                        window.location.href = "/customer/common/login";
                    },2000);
                }else{
                    that.updateCaptcha();
                }

            }, responser=> {
                console.log(response.body.msg)
            });

        },
    }
});