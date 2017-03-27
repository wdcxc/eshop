var csrfToken = Cookies.get("csrftoken");
var oldNode = {
    "id":document.getElementById("id").value,
    "name":document.getElementById("name").value,
    "controller":document.getElementById("controller").value,
    "action":document.getElementById("action").value,
    "linkUrl":document.getElementById("linkUrl").value,
};
var nodeForm = new Vue({
    el:"#nodeForm",
    data:{
        node:{
            id:oldNode.id,
            name:oldNode.name,
            action:oldNode.action,
            controller:oldNode.controller,
            linkUrl:oldNode.linkUrl,
        }
    },
    methods:{
        updateNode:function(){
            this.$http.post("/admin/adminadmin/updateNode",this.node,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        alert(success.body.msg);
                        if(success.body.code == 200){
                            location.href = "/admin/adminadmin/nodeIndex";
                        }
                      },error=>{
                        console.log(error.body)
                      });
        }
    }
});