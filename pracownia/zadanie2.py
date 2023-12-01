"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 2"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela, pagerank, potegowa
import numpy as np

class Zadanie2:

    def __init__(self):
        """Konstruktor"""
        self.k = 5            # liczba pomiarow dla jednej wartosci parametru
        
    def testy(self):
        """Testy wstepne"""
        # miejsce na rozwiazanie pierwszej czesci zadania 2
        
        return 0
        
    def badaj_zbieznosc(self, epsilon = 1e-7):
        """Badam zbieznosc metody iteracji prostej"""
        # ustalam zbior parametrow
        # zmieniam je w skali logarytmicznej
        param = [1e-9, 1e-7, 1e-5, 1e-3, 0.1, 10, 1e3, 1e5, 1e7, 1e9]
        # okreslam uklad rownan
        u1 = uklad.Uklad(wymiar = self.n)
        # dla kazdej wartosci parametru przeprowadzam po k testow
        # i wyswietlam wartosci wybranych charakterystyk eksperymentu
        sr_liczba_iteracji = []
        sr_norma_macierzy = []
        sr_norma_X0 = []
        sr_niedokladnosc = []
        for sk in param:
            norma_macierzy = 0.0
            liczba_iteracji = 0.0
            norma_X0 = 0.0
            niedokladnosc = 0.0
            iteracje = 0
            while iteracje < self.k:
                # losujemy uklad
                u1.losuj_uklad_symetryczny_dodatnio_okreslony()
                # rozwiazuje uklad z wykorzystaniem metody iteracji prostej
                test1 = iteracjaprosta.IteracjaProsta(ukl = u1)
                # wyznaczam macierz D i wektor C
                test1.przygotuj()
                # obliczam norma macierzy D
                norma_D = u1.norma_macierzy(
                        typ = self.norma,
                        macierz = test1.D
                    )
                # losuje wektor poczatkowy
                wek = np.random.random([self.n, 1])
                # obliczam norme tego wektora
                norma_wek = u1.norma_wektora(typ = self.norma, wektor = wek)
                # skaluje wylosowany wektor
                wek *= sk/norma_wek
                norma_wek = u1.norma_wektora(typ = self.norma, wektor = wek)
                # wykonuje iteracje do momentu, gdy norma roznicy kolejnych
                # przyblizen jest mniejsza niz zadany eps
                iter = test1.iteruj_roznica(
                    eps = epsilon,
                    norma = self.norma,
                    wyswietlaj = 0,
                    X0 = wek)
                niedokl = test1.sprawdz_rozwiazanie(norma = self.norma)
                if iter == 0:
                    # jezeli nie mozna bylo wykonac iteracji
                    # nalezy powtorzyc pomiar
                    continue
                else:
                    # jezeli eksperyment udalo sie przeprowadzic
                    # agregujemy charakterystyki
                    norma_macierzy += norma_D
                    norma_X0 += norma_wek
                    niedokladnosc += niedokl
                    liczba_iteracji += iter
                    iteracje += 1
            # obliczam srednie wartosci charakterystyk
            sr_norma_macierzy.append(norma_macierzy/self.k)
            sr_norma_X0.append(norma_X0/self.k)
            sr_liczba_iteracji.append(liczba_iteracji/self.k)
            sr_niedokladnosc.append(niedokladnosc/self.k)
        # wypisujemy srednie charakterystyki
        print("||X0|| \t \t ||D|| \t     Iteracje   Niedkoladnosc")
        print("------"*9)
        for i in range(len(param)):
            wyniki = f"{sr_norma_X0[i]:.2e} \t"
            wyniki += f"{sr_norma_macierzy[i]:.6f} \t"
            wyniki += f"{sr_liczba_iteracji[i]:.2f} \t"
            wyniki += f"{sr_niedokladnosc[i]:.6e} \n"
            print(wyniki)
        """Badam zbieznosc metody iteracyjnej"""
        # miejsce na realizacje eksperymentu - drugiej czesci zadania 2

        return 0
