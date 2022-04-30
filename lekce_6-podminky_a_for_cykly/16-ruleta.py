# Na obrázku vidíte rozložení čísel na klasické Francouzské ruletě. Ruleta obsahuje čísla 0 - 36. Každé číslo s výjimkou nuly je buď sudé nebo liché a zároveň červené nebo černé. Pro čísla 1 až 10 a 19 až 28 platí, že lichá čísla jsou červená a sudá jsou černá. Pro zbytek platí obrácené pravidlo, tedy lichá jsou černá a sudá červená. Nula není ani lichá ani sudá, ani černá ani červená.

# Napište program, kterému uživatel zadá číslo a program odpoví jestli jde o číslo sudé nebo liché, černé nebo červené, nebo je to nula.

import sys

number = int(sys.argv[1])

if number < 0 or number > 36:
  print(f"Číslo {number} na ruletě není.")
elif number == 0:
  print(f"Číslo {number} je zelené.")
elif (number > 0 and number < 11) or (number > 18 and number < 29):
  if number % 2 == 0:
    print(f"Číslo {number} je sudé a černé.")
  else:
    print(f"Číslo {number} je liché a červené.")
else:
  if number % 2 == 0:
    print(f"Číslo {number} je sudé a červené.")
  else:
    print(f"Číslo {number} je liché a černé.")