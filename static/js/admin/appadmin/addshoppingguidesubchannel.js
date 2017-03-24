var csrfToken = Cookies.get("csrftoken");
var parentId = document.getElementById("parentId").value;
var subChannelForm = new Vue({
    el:"#subChannelForm",
    data:{
        subChannel:{
            parentId:parentId,
            name:"",
            show:"True",
            order:"1",
        }
    },
    methods:{
        addSubchannel:function(){
            console.log(this.subChannel);
            this.$http.post("/admin/appadmin/addShoppingGuideSubchannel",this.subChannel,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        alert(success.body.msg);
                        if(success.body.code == 200){
                            window.location.href="/admin/appadmin/shoppingGuide";
                        }
                      },error=>{console.log(error.body)});
        }
    }
});
