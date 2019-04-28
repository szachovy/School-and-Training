package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import domain.Account;
import domain.HSQLDBConnect;

// UWAGA podczas rejestracji należy odświeżyć hosta
@WebServlet("/signingSession")
public class RegistrationServlet extends HttpServlet{
	private static final long serialVersionUID = 1L;
	public HSQLDBConnect repo = new HSQLDBConnect();
	
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		
		HttpSession session = request.getSession();
		Account user = retrieveUserInformationFromRequest(request);
				
		session.setAttribute("signed", user);
		
		// sprawdzanie poprawności haseł
		if(request.getParameter("password").equals(request.getParameter("confirmPassword"))){
			try {
				repo.add(user);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			response.sendRedirect("/loggingSession");
		}else{
			response.setContentType("text/html;charset=UTF-8");
	        PrintWriter out = response.getWriter();
			out.println("Passwords are not the same.");
            out.println("</br>");
            request.getRequestDispatcher("/loggingSession").include(request, response);
            out.close();
		}
		
		repo.closeConn();
		
	}
	private Account retrieveUserInformationFromRequest(HttpServletRequest request) {
		// zakładanie nowego konta
		Account result = new Account();
		result.setUsername(request.getParameter("username"));
		result.setPasswd(request.getParameter("passwd"));
		result.setEmail(request.getParameter("email"));
		result.setAdmin(false);
		result.setPremium(false);
		return result;
		}
}
