package domain;

// przechowywanie danych konta (patrz: LoginServlet)
public class Account {
	private boolean premium;
	private boolean admin;
	private String username;
	private String passwd;
	private String email;
	
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String name) {
		this.username = name;
	}
	public String getPasswd() {
		return passwd;
	}
	public void setPasswd(String password) {
		this.passwd = password;
	}
	public boolean isPremium() {
		return premium;
	}
	public void setPremium(boolean premium) {
		this.premium = premium;
	}
	public boolean isAdmin() {
		return admin;
	}
	public void setAdmin(boolean admin) {
		this.admin = admin;
	}
}
