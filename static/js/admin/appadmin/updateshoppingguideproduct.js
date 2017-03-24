var csrfToken = Cookies.get("csrftoken");
var oldProduct = {
    "id":document.getElementById("id").value,
    "name":document.getElementById("name").value,
    "show":document.getElementById("show").value,
    "order":document.getElementById("order").value,
    "linkUrl":document.getElementById("linkUrl").value,
    "productImgUrl":document.getElementById("productImgUrl").value,
    "description":document.getElementById("description").value
};
var productForm = new Vue({
    el:"#productForm",
    data:{
        product:{
            id:oldProduct.id,
            name:oldProduct.name,
            show:oldProduct.show,
            order:oldProduct.order,
            linkUrl:oldProduct.linkUrl,
            productImgUrl:oldProduct.productImgUrl,
            description:oldProduct.description,
        }
    },
    methods:{
        updateImg:function(){
            var that = this;
            var formData = new FormData();
            formData.append("productImg",document.getElementById("productImg").files[0]);
            this.$http.post("/admin/appadmin/updateShoppingGuideProductImg",formData,{"headers":{"X-CSRFToken":csrfToken,"enctype":"multipart/form-data"}})
                      .then(success=>{
                        alert(success.body.msg);
                        that.product.productImgUrl = "/static/media/fileupload/shoppingguide/" + success.body.data.imgUrl;
                      },error=>{
                        console.log(error.body.msg);
                      });
        },
        updateProduct:function(){
            this.$http.post("/admin/appadmin/updateShoppingGuideProduct",this.product,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        alert(success.body.msg);
                        if(success.body.code == 200){
                            window.location.href="/admin/appadmin/shoppingGuide";
                        }
                      },error=>{console.log(error.body)});
        }
    }
});
