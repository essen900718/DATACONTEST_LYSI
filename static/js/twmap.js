$(function(){
  $("#none").click(function(){
    location.reload();
  });
	// $(".color").click(function (){
	// 	$(this).addClass('now');
	// 	$(".color").not(this).removeClass('now');
	// 	color = $('.now').attr('style').substr(12,7);
	// 	console.log(color);
	// });
	color = $('.now').attr('style').substr(12,7);
	console.log(color);
	let clicked = false;
	$(".twt-map-path").click(
		function(){
			if (clicked){
				clicked = false
				color = "#e3b92c"
			}else{
				clicked = true
				color = $('.now').attr('style').substr(12,7);
			}
			$(this).css('fill',color);
			console.log(clicked)
		}
	);

});