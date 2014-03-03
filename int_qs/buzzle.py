#!/usr/bin/env python
from __future__ import print_function
total = 64
true = '*'
false = '-'
mid = 64/2
place_list = []
ph = ph1= mid
pl = pl1 = 0
for i in range(1,64):
  ph  = ph-1
  ph1 = ph1+1
  place_list.append(ph)
  place_list.append(ph1)
  if ph==1 or ph1==64:
      break

cpl = place_list
for k in range(1,32):
  if ( k == 1):
    for i in range(1,64):
      print(false, end='')
      if (i == mid):
          print(true, end='')
    print()
  else:
    try:
      pl = place_list.pop(0)
      pl1 = place_list.pop(0)
    except Exception as err:
      pass
    for j in range(1,64):
      print(false, end='')
      if (j == pl or j == pl1):
          print(true, end='')
    print()
