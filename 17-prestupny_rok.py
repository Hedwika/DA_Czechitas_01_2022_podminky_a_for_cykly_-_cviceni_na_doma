# Napište program, který po zadání kalendářního roku vypíše, zda jde o rok přestupný, či nikoliv. Letopočet je přestupný, pokud je dělitelný čtyřmi. Roky, které jsou dělitelné 100 jsou ovšem přestupné pouze tehdy, jsou-li zároveň dělitelné 400.

import sys

rok = int(sys.argv[1])

if rok % 4 == 0:
  if rok % 100 == 0:
    if rok % 400 == 0:
      print(f"Rok {rok} je přestupný.")
    else:
      print(f"Rok {rok} není přestupný.")
  else:
    print(f"Rok {rok} je přestupný.")
else:
  print(f"Rok {rok} není přestupný.")