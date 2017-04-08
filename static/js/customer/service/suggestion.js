var csrfToken = Cookies.get("csrftoken");

var form = new Vue({
    el:"#form",
    data:{
        suggestion:{
            suggestion:"",
            type:"1",
        }
    },
    methods:{
        submitForm:function(){
            this.$http.post("/customer/service/addSuggestion",this.suggestion,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#modalInfo").html(success.body.msg);
                        $("#submitModal").modal("toggle");
                        setTimeout(function(){location.reload(true);},2000);
                      },error=>{
                        console.log(error);
                      });
        }
    }
});