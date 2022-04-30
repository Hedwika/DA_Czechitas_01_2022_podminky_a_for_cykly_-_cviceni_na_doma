# Napište program, který o zadaném seznamu celých čísel rozhodne, zda jsou čísla v tomto seznamu vzestupně seřazena.

vzestupny_seznam = [1, 2, 3, 4, 5]
sestupny_seznam = [5, 4, 3, 2, 1]
vzestupny_seznam_s_nulou = [-2, -1, 0, 1, 2]
sestupny_seznam_s_nulou = [2, 1, 0, -1, -2]
prehazeny_seznam = [9, -2, -78, 65, 0]

# Do proměnné seznam si uložte ten seznam, který chcete otestovat:
seznam = 

for cislo in seznam:
  index_cisla = seznam.index(cislo)
  if cislo == seznam[-1]:
    pass
  else:
    index_dalsiho_cisla = index_cisla + 1
    if seznam[index_cisla] > seznam[index_dalsiho_cisla]:
      print("Nejedná se o vzestupný seznam!")
      quit()
print("Jedná se o vzestupný seznam.")