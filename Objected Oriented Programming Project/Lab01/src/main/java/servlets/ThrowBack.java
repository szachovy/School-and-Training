package servlets;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


//i powrót do formularza z efektem przekierowania
@WebServlet("/getback")
public class ThrowBack extends HttpServlet{
	private static final long serialVersionUID = 1L;

	
	public void routingEffect() {
		try {
			TimeUnit.SECONDS.sleep(2);
		} 
		catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException{
		
		routingEffect();
		response.sendRedirect("/");
	}
}
