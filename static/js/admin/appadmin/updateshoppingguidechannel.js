var csrfToken = Cookies.get("csrftoken");
var oldChannel = {
    "id":document.getElementById("id").value,
    "name":document.getElementById("name").value,
    "show":document.getElementById("show").value,
    "order":document.getElementById("order").value
};
var channelForm = new Vue({
    el:"#channelForm",
    data:{
        channel:{
            id:oldChannel.id,
            name:oldChannel.name,
            show:oldChannel.show,
            order:oldChannel.order
        }
    },
    methods:{
        updateChannel:function(){
            this.$http.post("/admin/appadmin/updateShoppingGuideChannel",this.channel,{"headers":{"X-CSRFToken":csrfToken}})
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