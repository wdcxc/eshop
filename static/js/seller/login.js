/**
 * Created by zihang on 2017/3/27.
 */
var csrftoken = Cookies.get('csrftoken');
var captchaUrl = "/seller/common/generateCaptcha/";

var loginForm = new Vue({
    el: '#loginForm',
    data: {
        seller: {
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
                return this.seller.captchaCode;
            },
            set: function (newValue){
                this.seller.captchaCode = newValue;
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
            this.$http.post('/seller/common/doLogin', that.seller, {"headers":{"X-CSRFToken":csrftoken}})
                .then(response => {
                    if(response.body.code == 200){
                        window.location.href = "/seller/index";
                    } else {
                        this.infoMsg = response.body.msg;
                    }
                }, response => {
                    alert(response);
                });
        },
        valifyCaptcha: function(){
           var captchaCode = this.seller.captchaCode;
           var that = this;
           this.$http.post('/seller/common/valifyCaptcha',{"captchaCode":captchaCode},{"headers":{"X-CSRFToken":csrftoken}})
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