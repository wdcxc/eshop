var csrfToken = Cookies.get("csrftoken");
var oldCustomer = {
    "nickname":document.getElementById("nickname").value,
    "truename":document.getElementById("truename").value,
    "sex":document.getElementById("sex").value,
    "mobile":document.getElementById("mobile").value,
    "email":document.getElementById("email").value,
    "avatar":document.getElementById("avatar").value,
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
            birthday:"",
        }
    },
    methods:{
        formSubmit:function(){
            this.customer.birthday = $("#birthday").val();
            this.$http.post("/customer/information/information",this.customer,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#infoMsg").html(success.body.msg);
                        $("#saveModal").modal("toggle");
                        if(success.body.code == 200){
                            setTimeout(function(){
                                location.reload(true);
                            },1000);
                        }
                      },error=>{
                        console.log(error);
                      });
        },
        uploadAvatar:function(){
            var that = this;
            var formData = new FormData();
            formData.append("img",document.getElementById("img").files[0])
            this.$http.post("/customer/information/uploadAvatar",formData,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#infoMsg").html(success.body.msg);
                        $("#saveModal").modal("toggle");
                        if(success.body.code == 200){
                            that.customer.avatar = "/static/media/fileupload/"+success.body.data.imgUrl;
                        }
                      },error=>{
                        console.log(error);
                      });
        }
    }
});