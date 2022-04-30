# Zkuste napsat program, který na vstupu obdrží seznam čísel a najde mezi nimi nejvyšší číslo. Pozor, bez použití funkce max().

import sys

cisla = [int(c) for c in sys.argv[1:]]

nejvyssi_cislo = 0

for prvek in cisla:
  if prvek > nejvyssi_cislo:
    nejvyssi_cislo = prvek

print(f"Nejvyšší číslo je {nejvyssi_cislo}.")