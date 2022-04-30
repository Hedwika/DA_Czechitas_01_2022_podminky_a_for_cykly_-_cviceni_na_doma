import sys

mena = sys.argv[1]
castka = float(sys.argv[2])

usd_eur = 0.95
usd_czk = 23.33

if mena == "czk":
  print(f"{castka} {mena} je {round(castka/usd_czk, 2)} dolarů.")
elif mena == "eur":
  print(f"{castka} {mena} je {round(castka/usd_eur, 2)} dolarů.")
else:
  print(f"{mena} zatím převést neumíme. :(")