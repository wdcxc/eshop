/**
 * Created by zihang on 2017/3/16.
 */
$(document).ready(function() {
		let splitArray=location.search.substring(1).split('&');
		let object={};
		let tempArray=[];
		for(let i=0;i<splitArray.length;i++){
			tempArray=splitArray[i].split('=');
			object[tempArray[0]]=tempArray[1];
		}
		if(object.hasOwnProperty('method')){
			let method=object['method'];
			$('.sort').find('a').each(function () {
				$(this).parent().css('background-color', '#fff');
				if ($(this).data('method') == method) {
					$(this).parent().css('background-color', '#f5f5f5');
				}
			});
		}
		if(object.hasOwnProperty('brand')){
			let brand=decodeURI(object['brand']);
			$("#select1").find('a').each(function () {
				if($(this).data('value')==brand){
					$(this).parent().addClass('selected').siblings().removeClass("selected");
					let copyThisA = $(this).parent().clone(false);
					if ($("#selectA").length > 0) {
						$("#selectA").find("a").html($(this).parent().text());
					} else {
						$(".select-result").css("display","block");
						$(".select-result dl").append(copyThisA.attr("id", "selectA"));
					}
				}
			});
		}
		if(object.hasOwnProperty('category_id')){
			let category_id=object['category_id'];
			$("#select2").find('a').each(function () {
				if($(this).data('id')==category_id){
					$(this).parent().addClass('selected').siblings().removeClass("selected");
					let copyThisB = $(this).parent().clone(false);
					if ($("#selectB").length > 0) {
						$("#selectB").find("a").html($(this).parent().text());
					} else {
						$(".select-result").css("display","block");
						$(".select-result dl").append(copyThisB.attr("id", "selectB"));
					}
				}
			});
		}

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
		let oldParam=location.search+"&method="+$(this).find("a").data("method");
		string=getParamString(oldParam);
		window.location.href=window.location.pathname+string;
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
		if(!$(this).hasClass('select-all')){
			let oldParam=location.search+"&brand="+$(this).find("a").data("value");
			string=getParamString(oldParam);
			window.location.href=window.location.pathname+string;
		}else{
			let oldSearch=location.search;
			let string;
			string=deleteParam(oldSearch,'brand');
			window.location.href=window.location.pathname+string;
		}
	});
	$("#select2").find("dd").on("click",function () {
		if(!$(this).hasClass('select-all')){
			let oldParam=location.search+"&category_id="+$(this).find("a").data("id");
			string=getParamString(oldParam);
			window.location.href=window.location.pathname+string;
		}else{
			let oldSearch=location.search;
			let string;
			string=deleteParam(oldSearch,'category_id');
			window.location.href=window.location.pathname+string;
		}
	});
	$(".pagination").find("li").on("click",function () {
		location.search=location.search+"&page="+$(this).find("a").data("page");
		string=getParamString(oldParam);
		window.location.href=window.location.pathname+string;
	});
});
function getParamString(oldParam){
	var i=0;
	var a=[],params,arr=[];
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
function deleteParam(oldSearch,name){
	var i=0;
	var a=[],arr=[];
	var string="?";
	var object={};
	arr = oldSearch.substring(1).split("&");
	for (i = 0; i < arr.length; i++) {
		a = arr[i].split("=");
		object[a[0]] = a[1];
	}
	if(object[name]){
		delete object[name];
	}
	for (var key in object) {
		string = string + key + "=" + object[key] + "&";
	}
	string = string.substr(0, string.length - 1);
	return string;
}

