package servlets;


import java.io.IOException;
import java.io.PrintWriter;


import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import domain.HSQLDBConnect;



@WebServlet("/setPremium")
public class Premium extends HttpServlet{
	private static final long serialVersionUID = 1L;
	public HSQLDBConnect repo;
	
	//nadawanie uprawnień konkretnemu userowi
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		repo.connectHSQLDB();
		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		String username = request.getParameter("username");
		
		out.print("Target User set to Premium: " + username); 
		try {
			repo.setPrivilages(username);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		out.close();
		repo.closeConn();
	}

	
}