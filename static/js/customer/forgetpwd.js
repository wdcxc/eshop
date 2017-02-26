/**
 * Created by zihang copy form register.js on 2017/2/26.
 */
csrftoken = Cookies.get("csrftoken");
var captchaUrl = "/customer/captcha/";

registerForm = new Vue({
    el: "#forgetPwdForm",
    data: {
        customer: {
            captchaCode: '',
        },
        captcha: captchaUrl,
    },
    methods: {
        updateCaptcha: function () {
            console.log(this.captcha);
            this.captcha = captchaUrl + Math.random();
            return false;
        },
        commit: function () {
            let that = this;
            this.$http.post("/customer/doForgetPwd", that.customer, {"headers": {"X-CSRFToken": csrftoken}}).then(response=> {
            }, responser=> {
            });

        }
    }
});