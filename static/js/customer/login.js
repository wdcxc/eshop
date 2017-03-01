/**
 * Created by wdcxc on 2017/2/18.
 */
var csrftoken = Cookies.get('csrftoken');
var captchaUrl = "/customer/getCaptchaImage/";

var loginForm = new Vue({
    el: '#loginForm',
    data: {
        customer: {
            account: '',
            password: '',
            captchaCode: '',
        },
        captcha:{
            imageUrl : captchaUrl
        },
        infoMsg:{
            msg : '',
            style : 'hide'
        }
     },
    computed:{
        updateCaptchaCode:{
            get: function(){
                return this.customer.captchaCode;
            },
            set: function (newValue){
                this.customer.captchaCode = newValue;
                if(newValue.length == 4){
                    this.valifyCaptchaCode();
                }
            }
        }
    },
    methods: {
        updateCaptcha: function () {
            this.captcha.imageUrl = captchaUrl + Math.random();
            this.infoMsg.style = 'hide';
            return false;
        },
        doLogin: function () {
            var that = this;
            this.$http.post('/customer/doLogin', that.customer, {"headers":{"X-CSRFToken":csrftoken}})
                .then(response => {
                    if(response.body.code == 200){
                        window.location.href = "/app/index";
                    } else {
                        this.infoMsg = response.body.msg;
                    }
                }, response => {
                    alert(response);
                });
        },
        valifyCaptchaCode: function(){
           var captchaCode = this.customer.captchaCode;
           var that = this;
           this.$http.post('/customer/valifyCaptcha',{"captchaCode":captchaCode},{"headers":{"X-CSRFToken":csrftoken}})
                     .then(response=>{
                        that.infoMsg.msg = response.body.msg;
                        if(response.body.code == 200){
                            that.infoMsg.style = 'msg-right';
                        }else{
                            that.infoMsg.style = 'msg-error';
                        }
                     },response=>{
                        console(response.body);
                     })
        }
    }
});