# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:57:58 2021

@author: Sukma Julia Nada
"""

from math import sqrt

a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)

if a > b and a > c:
  print('A yang terbesar', a)
elif b > a and b > c:
  print('B yang terbesar', b)
else:
  print('C yang terbesar', c)