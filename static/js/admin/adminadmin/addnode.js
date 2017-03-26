var csrfToken = Cookies.get("csrftoken");
var nodeForm = new Vue({
    el:"#nodeForm",
    data:{
        node:{
            name:"",
            action:"",
            controller:"",
            linkUrl:"",
        }
    },
    methods:{
        addNode:function(){
            this.$http.post("/admin/adminadmin/addNode",this.node,{"headers":{"X-CSRFToken":csrfToken}})
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