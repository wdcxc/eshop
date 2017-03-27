/**
 * Created by zihang on 2017/3/27.
 */
csrftoken = Cookies.get("csrftoken");
var captchaUrl = "/seller/captcha/";

registerForm = new Vue({
    el: "#forgetPwdForm",
    data: {
        seller: {
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
            this.$http.post("/seller/doForgetPwd", that.seller, {"headers": {"X-CSRFToken": csrftoken}}).then(response=> {
            }, responser=> {
            });

        }
    }
});
