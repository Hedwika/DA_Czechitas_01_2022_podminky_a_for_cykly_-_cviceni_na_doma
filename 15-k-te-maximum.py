# Napište program, který dostane na příkazové řádce posloupnost čísel. První číslo udává, kolikáté největší číslo chceme ve zbytku zadaných čísel najít. Můžeme tak chtít třeba páté největší číslo z 6, 1, 3, 8, 4, 7, 2

# $ python3 kmax.py 5 6 1 3 8 4 7 2
# 3

# Pokud je nějaké číslo v seznamu dvakrát, bere se jako dvě různá maxima. Nepoužívejte žádné Python funkce typu sorted nebo max. Napište všechno pěkně od píky.

# Možností, jak tento úkol vyřešit, je více. Nebojte se zagooglit, nebojte se být kreativní.

import sys

seznam = [int(c) for c in sys.argv[1:]]

kolikate_nejvyssi_cislo = seznam[0]
seznam.pop(0)

for cislo in range(len(seznam)):
  for nasledujici_cislo in range(len(seznam)):
    if seznam[cislo] > seznam[nasledujici_cislo]:
      seznam[nasledujici_cislo],seznam[cislo] = seznam[cislo],seznam[nasledujici_cislo]

if kolikate_nejvyssi_cislo > len(seznam):
  print(f"ERROR: Čísel máme v seznamu méně než {kolikate_nejvyssi_cislo}.")
else:
  index_hledaneho_cisla = kolikate_nejvyssi_cislo - 1
  print(f"{kolikate_nejvyssi_cislo}-té nejvyšší číslo ze seznamu je {seznam[index_hledaneho_cisla]}.")