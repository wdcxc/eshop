var csrfToken = Cookies.get("csrftoken");
var oldSeller = {
    "truename":document.getElementById("truename").value,
    "mobile":document.getElementById("mobile").value,
    "email":document.getElementById("email").value,
    "shopName":document.getElementById("shopName").value,
    "shopAddress":document.getElementById("shopAddress").value,
    "idno":document.getElementById("idno").value,
    "thumbnail":document.getElementById("thumbnail").value,
}
var form = new Vue({
    el:"#form",
    data:{
        seller:{
            truename:oldSeller.truename,
            mobile:oldSeller.mobile,
            email:oldSeller.email,
            idno:oldSeller.idno,
            shopName:oldSeller.shopName,
            shopAddress:oldSeller.shopAddress,
            thumbnail:oldSeller.thumbnail,
        }
    },
    methods:{
        submitForm:function(){
            this.$http.post("/seller/common/shopinfo",this.seller,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#modalInfo").html(success.body.msg);
                        $("#saveModal").modal("toggle");
                        if(success.body.code == 200){
                            setTimeout(function(){location.reload(true);},2000);
                        }
                      },error=>{
                            console.log(error);
                      });
        },
        uploadImg:function(){
            var that = this;
            var formData = new FormData();
            formData.append("img",document.getElementById("img").files[0]);
            this.$http.post("/seller/common/uploadThumbnail",formData,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#modalInfo").html(success.body.msg);
                        $("#saveModal").modal("toggle");
                        if(success.body.code==200){
                            that.seller.thumbnail = "/static/media/fileupload/"+success.body.data.imgUrl;
                        }
                      },error=>{
                        console.log(error);
                      });
        }
    }
});