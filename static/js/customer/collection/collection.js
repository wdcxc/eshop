$(function(){
    $(".add-to-shopcart").on("click",function(){
        $.get("/app/common/addShopcart?id="+$(this).data("id")+"&num=1",
            function(result){
                alert(result.msg);
                if(result.code == 200){
                    location.href = "/app/common/shopcart";
                }
            }
        );
    });

    $(".delete").on("click",function(){
        $.get(
            "/app/common/deleteCollection?id="+$(this).data("id"),
            function(result){
                alert(result.msg);
                location.reload(true);
            }
        );
    });
});