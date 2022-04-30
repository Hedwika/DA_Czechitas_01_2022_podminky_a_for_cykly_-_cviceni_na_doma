# Napište program, který z textového souboru přečte seznam zůstatků na spořících účtech a vypíše tyto zůstatky navýšené o 2.5% úrok.

with open('9-zustatky.txt', encoding='utf-8') as vstup:
  zustatky = vstup.readlines()

zustatky_float = [float(radek) for radek in zustatky]
print(zustatky_float)

# Vypište každý navýšený zůstatek na samostatný řádek.
for cislo in zustatky_float:
  print(cislo)

# Vypište jen ty zůstatky, které nejsou záporné.
for cislo in zustatky_float:
  if cislo >= 0:
    print(cislo)

# Zkuste jednotlivé řádky očíslovat. Každý řádek tedy bude obsahovat číslo řádku a výsledný zůstatek.
cislo_radku = 1

for cislo in zustatky_float:
  print(f"{cislo_radku}: {cislo}")
  cislo_radku += 1