/**
 * Created by wdcxc on 2017/2/21.
 */
var csrftoken = Cookies.get("csrftoken");
var captchaUrl = "/customer/captcha/";

registerForm = new Vue({
    el: "#registerForm",
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
        register: function () {
            let that = this;
            this.$http.post("/customer/doRegister", that.customer, {"headers": {"X-CSRFToken": csrftoken}}).then(response=> {
            }, responser=> {
            });

        }
    }
});