/**
 * Created by wdcxc on 2017/2/21.
 */
var csrftoken = Cookies.get("csrftoken");
var captchaUrl = "/customer/common/generateCaptcha/";

registerForm = new Vue({
    el: "#registerForm",
    data: {
        customer: {
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
            var that = this;
            this.$http.post("/customer/common/doRegister", that.customer, {"headers": {"X-CSRFToken": csrftoken}}).then(response=> {
                if(response.body.code == 200){
                    //todo
                }else{

                }

            }, responser=> {
                console.log(response.body)
            });

        }
    }
});