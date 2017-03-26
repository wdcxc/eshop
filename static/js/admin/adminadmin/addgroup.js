var csrfToken = Cookies.get("csrftoken");
var nodeForm = new Vue({
    el:"#groupForm",
    data:{
        group:{
            name:"",
            nodeIds:[],
        }
    },
    methods:{
        addGroup:function(){
            this.$http.post("/admin/adminadmin/addGroup",this.group,{"headers":{"X-CSRFToken":csrfToken}})
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