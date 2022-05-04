# Napište program, který obdrží seznam známek z písemek a na výstup vypíše souhrn toho, kolik bylo dohromady jedniček,
# kolik dvojek, kolik trojek a tak dále.

znamky = [1, 1, 2, 1, 5, 4, 2, 5, 4, 3, 5, 2, 1, 53, 9, 0, 3, 0, 4, 5, 5, 5, 5, 1, 5, 1, 2, 3, 4, 6, 5]

jednicky = 0
dvojky = 0
trojky = 0
ctyrky = 0
petky = 0
neklasifikovano = 0
chyba = 0

for znamka in znamky:
    if znamka == 1:
        jednicky += 1
    elif znamka == 2:
        dvojky += 1
    elif znamka == 3:
        trojky += 1
    elif znamka == 4:
        ctyrky += 1
    elif znamka == 5:
        petky += 1
    elif znamka == 0:
        neklasifikovano += 1
    else:
        chyba += 1

print(f"Jedničky: {jednicky}.\n"
      f"Dvojky: {dvojky}.\n"
      f"Trojky: {trojky}.\n"
      f"Čtyřky: {ctyrky}.\n"
      f"Pětky: {petky}.\n"
      f"Neklasifikováno: {neklasifikovano}.\n"
      f"Chybně zapsáno: {chyba}.\n")