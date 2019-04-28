package repositories;

import java.util.ArrayList;
import java.util.List;

import domain.Account;

//klasa umozliwiajaca operacje na danym koncie
public class AccountRepository implements AccountRepositoryInterface {

	private static List<Account> db = new ArrayList<Account>();
	
	@Override
	public Account getAccountByName(String username) {
		for(Account user: db){
			if(user.getUsername().equalsIgnoreCase(username))
				return user;
		}
		return null;
	}
	
	@Override
	public void setPrivilages(String username) {
		for(Account user:db) {
			if(user.getUsername().equalsIgnoreCase(username)) {
				user.setPremium(true);
			}
		}
	}

	@Override
	public void add(Account user) {
		db.add(user);	
	}
	@Override
	public int count() {
		return db.size();
	}
	public Object returnArray() {
		return db;
	}
}
