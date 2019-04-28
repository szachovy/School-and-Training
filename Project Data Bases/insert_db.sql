SET DATESTYLE TO 'European,German';

--stan bazy na dnia 1 maja 2018 roku

INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Rafał','Strzelisty','07-01-1993',25,'Chodkiewicza 13 Gdynia');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Adam','Dackiewicz','27-04-1998',20,'Skrzaczkowskiego 14a Wejcherowo');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Dominika','Bułecka-Górna','13-11-1992',25,'Białego Wilka 21/4 Sopot');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Paweł','Paprocki','26-03-1994',24,'Chodkiewicza 17 Gdynia');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Rafał','Przydawka','30-09-1996',21,'Cerrery 13a/5 Sopot');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Filip','Bączkowski','14-07-1995',NULL,'Jana Pawła 6/9 Sopot');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Katarzyna','Mączyńska','07-01-1993',25,'Chodkiewicza 13 Kartuzy');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Alicja','Pawłowska-Hulaj','22-06-1991',NULL,'Diesla 33 Gdańsk');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Grażyna','Aleurwał','01-05-1997',21,'Chłystka 23/1 Gdańsk');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Andrzej','Nieszczęsny',NULL,NULL,NULL);
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Zygmunt','Suse','13-02-1993',25,'Głuszyńskiego 7 Prusz-Gdański');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Kamila','Cyps','20-08-1989',NULL,'Szybkiego 3 Gdynia');
INSERT INTO instruktorzy(imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES ('Andrzej','Grosicki','29-01-1996',22,NULL);



INSERT INTO szkola(adres,miesieczne_koszta)
	VALUES ('Kurzyńskiego 25 Gdańsk',50043.21);
INSERT INTO szkola(adres,miesieczne_koszta)
	VALUES ('Jabłkowska 1 Gdańsk',64827.01);
INSERT INTO szkola(adres,miesieczne_koszta)
	VALUES ('Sypka 6 Gdynia',28944.88);
INSERT INTO szkola(adres,miesieczne_koszta)
	VALUES ('Szczepana 6 Wejcherowo',NULL);




INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (4,'Jakub','Poziomka','16-03-1994',24,'Chłopska 16 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (3,'Alfred','Jarzębowski',NULL,NULL,'Wiejska 1/6 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (1,'Janina','Słowacka','11-02-1995',23,'Kazimierza 17a Gdynia');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (2,'Pola','Książkiewicz','05-05-1998',19,'Awangardowa 18/2 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (4,'Piotr','Rostkowski','14-03-1998',20,'Szwajcarska 18 Sopot');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (1,'Dawid','Czerwiec','09-09-1999',NULL,'Polna 13b Wejcherowo');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (2,'Patrycja','Super','11-01-1974',44,'Drzewiasta 3b Rumia');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (NULL,'Elżbieta','Rozmiarek','30-12-1989',28,'Balczyńskiego 14 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (2,'Dominik','Kieszkowski','28-07-1990',NULL,'Chodkiewicza 17 Kartuzy');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (3,'Patrycja','Radomska','14-02-2000',18,'Narutowicza 15a Gdynia');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (2,'Paweł','Cacha','03-11-1997',20,'Białego Wilka 21/4 Sopot');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (1,'Jakub','Krotowski','16-02-1999',19,'Chłopska 17 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (4,'Jakub','Sawicki','19-03-1997',21,NULL);
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (NULL,'Piotr','Super','08-12-1998',19,'Jana Pawła 6/8 Sopot');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (NULL,'Michał','Cholewa',NULL,NULL,'Będzyńska 14 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (1,'Adam','Utopski','16-03-1996',NULL,NULL);
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (2,'Adam','Wektorowy','16-03-1996',22,'Szostakiewicza 9a Gdynia');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (2,'Seweryn','Krajek','28-01-1988',30,'Małopolska 15c Reda');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (3,'Oliwia','Gruszka-Niepodam','10-04-1998',20,NULL);
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (1,'Wiktor','Żubrówka','01-03-2000',18,'Brukowska 11a Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (4,'Mariusz','Soplica','30-04-1999',19,'Świetlicka 7/2 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (4,'Agata','Żołądkowa-Gorzka','21-10-1999',18,NULL);
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (4,'Jan','Absolwent','24-02-2000',18,'Słowackiego 32 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (1,'Krzysztof','Absolut','16-05-1997',NULL,'Świecka 3a Wejcherowo');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (1,'Anna','Jager-Meister','11-09-1999',18,'Małopolska 13b Reda');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (4,'Krzysztof','Żubrówka','12-02-1995',23,'Chłopska 10 Gdańsk');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (3,'Jan','Księżycowy','10-07-1994',23,'Nowa 2a Kartuzy');
INSERT INTO kursanci(id_szkoly,imie,nazwisko,data_urodzenia,wiek,adres)
	VALUES (3,'Jakub','Jakubkiewicz','12-03-1998',20,'Będzyńska 11 Gdańsk');



INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('ZXCF-148-C5','B','Auto_Osobowe','Toyota','1.0 VVT-i','manualna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('DB2E-3R4-FV','B','Auto_Osobowe','Kia','1.2 CVVT','manualna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('FG44-66Y-2E','B','Auto_Osobowe','Toyota',NULL,NULL);
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('M7NI-OP8-T5','C','Ciężarówka','MAN','4.0 D2066LF57 EEV','manualna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('FVG4-D3A-RR','B','Auto_Osobowe','Toyota','1.0 VVT-i','automatyczna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('EX21-676-T6','D','Autobus','Solaris','3.5 DAF MX-11','manualna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('ERD2-7YY-UI','C','Ciężarówka','Scania','9.0 SCX-243EA','manualna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('CX2R-TUY-PO','D','Autobus',NULL,NULL,NULL);
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('CVF1-BN4-21','A','Motocykl','Honda','0.7 CXX-09',NULL);
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('GZ3R-P9T-LO','B','Auto_Osobowe','Toyota','1.0 VVT-i','manualna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('CH3M-OD0-DA','B','Auto_Osobowe','Kia','1.2 CVVT','manualna');
INSERT INTO pojazdy(numery_rejestracyjne,kategoria,rodzaj,marka,silnik,skrzynia)
	VALUES ('3RA1-DEV-44','B','Auto_Osobowe','Kia','1.2 CVVT','automatyczna');



INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (1,3,'DB2E-3R4-FV','04-01-2018','28-04-2018');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (2,1,'ZXCF-148-C5','18-03-2017','23-08-2017');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (2,7,'EX21-676-T6','12-12-2017','13-03-2018');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (3,5,'ERD2-7YY-UI','16-05-2017','19-11-2017');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (5,8,'CH3M-OD0-DA','12-08-2017','01-01-2018');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (5,9,'CVF1-BN4-21','18-02-2018',NULL);
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (5,16,'CX2R-TUY-PO',NULL,NULL);
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (6,12,'ERD2-7YY-UI','04-05-2017','28-09-2017');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (7,20,'DB2E-3R4-FV','30-01-2018',NULL);
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (7,13,'GZ3R-P9T-LO','08-08-2017','01-02-2018');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (8,17,'FG44-66Y-2E','30-12-2016','21-06-2017');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (9,14,'3RA1-DEV-44','14-04-2018',NULL);
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (10,23,'FVG4-D3A-RR','26-12-2016','30-04-2017');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (12,21,'CH3M-OD0-DA','07-10-2017','20-02-2018');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (12,28,'DB2E-3R4-FV',NULL,NULL);
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (12,26,'M7NI-OP8-T5','29-09-2017','23-01-2018');
INSERT INTO kurs(id_instruktora,id_kursanta,numery_rejestracyjne_pojazdow,data_rozpoczecia,data_zakonczenia)
	VALUES (13,27,'CX2R-TUY-PO','14-03-2018',NULL);





