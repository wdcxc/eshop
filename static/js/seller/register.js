/**
 * Created by zihang on 2017/3/27.
 */
var csrftoken = Cookies.get("csrftoken");
var captchaUrl = "/seller/common/generateCaptcha/";

registerForm = new Vue({
    el: "#registerForm",
    data: {
        seller: {
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
            this.$http.post("/seller/common/doRegister", that.seller, {"headers": {"X-CSRFToken": csrftoken}}).then(response=> {
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