# busy z narciarzami jadacymi na stok
# # nieznana liczba narciarzy - wczytywana na poczatku
# do kazdego busa moze zmiescic sie maksymalnie 10 par nart,
#     niektorzy wiozą 1, 2 lub 3 pary nart -> losowa liczba dla kazdego narciarza
# powiedz w ilu busach pojadą narciarze

# python program.py arg1 arg2 < test_input.txt
# Get-Content test_input.txt | python program.py arg1 arg2

import sys
import random

if sys.argv[1] == "INP":
    liczba_narciarzy = int(input("Liczba narciarzy: "))
else:
    liczba_narciarzy = int(sys.argv[1])

print(f"Wybrana liczba narciarzy: {liczba_narciarzy}")

MAKSYMALNA_LICZBA_NART_W_BUSIE = 10

liczba_nart_w_busie = 0
liczba_busow_wyslanych = 0
najwieksza_liczba_nart_w_busie = 0
numer_najbardziej_obladowanego_busa = None

for narciarz in range(liczba_narciarzy):
    while True:
        # liczba_nart_narciarza = int(input(f"Narciarz {narciarz} liczba par nart: "))
        liczba_nart_narciarza = random.randint(1, 3)
        if 1 <= liczba_nart_narciarza <= 3:
            break
        print("Podaj prawidlowa liczba nart, miedzy 1 a 3.")
    print(f"Narciarz {narciarz} ma {liczba_nart_narciarza} par nart.")

    if liczba_nart_w_busie + liczba_nart_narciarza > MAKSYMALNA_LICZBA_NART_W_BUSIE:
        print(f"Bus odjezdza z {liczba_nart_w_busie} parami nart!")
        print(f"Pozostala liczba miejsc na narty w busie: {MAKSYMALNA_LICZBA_NART_W_BUSIE - liczba_nart_w_busie}")
        liczba_busow_wyslanych += 1
        if liczba_nart_w_busie > najwieksza_liczba_nart_w_busie:
            najwieksza_liczba_nart_w_busie = liczba_nart_w_busie
            numer_najbardziej_obladowanego_busa = liczba_busow_wyslanych
            print(f"Nowa najwieksza liczba nart w busie: {najwieksza_liczba_nart_w_busie}")
        liczba_nart_w_busie = 0

    liczba_nart_w_busie += liczba_nart_narciarza

if liczba_nart_w_busie > 0:
    print(f"Ostatni bus odjezdza z {liczba_nart_w_busie} parami nart!")
    print(f"Pozostala liczba miejsc na narty w busie: {MAKSYMALNA_LICZBA_NART_W_BUSIE - liczba_nart_w_busie}")
    liczba_busow_wyslanych += 1
    if liczba_nart_w_busie > najwieksza_liczba_nart_w_busie:
        najwieksza_liczba_nart_w_busie = liczba_nart_w_busie
        numer_najbardziej_obladowanego_busa = liczba_busow_wyslanych
        print(f"Nowa najwieksza liczba nart w busie: {najwieksza_liczba_nart_w_busie}")

print("\nPOSUMOWANIE:")
print(f"Liczba wyslanych busow: {liczba_busow_wyslanych}")
print(f"Najwieksza liczba par nart w busie: {najwieksza_liczba_nart_w_busie}")
print(f"Numer busa najbardziej obladowanego: {numer_najbardziej_obladowanego_busa}")