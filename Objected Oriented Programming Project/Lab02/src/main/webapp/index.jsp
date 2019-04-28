<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Lab02</title>
</head>
<body>

		<!-- sprawdzenie czy uzytkownik zalogowany. Jesli tak to odsyła do serwletu zalogowania -->
	<%
	HttpServletResponse httpResponse = (HttpServletResponse) response;
	if(session.getAttribute("signed")!=null){
		httpResponse.sendRedirect("/loggingSession");
	}%>
	<!-- logowanie -->
	
	<form action="/loggingSession" method="get">
		<h2 style="font-style: italic">Sign in:</h2>
		<br>
		<label>Username: <input type="text" required id="username" name="username" /></label><br/><br/><br/>
		<label>Password: <input type="password" required id="passwd" name="passwd" /></label><br/><br/>
		<input type="submit" value="Sign In!"/>
	</form>
	<h2 style="font-style: italic">Or</h2>
	<!-- rejestracja -->
	<form action="/signingSession">
		<h2 style="font-style: italic">Sign up:</h2><br/>
		<label>Username: <input type="text" required id="username" name="username"/></label><br/><br/>
		<label>Password: <input type="password" required id="passwd" name="passwd"/></label><br/><br/>
		<label>Confirm Password: <input type="password" required id="passwdconf" name="passwdconf"/></label><br/><br/>
		<label>Email: <input type="email" required id="email" name="email"/></label><br/><br/>
		<input type="submit" value="Sign Up!"/>
	</form>
</body>
</html>