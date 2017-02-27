var csrftoken = Cookies.get("csrftoken");
var captchaImageBaseUrl = "/admin/getCaptchaImage/";
var loginForm = new Vue({
    el:"#loginForm",
    data:{
        admin:{
            username:'',
            password:'',
            captchaCode:''
        },
        captcha:{
            imageUrl:captchaImageBaseUrl,
        }
    },
    computed:{
    },
    methods:{
        doLogin:function(){},
        updateCaptchaImage:function(){
           this.captcha.imageUrl = captchaImageBaseUrl + Math.random();
           return false;
        },
        valifyCaptcha:function(){
        }
    }
});