var csrfToken = Cookies.get("csrftoken");
var carouselForm = new Vue({
    el:"#carouselForm",
    data:{
        carousel:{
            title:"",
            show:"True",
            order:"1",
            imgUrl:"",
            linkUrl:""
        }
    },
    methods:{
        addCarousel:function(){
            var that = this;
            this.$http.post("/admin/appadmin/addCarousel",this.carousel,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(response=>{
                                if(response.body.code == 200){
                                    alert(response.body.msg);
                                    window.location.href="/admin/appadmin/carousel";
                                }else{
                                    alert("添加首页轮播图失败");
                                }
                            },
                            response=>{console.log(response.body)});
        }
    },
})