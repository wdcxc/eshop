/**
 * Created by zihang on 2017/3/16.
 */
$(document).ready(function() {
        $("#select1").find("dd").click(function(){
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectA").remove();
		} else {
			var copyThisA = $(this).clone();
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

	$("#selectA").on("click", function() {
		$("#selectA").remove();
		$("#select1").find(".select-all").addClass("selected").siblings().removeClass("selected");
	});

	$("#selectB").on("click", function() {
		$("#selectB").remove();
		$("#select2").find(".select-all").addClass("selected").siblings().removeClass("selected");
	});

	$("#selectC").on("click", function() {
		$("#selectC").remove();
		$("#select3").find(".select-all").addClass("selected").siblings().removeClass("selected");
	});

	$(".select dd").on("click", function() {
		if ($(".select-result dd").length > 1) {
			$(".select-no").hide();
			$(".eliminateCriteria").show();
			$(".select-result").show();
		} else {
			$(".select-no").show();
			$(".select-result").hide();
		}
	});

	$(".eliminateCriteria").on("click", function() {
		$("#selectA").remove();
		$("#selectB").remove();
		$("#selectC").remove();
		$(".select-all").addClass("selected").siblings().removeClass("selected");
		$(".eliminateCriteria").hide();
		$(".select-no").show();
		$(".select-result").hide();
	});
	$(".sort").find("li").on("click",function(){
		$(".sort").find("li").css("background-color","#fff");
		$(this).css("background-color","#F5F5F5");
	});
});