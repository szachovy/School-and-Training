/*	UWAGA !!!
 * Przez problemy z konwersią pliku PDF został dodatkowo pobrany plik itextpdf-5.3.4.jar
 * w katalogu webapp/WEB-INF/lib/
 * 
 * zakomentowałem kod z tworzeniem pliku PDF ponieważ wysyłane jest żądanie FTP i niemogę wyświetlić
 * docelowej tabeli

 */
package servlets;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.itextpdf.text.Document;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.pdf.PdfPTable;

@WebServlet("/calculate")
public class HelloServlet extends HttpServlet{
	private static final long serialVersionUID = 1L;
	
	//by liczby mieściły się w tabeli potrzebowałem funkcji zaokrąglającej wynik do 2 miejsc po przecinku w górę
	public double zaokraglanie(double wartosc) {
		Double wynik = BigDecimal.valueOf(wartosc)
			    .setScale(2, RoundingMode.HALF_UP)
			    .doubleValue();
		return wynik;
	}
	
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		
		String kredyt = request.getParameter("kredyt");
		String raty = request.getParameter("raty");
		String oprocentowanie = request.getParameter("oprocentowanie");
		String oplata = request.getParameter("oplata");
		String rodzaj = request.getParameter("rodzaj");
		
		//tworzenie modułu pdf do wdrażania danych do tabeli
		ByteArrayOutputStream rozmiarPDF = new ByteArrayOutputStream();
		Document pdf = new Document();
		pdf.open();
		PdfPTable tabela = new PdfPTable(4);
		
		//sprawdzenie czy coś nie zostało pominięte przy wpisywaniu
		if (kredyt.isEmpty() || raty.isEmpty() || oprocentowanie.isEmpty() || oplata.isEmpty()) {
			request.getRequestDispatcher("/error").forward(request, response);
		}
		try {
			//konwersja Stringów, w razie niepowodzenia catch
			float kredytf = Float.parseFloat(kredyt);
			int ratyi = Integer.parseInt(raty);
			float oprocentowanief = Float.parseFloat(oprocentowanie);
			float oplataf = Float.parseFloat(oplata);
			
			if (kredytf <= 0 || ratyi <= 0 || oprocentowanief <= 0 || oplataf <= 0) {
				request.getRequestDispatcher("/error").forward(request, response);
			}
			//tablica danych
			double[] kapital = new double[ratyi];
			double[] odsetki = new double[ratyi];
			double[] calkowita = new double[ratyi];
			
			//zależność sprowadzana do rodzaju kredytu
			if ("stala".equals(rodzaj)) {
				float y = 1 + (oprocentowanief/1200);
				for (int i = 0; i < ratyi; i++) {
					odsetki[i] = zaokraglanie(kredytf * oprocentowanief * ratyi/(14400));
					calkowita[i] = zaokraglanie((kredytf + Math.pow(y, ratyi) * (y - 1)/(Math.pow(y, ratyi) - 1) + oplataf)/ratyi);
					kapital[i] = zaokraglanie(calkowita[i] - odsetki[i] - oplataf);
					
					//wypisanie danych
					response.getWriter().println("rata nr: " + (i + 1) + " | kapital: " + kapital[i] + " | odsetki: " + odsetki[i] + " | calkowita: " + calkowita[i]);
					response.getWriter().println("-----------------------------------------------------------------------------");
					
					//i dodanie do tabeli w PDF
					tabela.addCell(String.valueOf("rata nr: " + (i + 1)));
					tabela.addCell(String.valueOf("kapital: " + kapital[i]));
					tabela.addCell(String.valueOf("odsetki: " + odsetki[i]));
					tabela.addCell(String.valueOf("calkowita: " + calkowita[i]));
					
				}
			}
			else {
				float pozostalo = 0;
				for (int i = 0; i < ratyi; i++) {
					kapital[i] = zaokraglanie(kredytf/ratyi);
					if (i == 0) {
						odsetki[i] = zaokraglanie(kredytf * (oprocentowanief/1200));
					}
					else {
						pozostalo += kapital[i - 1];
						odsetki[i] = zaokraglanie((kredytf - pozostalo) * (oprocentowanief/1200));
					}
					calkowita[i] = zaokraglanie(kapital[i] + odsetki[i] + oplataf);
					
					//wypisanie danych
					response.getWriter().println("rata nr: " + (i + 1) + " | kapital: " + kapital[i] + " | odsetki: " + odsetki[i] + " | calkowita: " + calkowita[i]);
					response.getWriter().println("-----------------------------------------------------------------------------");
					
					//i dodanie do tabeli w PDF
					tabela.addCell(String.valueOf("rata nr: " + (i + 1)));
					tabela.addCell(String.valueOf("kapital: " + kapital[i]));
					tabela.addCell(String.valueOf("odsetki: " + odsetki[i]));
					tabela.addCell(String.valueOf("calkowita: " + calkowita[i]));
					
				}
			}
			try {
				pdf.add(tabela);
			} 
			catch (DocumentException e) {
				e.printStackTrace();
			}
			pdf.close();
			/*
			response.setContentType("application/pdf");
			response.addHeader("Content-Disposition", "attachement; filename=rezultat.pdf");
			response.setContentLengthLong((byte)rozmiarPDF.size());
			
			byte[] pdfStringToBytes = rozmiarPDF.toByteArray();
			ByteArrayInputStream pdfOut = new ByteArrayInputStream(pdfStringToBytes);
			
			while(pdfOut.read() != -1) {
				response.getOutputStream().write(pdfOut.read());
			}
			*/
			
		}
		catch (NumberFormatException a) {
			request.getRequestDispatcher("/error").forward(request, response);
	}
}
}
	
	
	
	
	
	
	
	
	
