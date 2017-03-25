var csrfToken = Cookies.get("csrftoken");
$(function(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        }
    });

    $(".del-channel").on("click",function(){
        $.post(
            '/admin/appadmin/deleteShoppingGuideChannel',
            {"id":$(this).data("id")},
            function(result){
                alert(result.msg);
                if(result.code == 200){
                    window.location.href = "/admin/appadmin/shoppingGuide";
                }
            }
        );
    });

    $(".del-subchannel").on("click",function(){
        $.post(
            '/admin/appadmin/deleteShoppingGuideSubchannel',
            {"id":$(this).data("id")},
            function(result){
                alert(result.msg);
                if(result.code == 200){
                    window.location.href = "/admin/appadmin/shoppingGuide";
                }
            }
        );
    });

    $(".del-product").on("click",function(){
        $.post(
            '/admin/appadmin/deleteShoppingGuideProduct',
            {"id":$(this).data("id")},
            function(result){
                alert(result.msg);
                if(result.code == 200){
                    window.location.href = "/admin/appadmin/shoppingGuide";
                }
            }
        );
    });
});