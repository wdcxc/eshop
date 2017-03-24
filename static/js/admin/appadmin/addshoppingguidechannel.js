var csrfToken = Cookies.get("csrftoken");

var channelForm = new Vue({
    el:"#channelForm",
    data:{
        channel:{
            name:"",
            show:"True",
            order:"1"
        }
    },
    methods:{
        addChannel:function(){
            this.$http.post("/admin/appadmin/addShoppingGuideChannel",this.channel,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        if(success.body.code == 200){
                            alert(success.body.msg);
                            window.location.href = "/admin/appadmin/shoppingGuide";
                        }else{
                            alert(success.code.msg);
                        }
                      },error=>{
                        console.log(error.body);
                      });
        }
    }
});