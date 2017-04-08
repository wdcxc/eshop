/**
 * Created by zihang on 2017/3/16.
 */
$(document).ready(function() {

        $("#select1").find("dd").click(function(){
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectA").remove();
		} else {
			var copyThisA = $(this).clone(false);
			if ($("#selectA").length > 0) {
				$("#selectA").find("a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisA.attr("id", "selectA"));
			}
		}
	});

	$("#select2").find("dd").click(function() {
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectB").remove();
		} else {
			var copyThisB = $(this).clone();
			if ($("#selectB").length > 0) {
				$("#selectB").find("a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisB.attr("id", "selectB"));
			}
		}
	});

	$("#select3").find("dd").click(function() {
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectC").remove();
		} else {
			var copyThisC = $(this).clone();
			if ($("#selectC").length > 0) {
				$("#selectC").find("a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisC.attr("id", "selectC"));
			}
		}
	});

	$(".select-list dd").click(function(){
		if ($(".select-result dd").length > 1) {
			$(".select-no").hide();
			$(".eliminateCriteria").show();
			$(".select-result").show();
		} else {
			$(".select-no").show();
			$(".select-result").hide();
		}
	});

	$(".select").on("click","#selectA",function () {
	    if ($(".select-result dd").length == 2) {
            $(".eliminateCriteria").click();
        }else{
	        $("#selectA").remove();
		    $("#select1").find(".select-all").addClass("selected").siblings().removeClass("selected");
	    }
	});
	$(".select").on("click","#selectB",function () {
	    if ($(".select-result dd").length == 2) {
            $(".eliminateCriteria").click();
        }else{
	        $("#selectB").remove();
		    $("#select2").find(".select-all").addClass("selected").siblings().removeClass("selected");
	    }
	});
	$(".select").on("click","#selectC",function () {
	    if ($(".select-result dd").length == 2) {
            $(".eliminateCriteria").click();
        }else{
	        $("#selectC").remove();
		    $("#select3").find(".select-all").addClass("selected").siblings().removeClass("selected");
	    }
	});

	$(".eliminateCriteria").click(function(){
		$("#selectA").remove();
		$("#selectB").remove();
		$("#selectC").remove();
		$(".select-all").addClass("selected").siblings().removeClass("selected");
		$(".eliminateCriteria").hide();
		$(".select-no").show();
		$(".select-result").hide();
	});

	$(".sort").find("li").click(function(){
		$(".sort").find("li").css("background-color","#fff");
		$(this).css("background-color","#F5F5F5");
	});
	$(".commodity").mouseenter(function () {
		$(this).css("box-shadow","0px 1px 3px rgba(34, 25, 25, 0.2)");
	});
	$(".commodity").mouseleave(function () {
		$(this).css("box-shadow","none");
	});


	$("#prePage").on("click",function(){

	});
	$("#nextPage").on("click",function(){

	});

	$("#select1").find("dd").on("click",function () {
		let oldParam=location.search+"&brand="+$(this).find("a").data("value");
		string,object=getParamString(oldParam);
		window.location.href=window.location.pathname+string;
	});
	$("#select2").find("dd").on("click",function () {
		let oldParam=location.search+"&category_id="+$(this).find("a").data("id");
		string=getParamString(oldParam);
		window.location.href=window.location.pathname+string;
	});
	$(".sort").find("li").on("click",function () {
		let oldParam=location.search+"&method="+$(this).find("a").data("method");
		string=getParamString(oldParam);
		window.location.href=window.location.pathname+string;
	});
	$(".pagination").find("li").on("click",function () {
		location.search=location.search+"&page="+$(this).find("a").data("page");
		string=getParamString(oldParam);
		window.location.href=window.location.pathname+string;
	});
});
function getParamString(oldParam){
	var i=0;
	var a=[],params=[],arr=[];
	var string="?";
	var object={};
	params = decodeURI(oldParam);
	arr = params.substring(1).split("&");
	for (i = 0; i < arr.length; i++) {
		a = arr[i].split("=");
		object[a[0]] = a[1];
	}
	for (var key in object) {
		string = string + key + "=" + object[key] + "&";
	}
	string = string.substr(0, string.length - 1);
	return string;
}

