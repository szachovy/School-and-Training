SET client_encoding TO 'UTF-8';
CREATE LANGUAGE plpgsql;

CREATE TABLE szkola_wydatki(
	id int,
	miesieczne_koszta numeric(7,2),
	"data" timestamp
	
);

CREATE FUNCTION zaktualizuj()
	RETURNS TRIGGER AS $$
BEGIN
	IF old.miesieczne_koszta<>new.miesieczne_koszta
	THEN INSERT INTO szkola_wydatki VALUES (old.id, new.miesieczne_koszta, current_timestamp);
	RAISE NOTICE 'miesieczne wydatki szkoly o id %',old.id;
	RAISE NOTICE 'zostaly zmienione o %',new.miesieczne_koszta-old.miesieczne_koszta;
	END IF;
	RETURN NULL;
END
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER zaktualizuj
	AFTER UPDATE ON szkola
	FOR EACH ROW EXECUTE PROCEDURE zaktualizuj();

UPDATE szkola SET miesieczne_koszta = miesieczne_koszta + 140 WHERE id = 1;


--projekt czas_wykonania
CREATE TABLE kursy_ukonczone(
	id int,
	czas_trwania_w_dniach int
);
CREATE FUNCTION czas_trwania()
	RETURNS TRIGGER AS $$
BEGIN
	IF ((new.data_rozpoczecia IS NULL) OR (new.data_zakonczenia IS NULL)) 
	THEN
	--jesli start lub koniec NULL, to ustaw czas_wykonania na NULL
		RAISE NOTICE 'Kurs się nie rozpoczął lub nie zakończył';
		INSERT INTO kursy_ukonczone VALUES(old.id,NULL);
	ELSIF ((new.data_rozpoczecia <> old.data_zakonczenia) 
		OR (new.data_rozpoczecia <> old.data_zakonczenia)) 
	THEN
		--jesli zmienil sie koniec lub start, to aktualizacja czasu wykonania
		RAISE NOTICE 'zmiana czasu_trwania_kursu';
		INSERT INTO kursy_ukonczone VALUES(old.id,new.data_zakonczenia::date - 				new.data_rozpoczecia::date);
	END IF;
	RETURN new;
END
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER czas_trwania
	BEFORE INSERT OR UPDATE ON kurs 
FOR EACH ROW EXECUTE PROCEDURE czas_trwania();

UPDATE kurs SET data_zakonczenia='2018-04-25' WHERE id=15;
UPDATE kurs SET data_zakonczenia='2018-01-22' WHERE id=7;
UPDATE kurs SET data_rozpoczecia='2017-11-14', data_zakonczenia='2018-03-30' WHERE id = 1;

CREATE TABLE przeglady(
	numery_rejestracyjne varchar(64),
	status varchar(16)
);

ALTER TABLE pojazdy ADD ostatni_przeglad timestamp;

CREATE FUNCTION dodaj_przeglad()
	RETURNS TRIGGER AS $$
BEGIN
	IF new.status = 'pozytywny'
	THEN
	RAISE NOTICE 'dodana data przeglądu %',current_timestamp;
	UPDATE pojazdy SET ostatni_przeglad = current_timestamp 					WHERE numery_rejestracyjne = new.numery_rejestracyjne;
	ELSE
	RAISE NOTICE 'pojazd nie przeszedł przeglądu';
	END IF;
	RETURN NULL;
END
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER dodaj_przeglad
	AFTER UPDATE ON przeglady
FOR EACH ROW EXECUTE PROCEDURE dodaj_przeglad();

UPDATE przeglady SET numery_rejestracyjne='ZXCF-148-C5',status='pozytywny';
UPDATE przeglady SET status='negatywny' WHERE numery_rejestracyjne='DB2E-3R4-FV';

SELECT * FROM dodaj_przeglad('ZXCF-148-C5','pozytywny');

CREATE VIEW roczne_koszta_szkoly AS 
	SELECT *,miesieczne_koszta*12 AS roczne_koszta FROM szkola;





