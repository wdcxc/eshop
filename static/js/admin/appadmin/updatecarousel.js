var csrfToken = Cookies.get("csrftoken");
var oldCarousel = {
    id:document.getElementById("id").value,
    title:document.getElementById("title").value,
    show:document.getElementById("show").value,
    order:document.getElementById("order").value,
    imgUrl:document.getElementById("oldImgUrl").value,
    linkUrl:document.getElementById("linkUrl").value,
};

var carouselForm = new Vue({
    el:"#carouselForm",
    data:{
        carousel:{
            id:oldCarousel.id,
            title:oldCarousel.title,
            show:oldCarousel.show,
            order:oldCarousel.order,
            imgUrl:oldCarousel.imgUrl,
            linkUrl:oldCarousel.linkUrl
        },
        errMsg:''
    },
    methods:{
        updateCarousel:function(){
            var that = this;
            this.$http.post("/admin/appadmin/updateCarousel",this.carousel,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        if(success.body.code == 200){
                            alert(success.body.msg);
                            location.href = "/admin/appadmin/carousel";
                        }else{
                            that.showErrMsg = true;
                            that.errMsg = success.body.msg;
                        }
                      },error=>{
                        console.log(error.body);
                      });
        },
        updateImg:function(){
            var that = this;
            var formData = new FormData();
            formData.append("newImg",document.getElementById("img").files[0]);
            formData.append("oldImgUrl",oldCarousel.imgUrl);
            this.$http.post("/admin/appadmin/updateCarouselImg",formData,{"headers":{"X-CSRFToken":csrfToken,"enctype":"multipart/form-data"}})
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
    }
});
