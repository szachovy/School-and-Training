package repositories;

import java.sql.SQLException;

import domain.Account;

public interface AccountRepositoryInterface {
	Account getAccountByName(String username) throws SQLException;
	void add(Account user) throws SQLException;
	int count() throws SQLException;
	void setPrivilages(String username) throws Exception;
}
