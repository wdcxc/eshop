var csrfToken = Cookies.get("csrftoken");
var uploadImages = new Set();
var uploadedImageConfigs = [];
var uploadedImageUrls = [];
var quill = null;

var oldProduct = {
    id:$("#id").val(),
    name:$("#name").val(),
    price:$("#price").val(),
    amount:$("#amount").val(),
    status:$("#status").val(),
    brand:$("#brand").val(),
    description:$("#description").val(),
    thumbnail:$("#oldThumbnail").val(),
};

 $(function () {
     quill = new Quill('#editor', {
        modules:{
            toolbar:[
                [{header:[1,2,false]}],
                ['bold','italic','underline'],
                ['image','link'],
            ]
        },
        theme: 'snow'
    });

    let desc = $.parseJSON(oldProduct.description);
    quill.setContents(desc);

    $('.image').each(function(){
        uploadedImageConfigs.push({key:$(this).attr("id")});
        uploadedImageUrls.push($(this).val());
        uploadImages.add($(this).attr("id"));
    });

    $('#manufacture-date').datetimepicker({
        format: 'YYYY-MM-DD'
    });

     $('#guarantee-date').datetimepicker({
        format: 'YYYY-MM-DD'
    });

     $("#modal-input").fileinput({
         uploadUrl:"/seller/goods/uploadImage",
         initialPreview: uploadedImageUrls,
         initialPreviewAsData: true,
         initialPreviewConfig: uploadedImageConfigs,
         deleteUrl: "/seller/goods/deleteImage",
         overwriteInitial: false,
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
     });

     $('#modal-input').on('fileuploaded', function(event, data, previewId, index) {
            response = data.response;
            uploadImages.add(response.id);
            console.log(response);
     });

     $("#modal-input").on('filedeleted',function(event,key){
        uploadImages.delete(key);
     });

     $("#thumbnail").fileinput({
         uploadUrl:"/seller/goods/uploadImage",
         initialPreview: [oldProduct.thumbnail],
         initialPreviewAsData: true,
         overwriteInitial: true,
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
     });

     $('#thumbnail').on('fileuploaded', function(event, data, previewId, index) {
            response = data.response;
            form.$data.product.thumbnail = response.imgUrl;
     });

     $("#thumbnail").on('filedeleted',function(event,key){
        form.$data.product.thumbnail = "";
     });


});

var form = new Vue({
    el:"#form",
    data:{
        product:{
            id:oldProduct.id,
            name:oldProduct.name,
            price:oldProduct.price,
            amount:oldProduct.amount,
            brand:oldProduct.brand,
            status:oldProduct.status,
            properties:{},
            uploadImages:[],
            description:oldProduct.description,
            thumbnail:oldProduct.thumbnail,
        }
    },
    methods:{
        submitForm:function(){
            var that = this;
            $(".property").each(function(){
                that.product.properties[$(this).attr("id")] = $(this).val();
            });
            this.product.uploadImages = Array.from(uploadImages);
            this.product.description = JSON.stringify(quill.getContents());
            this.$http.post("/seller/goods/updateGoods",this.product,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#modalInfo").html(success.body.msg);
                        $("#modifyModal").modal("toggle");
                        if(success.body.code==200){
                            setTimeout(function(){location.reload(true);},2000);
                        }
                      },error=>{
                        console.log(error);
                      });
        }
    }
});