var csrfToken = Cookies.get("csrftoken");
var oldAdmin = {
    "id":document.getElementById("id").value,
    "root":document.getElementById("root").value,
    "groupIds":document.getElementById("groupIds").value.split(","),
};
var adminForm = new Vue({
    el:"#adminForm",
    data:{
        admin:{
            id:oldAdmin.id,
            password:"",
            root:oldAdmin.root,
            groupIds:oldAdmin.groupIds,
        }
    },
    methods:{
        updateAdmin:function(){
            if(this.admin.groupIds.indexOf("") != -1){
                this.admin.groupIds.splice(this.admin.groupIds.indexOf(""),1);
            }
            this.$http.post("/admin/adminadmin/updateAdmin",this.admin,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        alert(success.body.msg);
                        if(success.body.code == 200){
                            location.href = "/admin/adminadmin/adminIndex";
                        }
                      },error=>{
                        console.log(error.body)
                      });
        }
    }
});