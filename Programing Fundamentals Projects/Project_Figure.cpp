#define _CRT_SECURE_NO_WARNINGS       //dla niestandardowych bledow

#include "stdafx.h"     // podstawowe biblioteki dla uzytych funkcji
#include<iostream>        
#include<conio.h>         
#include<Windows.h>
#include <limits>

HANDLE hOut; //do zmiany koloru tekstu lub tla

#define ESC 27   //kod do znaku wyjscia z programu
#define SCREENWIDTH 160     //bufor dla szerokosci ekranu
#define SCREENHEIGHT 40     //bufor dla wysokosci ekranu
#define MINIMUMSIZEOFCHAR 0     //minimalna mozliwa wielkosc rysowanego znaku
#define MAXIMUMSIZEOFCHAR 7     //maksymalna mozliwa wielkosc rysowanego znaku

using namespace std;   

void gotoxy(int x, int y);       //funkcja wyrazajaca wspolrzedne kursora

void HideCursor();         //funkcja chowajaca kursor

bool menu(int &size, char &ascii);       //menu

void rysuj(int &size, int *refx, int *refy, char ascii); //fukcja rysujaca zadany kod

int main()
{
	int size, refx, refy;
	char ascii;
	int znak = 0;
	refx = 0;   //punkt startowy x
	refy = 0;   //punkt startowy y

	HideCursor();   //znikniecie kursora

	menu(size,ascii);   //menu

	system("cls");   //czyszczenie ekranu

	rysuj(size, &refx, &refy,ascii);   //pierwszy znak

	do
	{
#pragma warning(disable : 4996)   //gdyby nie dzialal getch();
		znak = getch();
			switch (znak)  //poruszanie sie
			{
			case 0:    //0 lub 224 zalezy od architektury systemu
			case 224:
				znak = getch();
				switch (znak)
				{
				case 72: //strzałka w górę
				{
					if (refy <= 0)      // wytyczne dla nie wychodzenia poza ekran musza byc spelnione
					{
						system("cls");
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
					}
					else
					{
						system("cls");
						refy--;     // przemieszczanie sie za pomoca zmiany wskaznika na zmienne w funckji
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
					}
				}
				case 80: //strzałka w dół
				{
					if (refy>=SCREENHEIGHT)  // wytyczne dla nie wychodzenia poza ekran musza byc spelnione
					{
						system("cls");
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
					}
						system("cls");
						refy++;   // przemieszczanie sie za pomoca zmiany wskaznika na zmienne w funckji
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
				}
				case 75: //strzałka w lewo
				{

					if (refx <= 0)   // wytyczne dla nie wychodzenia poza ekran musza byc spelnione w przypadku nie spelnienia pozostawia co bylo
					{
						system("cls");
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
					}
					else
					{
						system("cls"); 
						refx--;   // przemieszczanie sie za pomoca zmiany wskaznika na zmienne w funckji
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
					}
				}
				case 77: //strzałka w prawo
				{

					if (refx>=SCREENWIDTH)   // wytyczne dla nie wychodzenia poza ekran musza byc spelnione w przypadku nie spelnienia pozostawia co bylo
					{
						system("cls");
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
					}
					else
					{
						system("cls");
						refx++;   // przemieszczanie sie za pomoca zmiany wskaznika na zmienne w funckji
						HideCursor();
						rysuj(size, &refx, &refy,ascii);
						break;
					}
				}
				}
				znak = 0;    //zerowanie
				break;
			case '+':   //zwiekszanie znaku poprzez size dla wytycznych rozmiarow
			{
				if (size >= MAXIMUMSIZEOFCHAR)   // wytyczne dla nie wychodzenia poza ekran musza byc spelnione w przypadku nie spelnienia pozostawia co bylo
				{
					system("cls");
					HideCursor();
					rysuj(size, &refx, &refy,ascii);
					break;
				}
				system("cls");
				size++;    //zwiekszenie rozmiaru figury o 1
				HideCursor();
				rysuj(size, &refx, &refy,ascii);
				break;
			}
			case '-': //zwiekszanie znaku poprzez size dla wytycznych rozmiarow
			{
				if (size <= MINIMUMSIZEOFCHAR)    // wytyczne dla nie wychodzenia poza ekran musza byc spelnione w przypadku nie spelnienia pozostawia co bylo
				{
					system("cls");
					HideCursor();
					rysuj(size, &refx, &refy,ascii);
					break;
				}
				else
				{
					system("cls");
					size--;   //zmniejszenie rozmiaru figury o 1
					HideCursor();
					rysuj(size, &refx, &refy,ascii);
					break;
				}
			}
			case 'n':  //nowy rozmiar figury dla spelnionych zalozen
			{
				system("cls");
				cout << "nowy rozmiar figury : ";
				cin >> size;
				if (size > MAXIMUMSIZEOFCHAR)    //jezeli podany rozmiar wiekszy niz maksymalny mozliwy to daj najwiekszy mozliwy
				{
					size = MAXIMUMSIZEOFCHAR;
				}
				if (size < MINIMUMSIZEOFCHAR)   //jezeli podany rozmiar mniejszy niz maksymalny mozliwy to daj najmniejszy mozliwy
				{
		    		size = MINIMUMSIZEOFCHAR;
				}
					system("cls");
					HideCursor();
					rysuj(size, &refx, &refy,ascii);
					break;
			}
			}
	} while (znak != ESC);    //wyjscie z programu
}

