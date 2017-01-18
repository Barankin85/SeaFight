$(function() {
    $('.js-fireable').click(function(){
		var x = $(this).data('x');
		var y = $(this).data('y');
		
		$.ajax({
			url: '/',
			type: "POST",
			data: JSON.stringify({ x: x, y: y }),
			contentType: "application/json; charset=utf-8",
			success: function(message){
				if (message)
					alert(message);
				
				window.location.reload();
			},
			failure: function(errMsg) {
				alert(errMsg);
			}
		})
	});
});