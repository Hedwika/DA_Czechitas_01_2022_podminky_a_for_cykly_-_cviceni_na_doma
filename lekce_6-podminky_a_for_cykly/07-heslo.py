import sys

uzivatelske_jmeno = sys.argv[1]
heslo = sys.argv[2]

spravne_heslo = "ahoj_svete"

if heslo == spravne_heslo:
  print(f"Přístup uživateli '{uzivatelske_jmeno}' povolen.")
else:
  print("Přístup odepřen.")