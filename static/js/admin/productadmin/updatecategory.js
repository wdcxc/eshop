var csrfToken = Cookies.get("csrftoken");
var oldCategory = {
    id:document.getElementById("id").value,
    parentId:document.getElementById("parentId").value,
    name:document.getElementById("name").value,
    show:document.getElementById("show").value,
    grade:document.getElementById("grade").value,
    order:document.getElementById("order").value,
};

var categoryForm = new Vue({
    el:"#categoryForm",
    data:{
        category:{
            id:oldCategory.id,
            parentId:oldCategory.parentId,
            name:oldCategory.name,
            show:oldCategory.show,
            grade:oldCategory.grade,
            order:oldCategory.order,
        }
    },
    methods:{
        updateCategory:function(){
            this.$http.post("/admin/productadmin/updateCategory",this.category,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        if(success.body.code == 200){
                            alert(success.body.msg);
                            window.location.href = "/admin/productadmin/category";
                        }else{
                            alert(success.body.msg);
                        }
                      },error=>{
                        console.log(error.body);
                      });
        }
    }
})
