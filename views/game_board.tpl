<html>
<head>
  <title>Sea fight game</title>
  <link rel="stylesheet" href="/static/css/main.css">
  <link rel="stylesheet" href="/static/css/bootstrap/bootstrap.min.css">
</head>
<body>
	<div class="container">
		<div class="row">
			<div class="col-lg-6">
				<div>You</div>
				% for i in range(0,9):
				<div>
				  % for j in range(0,9):
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
			
			<div class="col-lg-6">
				<div>Enemy</div>
				% for i in range(0,9):
				<div>
				  % for j in range(0,9):
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