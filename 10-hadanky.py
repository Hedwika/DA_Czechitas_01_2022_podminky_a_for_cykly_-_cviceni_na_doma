cisla = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]
sum = 0
for cislo in cisla:
  sum = sum + cislo
  if cislo == 0:
    print(sum)
    sum = 0

# Odpověď:
# TLDR: Přičti číslo k sum. Když narazíš na 0, vytiskni sum a vynuluj sum

# Delší verze: Máme seznam čísel a proměnnou sum s hodnotou 0. Použitý for cyklus vezme každé číslo ze seznamu a přičte k němu hodnotu uloženou v proměnné sum. Výsledek uloží opět do proměnné sum, čili přepíše hodnotu, která v sum byla před tím. Následně se podívá, zda je číslo, se kterým momentálně pracujeme, rovno nule:
# - Pokud ano, vytiskne momentální hodnotu uloženou do proměnné sum a nastaví hodnotu uloženou v proměnné sum na nulu.
# - Pokud ne, posune se na další číslo v seznamu.
# Výsledkem jsou tedy čísla:
# - 15 - to je součet prvních tří elementů ze seznamu (3 + 5 + 8) než narazil na první nulu a sum nastavil na nulu.
# - 6 - součet 4 + 2
# - 15 - součet 7 + 6 + 2
# Poslední prvek v seznamu, číslo 5, se nám nevytiskne, protože po něm už nula nenásleduje. Ve for cyklu máme tisk nastaven pouze v případě, že narazíme na nulu.

cisla = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]
index = 0
for cislo in cisla:
  if index % 2 == 0:
    print(cislo)
  index +=  1

# Odpověď:
# TLDR: Vezmi číslo ze seznamu. Jestli se zbytek po dělení indexu 2 roven nule, vytiskni číslo ze seznamu. Přičti k indexu jedničku a pokračuj dalším čslem ze seznamu.

# Delší verze: Máme seznam čísel a proměnnou index s hodnotou 0. Použitý for cyklus vezme každé číslo ze seznamu a nic s ním nedělá. Místo toho se podívá, zda je hodnota uložená v proměnné index dělitelná dvěma beze zbytku:
# - Pokud ano, vytiskne číslo ze seznamu, se kterým momentálně pracuje. A navýší hodnotu čísla uloženého v proměnné index o 1.
# - Pokud ne, navýší hodnotu čísla uloženého v proměnné index o 1.
# Výsledkem jsou tedy čísla:
# - 8 - odpovídající hodnota uložená v proměnné index je 2. Zbytek po dělení čísla 2 číslem 2 je 0, vytiskneme.
# - 4 - odpovídající hodnota uložená v proměnné index je 4. Zbytek po dělení čísla 4 číslem 2 je 0, vytiskneme.
# - 0 - odpovídající hodnota uložená v proměnné index je 6. Zbytek po dělení čísla 6 číslem 2 je 0, vytiskneme.
# - 6 - odpovídající hodnota uložená v proměnné index je 8. Zbytek po dělení čísla 8 číslem 2 je 0, vytiskneme.
# - 0 - odpovídající hodnota uložená v proměnné index je 10. Zbytek po dělení čísla 10 číslem 2 je 0, vytiskneme.