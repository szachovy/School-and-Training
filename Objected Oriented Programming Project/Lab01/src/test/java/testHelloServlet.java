import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.junit.Test;
import org.mockito.Mockito;

import servlets.HelloServlet;


public class testHelloServlet extends Mockito{
	
	//test na puste pola
	@Test
	public void empty_checking() throws IOException{
		HttpServletRequest request = mock(HttpServletRequest.class);
		HttpServletResponse response = mock(HttpServletResponse.class);
		HelloServlet servlet = new HelloServlet();
		
		when(request.getParameter("kredyt")).thenReturn("");
		when(request.getParameter("raty")).thenReturn("");
		when(request.getParameter("oprocentowanie")).thenReturn("");
		when(request.getParameter("oplata")).thenReturn("");
		
		try {
			servlet.doPost(request, response);
			verify(response).sendRedirect("/");
		} 
		catch (ServletException e) {
			e.printStackTrace();
		}
	}
	
	//test czy wpisane dane są cyframi
	@Test
	public void digits_checking() throws IOException, ServletException {
		HttpServletRequest request = mock(HttpServletRequest.class);
		HttpServletResponse response = mock(HttpServletResponse.class);
		HelloServlet servlet = new HelloServlet();
		
		int zatwierdz = 0;

		Object[] pola = {request.getParameter("kredyt"), request.getParameter("raty"), request.getParameter("oprocentowanie"),
				request.getParameter("oplata"), request.getParameter("rodzaj")};
		
		//sprawdzenie dla kazdego pola w formularzu
		for (Object conv : pola) {
			if (conv instanceof String) {
				when(Float.parseFloat((String) conv));
				zatwierdz += 1;
			}
		}
		//jezeli wszedzie są cyfry to ilość pól w których są cyfry odpowiada ilości pól.
		if (zatwierdz == length(pola)) {
			servlet.doPost(request, response);
			verify(response).sendRedirect("/");
		}	
	}

	private int length(Object[] pola) {
		int dlugosc = 0;
		for (int i = 0; i < length(pola); i++) {
			dlugosc += 1;
		}
		return dlugosc;
	}

}
