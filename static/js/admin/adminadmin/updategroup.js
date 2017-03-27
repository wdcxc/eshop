var csrfToken = Cookies.get("csrftoken");
var oldGroup = {
    "id":document.getElementById("id").value,
    "name":document.getElementById("name").value,
    "nodeIds":document.getElementById("nodeIds").value.split(","),
};
var adminForm = new Vue({
    el:"#groupForm",
    data:{
        group:{
            id:oldGroup.id,
            name:oldGroup.name,
            nodeIds:oldGroup.nodeIds,
        }
    },
    methods:{
        updateGroup:function(){
            if(this.group.nodeIds.indexOf("") != -1){
                this.group.nodeIds.splice(this.group.nodeIds.indexOf(""),1);
            }
            this.$http.post("/admin/adminadmin/updateGroup",this.group,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        alert(success.body.msg);
                        if(success.body.code == 200){
                            location.href = "/admin/adminadmin/groupIndex";
                        }
                      },error=>{
                        console.log(error.body)
                      });
        }
    }
});