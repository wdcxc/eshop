var csrfToken = Cookies.get("csrftoken");
var parentId = document.getElementById("parentId").value;
var productForm = new Vue({
    el:"#productForm",
    data:{
        product:{
            parentId:parentId,
            name:"",
            show:"True",
            order:"1",
            linkUrl:"",
            productImgUrl:"",
            description:"",
        }
    },
    methods:{
        uploadImg:function(){
            var that = this;
            var formData = new FormData();
            formData.append("productImg",document.getElementById("productImg").files[0]);
            this.$http.post("/admin/appadmin/uploadShoppingGuideProductImg",formData,{"headers":{"X-CSRFToken":csrfToken,"enctype":"multipart/form-data"}})
                      .then(success=>{
                        alert(success.body.msg);
                        that.product.productImgUrl = "/static/media/fileupload/shoppingguide/" + success.body.data.imgUrl;
                      },error=>{
                        console.log(error.body.msg);
                      });
        },
        addProduct:function(){
            console.log(this.subChannel);
            this.$http.post("/admin/appadmin/addShoppingGuideProduct",this.product,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        alert(success.body.msg);
                        if(success.body.code == 200){
                            window.location.href="/admin/appadmin/shoppingGuide";
                        }
                      },error=>{console.log(error.body)});
        }
    }
});
