/**
 * Created by wdcxc on 2017/2/18.
 */
var csrftoken = Cookies.get('csrftoken');
var captchaUrl = "/customer/common/generateCaptcha/";

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
        inputCaptchaCode:{
            get: function(){
                return this.customer.captchaCode;
            },
            set: function (newValue){
                this.customer.captchaCode = newValue;
                if(newValue.length == 4){
                    this.valifyCaptcha();
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
            this.$http.post('/customer/common/doLogin', that.customer, {"headers":{"X-CSRFToken":csrftoken}})
                .then(response => {
                    if(response.body.code == 200){
                        window.location.href = "/customer/information/index";
                    } else {
                        that.updateCaptcha();
                        this.infoMsg.msg = response.body.msg;
                        this.infoMsg.style = 'msg-error';
                    }
                }, response => {
                    console.log(response);
                });
        },
        valifyCaptcha: function(){
           var captchaCode = this.customer.captchaCode;
           var that = this;
           this.$http.post('/customer/common/valifyCaptcha',{"captchaCode":captchaCode},{"headers":{"X-CSRFToken":csrftoken}})
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