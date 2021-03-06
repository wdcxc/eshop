/**
 * Created by zihang on 2017/3/24.
 */
$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        }
    });

    $(".user-addresslist").click(function () {
        $(this).addClass("address-selected").siblings().removeClass("address-selected");
    });

    $(".set-default").click(function () {
        $(this).addClass("hidden");
        $(this).parents("li").find(".deftip").removeClass("hidden");
        $(".set-default").not(this).removeClass("hidden");
        $(".set-default").not(this).parents("li").find(".deftip").addClass("hidden");
        let addrid = $(this).data("id");
        $.post(
        "/customer/information/setDefaultAddr",
        {"id":addrid},
        function(result){
            location.reload(true);
        }
        );
    });

    $(".delete-address").click(function () {
       $(this).parents("li").css("display","none");
       let addrid = $(this).data("id");
        $.post(
        "/customer/information/deleteAddress",
        {"id":addrid},
        function(result){
            location.reload(true);
        }
        );
    });

    $(".update-address").on("click",function(){
        $.get(
            "/customer/information/address?id="+$(this).data("id"),
            function(result){
                if(result.code==200){
                    addrModal.$data.provinces = result.data.provinces;
                    addrModal.$data.citys = result.data.citys;
                    addrModal.$data.dists = result.data.dists;
                    addrModal.$data.address = result.data.address;
                    $("#addressModal").modal("toggle");
                }else{
                    $("#modalInfo").html(result.msg);
                    $("#saveModel").modal("toggle");
                }
            }
        )
    });
});

var addrModal = new Vue({
    el:"#addrModal",
    data:{
        address:{
            id:"",
            name:"",
            address:"",
            mobile:"",
            province:"",
            city:"",
            dist:"",
        },
        provinces:[],
        citys:[],
        dists:[],
    },
    methods:{
        updateAddress:function(){
            this.$http.post("/customer/information/updateAddress",this.address,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        console.log(success);
                        location.reload(true);
                      },error=>{
                        console.log(error);
                      });
        },
        updateProvince:function(){
            var that = this;
            this.$http.get("/customer/information/citys?province="+this.address.province)
                      .then(success=>{
                        that.citys = success.body.data.citys
                      },error=>{
                        console.log(error);
                      });
        },
        updateCity:function(){
            var that = this;
            this.$http.get("/customer/information/dists?province="+this.address.province+"&city="+this.address.city)
                      .then(success=>{
                        that.dists = success.body.data.dists
                      },error=>{
                        console.log(error);
                      });
        }
    }
});

var csrfToken = Cookies.get("csrftoken");
var form = new Vue({
    el:"#form",
    data:{
        address:{
            name:"",
            address:"",
            province:"",
            city:"",
            dist:"",
            mobile:"",
        },
        citys:[],
        dists:[],
    },
    methods:{
        submitForm:function(){
            this.$http.post("/customer/information/addAddress",this.address,{"headers":{"X-CSRFToken":csrfToken}})
                      .then(success=>{
                        $("#modalInfo").html(success.body.msg);
                        $("#addModal").modal("toggle");
                        if(success.body.code==200){
                            setTimeout(function(){location.reload(true)},2000);
                        }
                      },error=>{
                        console.log(error);
                      });
        },
        updateProvince:function(){
            var that = this;
            this.$http.get("/customer/information/citys?province="+this.address.province)
                      .then(success=>{
                        that.citys = success.body.data.citys
                      },error=>{
                        console.log(error);
                      });
        },
        updateCity:function(){
            var that = this;
            this.$http.get("/customer/information/dists?province="+this.address.province+"&city="+this.address.city)
                      .then(success=>{
                        that.dists = success.body.data.dists
                      },error=>{
                        console.log(error);
                      });
        }
    }
});