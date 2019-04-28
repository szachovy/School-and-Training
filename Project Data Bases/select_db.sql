
--zapytania z usuwaniem tabeli sa w pliku drop_db.sql

--znajdz instruktora ktory w tej chwili nie prowadzi kursow

SELECT id,imie,nazwisko FROM instruktorzy
	WHERE id NOT IN 
		(SELECT id_instruktora FROM kurs)
		ORDER BY id;



--wyswietl instruktorow ktorzy prowadza wiecej niz jeden kurs

SELECT * FROM instruktorzy
	WHERE id IN (SELECT id_instruktora FROM kurs
		GROUP BY id_instruktora HAVING count(id_instruktora) > 1);



--sprawdz jacy kursanci nie maja przydzielonego instruktora

SELECT * FROM kursanci
	WHERE NOT EXISTS( SELECT * FROM instruktorzy
		INNER JOIN kurs ON kursanci.id = kurs.id_kursanta
			AND instruktorzy.id = kurs.id_instruktora);




--znajdz kursantow ktorzy nie maja przydzielonej szkoly

SELECT kursanci.id, imie, nazwisko FROM kursanci, szkola
	WHERE kursanci.id_szkoly = szkola.id
	ORDER BY nazwisko;



--znajdz kursantow ktorzy maja podana date urodzenia ale wiek nie zostal zaktualizowany

SELECT * FROM kursanci WHERE data_urodzenia IS NOT NULL AND wiek IS NULL;



--wyswietl czas_trwania kursow ktory trwal dluzej niz 5 miesiecy
--kolejnoscia ktory trwal najdluzej

SELECT *,(data_zakonczenia - data_rozpoczecia) AS czas_trwania FROM kurs
	WHERE data_rozpoczecia IS NOT NULL AND data_zakonczenia IS NOT NULL
		AND (data_zakonczenia - data_rozpoczecia)>150
			ORDER BY czas_trwania DESC;



--wypisz informacje o pojazdach kategorii B lub pojazdach
--ktorych numery rejestracyjne zaczynaja sie od literki "C"

SELECT * FROM pojazdy WHERE numery_rejestracyjne LIKE 'C%'
UNION ALL
SELECT * FROM pojazdy WHERE kategoria = 'B';



--oblicz ile pieniedzy w rok wyda szkola na Kurzyńskiego 

SELECT *,(miesieczne_koszta * 12) AS roczne_koszta FROM szkola
	WHERE adres LIKE '%Kurzyńskiego%';



--zaktualizuj miesieczne_koszta szkoły z Wejcherowa na '13256.23'

UPDATE szkola SET miesieczne_koszta = 13256.23 WHERE id = 4;




