package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import domain.Account;
import domain.HSQLDBConnect;


@WebServlet("/loggingSession")
public class LoginServlet extends HttpServlet{
	static final long serialVersionUID = 1L;
	public HSQLDBConnect repo = new HSQLDBConnect();
	boolean validateCheck = false;
	
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
		HttpSession session = request.getSession();
		PrintWriter out = response.getWriter();
		checkUser(retrieveUserInformationFromRequest(request), request, response, session);
        String username = request.getParameter("username");
        String passwd = request.getParameter("passwd");
		try {
			if(repo.count()!=0 && null != repo.getAccountByName(username)){
				// zapisywanie danych logowania w sesji
			    if(passwd.equals((repo.getAccountByName(username)).getPasswd())){ 
			        session.setAttribute("username",username);
			        session.setAttribute("password",passwd);
			        session.setAttribute("ispremium",(repo.getAccountByName(username)).isPremium());
			        session.setAttribute("isadmin",(repo.getAccountByName(username)).isAdmin());
			    	out.print("Logged as: "+ username );
			    	out.println("<br/>");
			    	out.println("see Premium");
			    	// odeslanie do servletu wypisujacego wszystkich uzytkownikow w usersdb
			    	out.println("form action='/printAll' method='get'><br/>");
			    	out.println("<input type=\"submit\" value=\"Print All\"/>");

			    	// po danych logowania system wykrywa czy uzytkownik jest adminem 
			    	if(repo.getAccountByName(username).isAdmin() == true){
			    		// i dodaje przycisk
			    		out.println("form action='/setPremium' method='get'><br/>");
			    		out.println("<label>Username: <input type=\"text\" required id=\"username\" name=\"username\"/></label><br/>");
				    	out.println("<input type=\"submit\" value=\"Premium Set\"/>");
			    	}
			    }
			    else{
			    	// w przypadku nieudanego logowania powiazania 'username' z 'passwd'
			    	out.println("Username or password incorrect...");
			    	out.println("</br>");
			    }
			}
			else{
				// w przypadku braku konta
				out.println("Username or password incorrect...");
				out.println("</br>");
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	private Account retrieveUserInformationFromRequest(HttpServletRequest request) {
		Account result = new Account();
		result.setUsername(request.getParameter("username"));
		result.setPasswd(request.getParameter("passwd"));
		return result;
	}
	private boolean checkUser(Account user, HttpServletRequest request, HttpServletResponse response, HttpSession session) throws IOException, ServletException {
		{
	        try{
	        	// sprawdzenie czy uzytkownik ma swoje konto w bazie danych usersdb
	           Class.forName("org.hsqldb.jdbc.JDBCDriver");

	           Connection cursor = DriverManager.getConnection
	                          ("jdbc:hsqldb:hsql//localhost/usersdb","asd123","");
	           PreparedStatement cur = cursor.prepareStatement
                       ("SELECT * FROM register WHERE username=? and pass=?");
	           cur.setString(1, (String) session.getAttribute(request.getParameter("username")));
	           cur.setString(2, (String) session.getAttribute(request.getParameter("passwd")));
	           ResultSet rs = cur.executeQuery();
	           validateCheck = rs.next();
	           
	           cursor.close();
	          
	        }
	        catch(Exception e)
	        {
	            e.printStackTrace();
	        }
	           return validateCheck;                 
	   }
	}
}
