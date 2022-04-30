# Zkuste napsat program, který na vstupu obdrží seznam čísel a najde mezi nimi druhé nejvyšší číslo. Opět bez použití funkce max().

import sys

cisla = [int(c) for c in sys.argv[1:]]

nejvyssi_cislo = 0
druhe_nejvyssi_cislo = 0

for prvek in cisla:
  if prvek > nejvyssi_cislo:
    druhe_nejvyssi_cislo = nejvyssi_cislo
    nejvyssi_cislo = prvek
  elif prvek > druhe_nejvyssi_cislo:
    druhe_nejvyssi_cislo = prvek

print(f"Druhé nejvyšší číslo je {druhe_nejvyssi_cislo}.")