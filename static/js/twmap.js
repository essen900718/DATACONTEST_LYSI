$(function(){
  $("#none").click(function(){
    location.reload();
  });
	$(".color").click(function(){
		$(this).addClass('now');
		$(".color").not(this).removeClass('now');
		color = $('.now').attr('style').substr(12,7);
		console.log(color);
	});

	color = $('.now').attr('style').substr(12,7);
	console.log(color);
	$(".twt-map-path").click(
		function(){
			$(this).css('fill',color);
	});

});