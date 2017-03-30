var csrfToken = Cookies.get("csrftoken");
var oldCustomer = {
    "nickname":document.getElementById("nickname").value,
    "truename":document.getElementById("truename").value,
    "sex":document.getElementById("sex").value,
    "mobile":document.getElementById("mobile").value,
    "email":document.getElementById("email").value,
    "avatar":document.getElementById("avatar").value,
    "birthday":document.getElementById("birthday").value,
}
var customerForm = new Vue({
    el:"#form",
    data:{
        customer:{
            nickname:oldCustomer.nickname,
            truename:oldCustomer.truename,
            sex:oldCustomer.sex,
            mobile:oldCustomer.mobile,
            email:oldCustomer.email,
            avatar:oldCustomer.avatar,
            birthday:oldCustomer.birthday,
        }
    },
    methods:{
        formSubmit:function(){
            this.$http.post("/customer/common/information",this.customer,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{

                      },error=>{

                      });
        },
        uploadAvatar:function(){

        }
    }
});