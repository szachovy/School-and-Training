package domain;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import repositories.AccountRepositoryInterface;

public class HSQLDBConnect implements  AccountRepositoryInterface{

	protected Connection connection = null;
	protected Statement cursor = null;
	protected ResultSet result = null;

		// łączenie z db
	    public void connectHSQLDB() {
	        try {
	            Class.forName("org.hsqldb.jdbcDriver");
	            String dburl = "jdbc:hsqldb:hsql://localhost:8080/";
	            String userid = "SA";
	            String password = "";
	            String database = "mydatabase";
	            connection = DriverManager.getConnection(dburl + database, userid, password);
	            cursor = connection.createStatement();
	        } catch (Exception e) {
	        	System.err.println("ERROR: failed to load HSQLDB JDBC driver.");
	            e.printStackTrace();
	            return;
	        }
	    }
	    // służy do fetchwania danych w PrintAllServlet
	    public List<Account> getRows() throws SQLException{
	    	ArrayList<Account> users = new ArrayList<Account>();
	    	Account account;
			cursor = connection.createStatement();
			result = cursor.executeQuery("SELECT * FROM users;");
			while (result.next()) {
				account = new Account();
				String username = result.getString("username");
				String passwd = result.getString("passwd");
				boolean premium = result.getBoolean("ispremium");
				boolean admin = result.getBoolean("isadministrator");
				
				account.setUsername(username);
				account.setPasswd(passwd);
				account.setPremium(premium);
				account.setAdmin(admin);
				users.add(account);
			}
			return users;
	    }
	    
	    public void insertTestRows() throws SQLException{
	    	for(int i=1;i<10;i++){
			cursor = connection.createStatement();
			result = cursor.executeQuery("INSERT INTO users VALUES (null,'a"+i+"','a"+i+"', false, false)");
			System.out.println(result);
	    	}
	    }

	    // fetchowanie tymczasowego konta
	    @Override
		public Account getAccountByName(String username) throws SQLException {
	    	Account acc = new Account();
			cursor = connection.createStatement();
			result = cursor.executeQuery("SELECT * FROM users WHERE username = '"+username+"';");
			while (result.next()) {
				System.out.println("u:"
						+ result.getString("username") + " / "
						+ result.getString("passwd") + " / "
						+ result.getBoolean("ispremium") + " / "
						+ result.getBoolean("isadministrator"));
				acc.setUsername(result.getString("username"));
				acc.setPasswd(result.getString("passwd"));
				acc.setPremium(result.getBoolean("ispremium"));
				acc.setAdmin(result.getBoolean("isadministrator"));
				
			}
			return acc;
		}
	    // powielone db.size()
		@Override
		public int count() throws SQLException {
			int rows =0;
			String sql = "select count(*) from users;";	
			cursor = connection.createStatement();
			result = cursor
					.executeQuery(sql);
			while (result.next()) {
				rows = result.getInt(1);
			}
			return rows;
		}
		
		// dodawanie konta do db przy tworzeniu
		@Override
		public void add(Account acc) throws SQLException {
			if(connection==null){
				System.out.println("Connection error with DB server");
			}
			else {
				cursor.execute("INSERT into USERS VALUES (null,'"+acc.getUsername()+"','"+acc.getPasswd()+"', false, false)");
			}
			
		}

		@Override
		public void setPrivilages(String username) throws Exception {
			cursor = connection.createStatement();
			result = cursor.executeQuery("UPDATE users SET ispremium = true WHERE username = '"+username+"';");
			connection.commit();
			cursor.close();
			
		}
		
		public void closeConn(){
			if(connection!=null){
				try {
					connection.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				System.out.println("Conn closed...");
			}
		}
}
