var csrfToken = Cookies.get("csrftoken");
var categoryForm = new Vue({
    el:"#categoryForm",
    data:{
        category:{
            parentId:document.getElementById("parentId").value,
            name:"",
            grade:document.getElementById("grade").value,
            show:"True",
            order:"1",
        }
    },
    methods:{
        addCategory:function(){
            this.$http.post("/admin/productadmin/addCategory",this.category,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        if(success.body.code == 200){
                            alert(success.body.msg);
                            window.location.href="/admin/productadmin/category";
                        }else{
                            alert(success.body.msg);
                        }
                      },error=>{
                        console.log(error.body);
                      });
        },
    }
});