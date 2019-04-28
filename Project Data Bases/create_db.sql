CREATE TABLE instruktorzy
(
	id			serial				,
	imie			varchar(16)			,
	nazwisko		varchar(16)		NOT NULL,
	data_urodzenia		date				,
	wiek			int				,
	adres			varchar(64)			,
	CONSTRAINT		id_instruktora_pk PRIMARY KEY(id),
	CONSTRAINT		instruktorzy_adres_un UNIQUE(adres)
);

CREATE TABLE szkola
(
	id			serial				,
	adres			varchar(64)			,
	miesieczne_koszta	numeric(7,2)			CHECK (miesieczne_koszta >= 0),
	CONSTRAINT		szkola_id_pk PRIMARY KEY(id)	

);

CREATE TABLE kursanci
(
	id			serial				,
	id_szkoly		int				,
	imie			varchar(16)			,
	nazwisko		varchar(16)		NOT NULL,
	data_urodzenia		date				,
	wiek			int				,
	adres			varchar(64)			,
	CONSTRAINT		id_kursanta_pk PRIMARY KEY(id)  ,
	CONSTRAINT		kursanci_adres_un UNIQUE(adres) ,
	CONSTRAINT		kursanci_id_szkoly_fk FOREIGN KEY(id_szkoly)
					REFERENCES szkola(id)
						
);


CREATE TABLE pojazdy
(
	numery_rejestracyjne	varchar(16)		NOT NULL,
	kategoria		char(2)				,
	rodzaj			varchar(16)			,
	marka			varchar(16)			,
	silnik			varchar(32)			,
	skrzynia		varchar(16)			,
	CONSTRAINT		pojazdy_numery_rejestracyjne_pk
					PRIMARY KEY(numery_rejestracyjne),
	CONSTRAINT		pojazdy_numery_rejestracyjne_un UNIQUE(numery_rejestracyjne)
);

CREATE TABLE kurs
(
	id			serial				,
	id_instruktora		int			NOT NULL,
	id_kursanta		int			NOT NULL,
	numery_rejestracyjne_pojazdow varchar(16)	NOT NULL,
	data_rozpoczecia	date				,
	data_zakonczenia	date				,
	CONSTRAINT		kurs_id_pk PRIMARY KEY(id)	,
	CONSTRAINT		id_instruktora_fk FOREIGN KEY(id_instruktora)
					REFERENCES instruktorzy(id),
	CONSTRAINT		id_kursanta_fk FOREIGN KEY(id_kursanta)
					REFERENCES kursanci(id),
	CONSTRAINT		numery_rejestracyjne_pojazdow_fk FOREIGN KEY 							(numery_rejestracyjne_pojazdow)
						REFERENCES pojazdy(numery_rejestracyjne),
	CONSTRAINT		dates CHECK(data_rozpoczecia<=data_zakonczenia)
);











