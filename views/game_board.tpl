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
				% for i in range(1,10):
				<div>
				  % for j in range(1,10):
				    %if game.yourBoard[i][j].occupied:
						%if game.yourBoard[i][j].isFired:
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
				% for i in range(1,10):
				<div>
				  % for j in range(1,10):
					%if game.enemyBoard[i][j].occupied:
						%if game.enemyBoard[i][j].isFired:
							<a href="#" class="btn btn-sq btn-danger" disabled="disabled"></a>
						%else:
							<a href="#" class="btn btn-sq btn-primary"></a>
						%end
					%else:
						%if game.enemyBoard[i][j].isFired:
							<a href="#" class="btn btn-sq btn-default" disabled="disabled"></a>
						%else:
							<a href="#" class="btn btn-sq btn-primary"></a>
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
</body>
</html>