<html>
<head>
  <title>Sea fight game</title>
  <link rel="stylesheet" href="/static/css/main.css">
  <link rel="stylesheet" href="/static/css/bootstrap/bootstrap.min.css">
</head>
<body>
	<div class="container">
		<div class="row gamefield">
		    <div class="col-lg-2">
				<a href="#" class="btn btn-primary" id="restartGameBtn">Restart game</a>
			</div>
			<div class="col-lg-5">
				<div>You</div>
				% for i in range(0,10):
				<div>
				  % for j in range(0,10):
				    %if game.you.board.positions[i][j].isOccupied:
						%if game.you.board.positions[i][j].isFired:
							<a href="#" class="btn btn-sq btn-danger" disabled="disabled"></a>
						%else:
							<a href="#" class="btn btn-sq btn-info" disabled="disabled"></a>
						%end
					%else:
					    <a href="#" class="btn btn-sq btn-primary" disabled="disabled"></a>
					%end
				  % end
				</div>
				% end
			</div>
			
			<div class="col-lg-5">
				<div>Enemy</div>
				% for i in range(0,10):
				<div>
				  % for j in range(0,10):
					%if game.enemy.board.positions[i][j].isOccupied:
						%if game.enemy.board.positions[i][j].isFired:
							<a href="#" class="btn btn-sq btn-danger" disabled="disabled"></a>
						%else:
							<a href="#" class="js-fireable btn btn-sq btn-primary" data-x="{{i}}" data-y="{{j}}"></a>
						%end
					%else:
						%if game.enemy.board.positions[i][j].isFired:
							<a href="#" class="btn btn-sq btn-default" disabled="disabled"></a>
						%else:
							<a href="#" class="js-fireable btn btn-sq btn-primary" data-x="{{i}}" data-y="{{j}}"></a>
						%end
					%end
				  % end
				</div>
				% end
			</div>
		</div>
	</div>
	<script src="/static/js/jquery-3.1.1.min.js"></script>
	<script src="/static/js/bootstrap/bootstrap.min.js"></script>
	<script src="/static/js/main.js"></script>
</body>
</html>