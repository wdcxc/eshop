var csrftoken = Cookies.get("csrftoken");
var captchaImageBaseUrl = "/admin/common/generateCaptcha/";
var loginForm = new Vue({
    el:"#loginForm",
    data:{
        user:{
            username:'',
            password:'',
            captchaCode:''
        },
        captcha:{
            imageUrl:captchaImageBaseUrl,
        },
        info:{
            msg:"",
            style:"info-hide"
        }
    },
    computed:{
        inputCaptchaCode:{
            get:function(){
                return this.user.captchaCode;
            },
            set:function(newValue){
                this.user.captchaCode = newValue;
                if(newValue.length == 4){
                    this.valifyCaptcha();
                }else if(newValue.length>4){
                    this.info.msg = "验证码错误";
                    this.info.style = "info-error";
                }
            }
        }
    },
    methods:{
        doLogin:function(){},
        updateCaptcha:function(){
           this.captcha.imageUrl = captchaImageBaseUrl + Math.random();
           return false;
        },
        valifyCaptcha:function(){
            var that = this;
            this.$http.post("/admin/common/valifyCaptcha",this.user,{"headers":{"X-CSRFToken":csrftoken}})
                      .then(response=>{
                        if(response.body.code == 200){
                            that.info.style = "info-success";
                        }else{
                            that.info.style = "info-error";
                        }
                        that.info.msg = response.body.msg;
                      },response=>{
                        console.log(response.body);
                      });
        },
        doLogin:function(){
            var that = this;
            this.$http.post("/admin/common/doLogin",this.user,{"headers":{"X-CSRFToken":csrftoken}})
                      .then(response=>{
                        console.log(response.body);
                        if(response.body.code == 200){
                            window.location.href = "/admin/common/index";
                        }else{
                            that.info.style = "info-error";
                            that.info.msg = response.body.msg;
                            that.updateCaptcha();
                        }
                      },response=>{
                        console.log(response.body);
                      });
        }
    }
});