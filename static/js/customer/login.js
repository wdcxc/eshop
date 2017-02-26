/**
 * Created by wdcxc on 2017/2/18.
 */
var csrftoken = Cookies.get('csrftoken');
var captchaUrl = "/customer/captcha/";

var loginForm = new Vue({
    el: '#loginForm',
    data: {
        customer: {
            account: '',
            password: '',
            captcha: '',
        },
        captcha: captchaUrl,
    },
    methods: {
        updateCaptcha: function () {
            console.log(this.captcha);
            this.captcha = captchaUrl + Math.random();
            return false;
        },
        login: function () {
            var that = this;
            this.customer.captcha = document.getElementById("captcha").value;
            this.$http.post('/customer/doLogin', that.customer, {"headers":{"X-CSRFToken":csrftoken}})
                .then(response => {
                    if(response.body.code == 200){
                        window.location.href = "/app/index"
                    } else {
                        alert(response.body.msg)
                    }
                }, response => {
                    alert(response);
                });
        }
    }
});