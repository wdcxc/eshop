var csrfToken = Cookies.get("csrftoken");

var change = {
    "show":{},
    "order":{},
};

$(function(){
    $("[name$=show]").on("change",function(){
        parentValue = $(this).val();
        change["show"][$(this).data("id")] = parentValue;
        children = $($(this).parents(".col-md-offset-1")[0]).find(".col-md-offset-1").find("[name$=show]");
        children.each(function(index,ele){
            if($(ele).val() != parentValue){
                $(ele).prop("checked",false);
            }else{
                $(ele).prop("checked",true);
            }
            change["show"][$(ele).data("id")] = parentValue;
        });
    });
    $("[name$=order]").on("change",function(){
        change["order"][$(this).data("id")] = $(this).val();
    });
    $("#submit").on("click",function(){
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
            }
        });
        $.post(
        "/admin/appadmin/productCategory",
        {"s":change["show"],"o":change["order"]},
        function(result){
            alert(result.msg);
            location.reload(true);
        });
        return false;
    });
});