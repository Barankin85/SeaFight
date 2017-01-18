$(function() {
	$('#restartGameBtn').click(function(){
		if (!confirm('Please confirm game restart')){
			return;
		}
		
		$.ajax({
			url: '/reset',
			type: "POST",
			success: function(){
				window.location.reload();
			},
			failure: function(errMsg) {
				alert(errMsg);
			}
		})
	});
	
    $('.js-fireable').click(function(){
		var button = $(this);
		var x = $(this).data('x');
		var y = $(this).data('y');
		
		$.ajax({
			url: '/',
			type: "POST",
			data: JSON.stringify({ x: x, y: y }),
			contentType: "application/json; charset=utf-8",
			success: function(message){
				button.removeClass('btn-primary');
				button.addClass('btn-danger');
				button.attr('disabled', 'disabled');
				setTimeout(function(){
					if (message)
						alert(message);
				
					window.location.reload();
				}, 200)
			},
			failure: function(errMsg) {
				alert(errMsg);
			}
		})
	});
});