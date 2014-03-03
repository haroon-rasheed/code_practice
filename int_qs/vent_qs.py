#!/usr/bin/env python
from __future__ import print_function
total = 64
true = '*'
false = '-'
mid = 64/2
place_list = []
ph = ph1= mid
pl = pl1 = 0
#while(ph>1 or ph1<64):
for i in range(1,64):
  ph  = ph-1
  ph1 = ph1+1
  #print(ph)
  #print(ph1)
  place_list.append(ph)
  place_list.append(ph1)
  if ph==1 or ph1==64:
      break

print(place_list)
cpl = place_list
#print("LEN ==>", len(place_list))
for k in range(1,64):
  if ( k == 1):
    for i in range(1,64):
      print(false, end='')
      if (i == mid):
          print(true, end='')
    print()
  else:
    if (k > 61):
      break
    pl = place_list.pop(0)
    pl1 = place_list.pop(0)
    for j in range(1,64):
      #print('j')
      #print("j", j)
      print(false, end='')
      #if ( k%2 != 0):
        #print("pl,  pl1,  j  k  ", pl, pl1, j)
      if (j == pl or j == pl1):
          print(true, end='')
    print()
