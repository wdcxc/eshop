var csrfToken = Cookies.get("csrftoken");
var adminForm = new Vue({
    el:"#adminForm",
    data:{
        admin:{
            username:"",
            password:"",
            root:"False",
            groupIds:[],
        }
    },
    methods:{
        addAdmin:function(){
            this.$http.post("/admin/adminadmin/addAdmin",this.admin,{"headers":{"X-CSRFToken":csrfToken}})
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