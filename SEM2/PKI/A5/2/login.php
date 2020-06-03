<! DOCTYPE html>
<html>
<h1 align = "center">Login Page</h1>
<body>
<head>
	<title> Login Page </title>
	<link rel = "stylesheet" type = "text/css" href = "style.css"> 
</head>
</body>
	<div id = "frm">
			<form action = "process.php" method = "POST">
			<p>
				<label>Username:</label>
				<input type = "text" id = "user" name = "user"/>
			</p>
			<p>
				<label> Password:</label>
				<input type = "password" id = "pwd" name = "pwd"/>
			</p>
			<p>
				
				<input type = "submit" id = "btn"  value= "Login"/>
			</p>
	</div>
</html>