package servlets;

import java.io.IOException;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


//wystąpienie informacji o błędzie
@WebServlet("/error")
public class ErrorMode extends HttpServlet{
	private static final long serialVersionUID = 1L;

	@Override
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException{
		
		response.getWriter().println("<h2 style=\"color:red;\">Error occurred! Przy wpisywaniu upewnij sie, ze wszedzie"
				+ " znajduja sie cyfry oraz pola nie sa puste.</h2>");
		
		response.getWriter().println("</br><h2>Nacisnij Powrot by zostac przekierowany do strony z formularzem</h2>"
				+ "<form method=\"post\" action=\"getback\"><input type=\"submit\" value=\"Powrot\"></form>");	
	}
}
