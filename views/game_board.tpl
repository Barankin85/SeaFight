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
				% for index in range(1,10):
				<div>
				  % for index2 in range(1,10):
					<a href="#" class="btn btn-sq btn-primary"></a>
				  % end
				</div>
				% end
			</div>
			
			<div class="col-lg-6">
				<div>Enemy</div>
				% for index in range(1,10):
				<div>
				  % for index2 in range(1,10):
					<a href="#" class="btn btn-sq btn-primary"></a>
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