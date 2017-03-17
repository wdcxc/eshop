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
        },
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
        },
        uploadImg:function(){
            var that = this;
            var formData = new FormData();
            formData.append("img",document.getElementById("img").files[0])
            this.$http.post("/admin/appadmin/uploadCarouselImg",formData,{"headers":{"X-CSRFToken":csrfToken,"enctype":"multipart/form-data"}})
                      .then(success=>{
                        if(success.body.code == 200){
                            that.carousel.imgUrl = "/static/media/fileupload/carousel/"+success.body.data.imgUrl;
                        }else{
                            alert(success.body.msg);
                        }
                      },error=>{
                        console.log(error.body);
                      });
        }
    },
})