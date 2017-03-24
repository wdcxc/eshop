var csrfToken = Cookies.get("csrftoken");
var oldSubchannel = {
    "id":document.getElementById("id").value,
    "name":document.getElementById("name").value,
    "show":document.getElementById("show").value,
    "order":document.getElementById("order").value,
};
console.log(oldSubchannel);
var subChannelForm = new Vue({
    el:"#subChannelForm",
    data:{
        subChannel:{
            id:oldSubchannel.id,
            name:oldSubchannel.name,
            show:oldSubchannel.show,
            order:oldSubchannel.order,
        }
    },
    methods:{
        updateSubchannel:function(){
            console.log(this.subChannel);
            this.$http.post("/admin/appadmin/updateShoppingGuideSubchannel",this.subChannel,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        alert(success.body.msg);
                        if(success.body.code == 200){
                            window.location.href="/admin/appadmin/shoppingGuide";
                        }
                      },error=>{console.log(error.body)});
        }
    }
});
