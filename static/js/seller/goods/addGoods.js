var csrfToken = Cookies.get("csrftoken");
var uploadImages = new Set();
var properties = {};
var quill = null;

$(function () {
    quill = new Quill('#description', {
        modules:{
            toolbar:[
                [{header:[1,2,false]}],
                ['bold','italic','underline'],
                ['image','link'],
            ]
        },
        placeholder:"goods description",
        theme: 'snow'
    });


    $('#manufacture-date').datetimepicker({
        format: 'YYYY-MM-DD'
    });

    $('#guarantee-date').datetimepicker({
        format: 'YYYY-MM-DD'
    });

    $("#uploadImage").fileinput({
        uploadUrl:"/seller/goods/uploadImage",
        deleteUrl:"/seller/goods/deleteImage",
        maxFileCount:5,
        ajaxSettings:{
            beforeSend: function(xhr, settings) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
            }
        },
        ajaxDeleteSettings:{
            beforeSend: function(xhr, settings) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
            }
        },
        initialPreview: [],
        initialPreviewAsData: true,
        initialPreviewConfig: [],
    });

    $('#uploadImage').on('fileuploaded', function(event, data, previewId, index) {
        response = data.response;
        uploadImages.add(response.id);
    });

    $("#uploadImage").on('filedeleted',function(event,key){
        uploadImages.delete(key);
    });

    $("#thumbnail").fileinput({
        uploadUrl:"/seller/goods/uploadImage",
        deleteUrl:"/seller/goods/deleteImage",
        maxFileCount:1,
        ajaxSettings:{
            beforeSend: function(xhr, settings) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
            }
        },
        ajaxDeleteSettings:{
            beforeSend: function(xhr, settings) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
            }
        },
        initialPreview: [],
        initialPreviewAsData: true,
        initialPreviewConfig: [],
    });

    $('#thumbnail').on('fileuploaded', function(event, data, previewId, index) {
        response = data.response;
        form.$data.goods.thumbnail = response.imgUrl;
    });

    $("#thumbnail").on('filedeleted',function(event,key){
        form.$data.goods.thumbnail = "";
    });
});

var form = new Vue({
    el:"#form",
    data:{
        goods:{
            name:"",
            price:"",
            amount:"",
            brand:"",
            status:1,
            categoryId:$("#categoryId").data("id"),
            uploadImages:[],
            properties:{},
            description:"",
            thumbnail:"",
        }
    },
    methods:{
        submitForm:function(){
            this.goods.uploadImages = Array.from(uploadImages);
            var that = this;
            $(".property").each(function(){
                that.goods.properties[$(this).attr("id")] = $(this).val();
            });
            this.goods.description = JSON.stringify(quill.getContents());
            this.$http.post("/seller/goods/addGoods",this.goods,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#modalInfo").html(success.body.msg);
                        $("#addModal").modal("toggle");
                        if(success.body.code == 200){
                            setTimeout(function(){location.href = "/seller/goods/goodslist";},2000);
                        }
                      },error=>{
                        console.log(error);
                      });
        }
    }
});