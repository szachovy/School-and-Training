package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import domain.Account;
import domain.HSQLDBConnect;
import repositories.AccountRepository;

@WebServlet("/printAll")
public class PrintAllServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	public HSQLDBConnect repo = new HSQLDBConnect();

	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		
		repo.connectHSQLDB();
		PrintWriter out = response.getWriter();
		AccountRepository repository = new AccountRepository();
		request.setAttribute("allUsers", repository.returnArray());
		request.getRequestDispatcher("/printAll.jsp").forward(request, response);
		

		// wypisywanie danych kont linijka bo linijce
        response.setContentType("text/html");  
	        try {
				if(repo.count()!=0){  
	      
					for(Account users : repo.getRows()){
						out.println(users.getUsername() + " | " + users.isPremium());
						out.println("<br>");
					}
					
					
				}
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}   
	        repo.closeConn();
	} 
}