void gotoxy(int x, int y)         //funkcja wyrazajaca wspolrzedne kursora
{
	COORD c;
	c.X = x;
	c.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}


void HideCursor()          //funkcja chowajaca kursor
{
	::HANDLE hConsoleOut = ::GetStdHandle(STD_OUTPUT_HANDLE);
	::CONSOLE_CURSOR_INFO hCCI;
	::GetConsoleCursorInfo(hConsoleOut, &hCCI);
	hCCI.bVisible = FALSE;
	::SetConsoleCursorInfo(hConsoleOut, &hCCI);
}
bool menu(int &size, char &ascii)       //menu
{
	int s;

	hOut = GetStdHandle(STD_OUTPUT_HANDLE);   //standardowe wyjscie kolorow w konsoli


	SetConsoleTextAttribute(hOut, FOREGROUND_GREEN);      //ustawienie koloru
	cout << "\n\n\tRysowanie figury podanym znakiem ASCII\n\n";

	SetConsoleTextAttribute(hOut, FOREGROUND_RED);   //zmiana koloru

	cout << " Autor : ***\n"
		<< " - wybor znaku kodu ASCII\n"
		<< " - wczytanie poczatkowych rozmiarow figury\n"
		<< " - przesuwanie figury strzalkami\n"
		<< " - powiekszanie i zmniejszanie figury za pomoca klawiszy + i -"
		<< " - ograniczenie przesuwania i rozmiarow figury od obszaru ekranu\n"
		<< " - figura to znak 'z' z kropka w prawym gornym rogu\n\n";


	SetConsoleTextAttribute(hOut, FOREGROUND_RED);   //zmiana koloru
	do   //dla zle wpisanego rozmiaru powrot
	{
		do
		{
			cout << "Wpisz poczatkowy rozmiar figury od " << MINIMUMSIZEOFCHAR << " do " << MAXIMUMSIZEOFCHAR << "  : ";
			cin >> size;
			if ((s = cin.fail()) == true)   //sprawdzenie czy zosala wpisana liczba
			{
				cout << "to nie liczba" << endl;
				cin.clear();
				cin.ignore(INT_MAX, '\n');
			}
		} while (s);
	} while (size < MINIMUMSIZEOFCHAR || size > MAXIMUMSIZEOFCHAR);

	cout << "Jakim znakiem ASCII ma byc narysowana figura : ";
	cin >> ascii;
	return true;    //dla dobrze podanych informacji przejscie dalej..
}


void rysuj(int &size, int *refx, int *refy, char ascii) //fukcja rysujaca zadany kod
{
	int x = *refx;   //zmienne na wskaznik w mainie
	int y = *refy;   //zmienne na wskaznik w mainie

	char tab[100][100];        //tablica statyczna
							   /*  tablica dynamiczna UWAGA RYZYKO WYSTAPIENIA BLEDU PRZY SZYBKICH ZMIANACH
							   char **tab = new char *[size];
							   for (int j = 0; j < size; j++)
							   {
							   tab[j] = new char[size];
							   }
							   */
	gotoxy(x, y);   //punkt poczatkowy gwiazdka
	tab[0][0] = '*';
	cout << tab[0][0];

	//dalsze rysowanie znaku 

	for (int i = 0; i < size*size; i++)    //wypelnienie 'sufitu' znaku
	{
		gotoxy(x + 1, y);    
		tab[0][i] = ascii;
		cout << tab[0][i];
		x++;
	}
	x = *refx;  //po zmianie wspolrzednych powrot do zmiennych poczatkowych
	y = *refy;
	for (int j = 0; j < size; j++)
	{
		for (int i = 0; i < size; i++)       //ukos znaku
		{
			gotoxy(x, y + 1);
			tab[j][i] = ascii;
			cout << tab[j][i];
			x++;
			y++;
		}
	}
	x = *refx;     //po zmianie wspolrzednych powrot do zmiennych poczatkowych
	y = *refy;
	for (int i = 0; i < size*size; i++)    //podloga znaku
	{
		gotoxy(x, size*size + y);
		tab[0][i] = ascii;
		cout << tab[0][i];
		x++;
	}
	x = *refx;  //po zmianie wspolrzednych powrot do zmiennych poczatkowych
	y = *refy;
}
