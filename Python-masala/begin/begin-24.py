# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:59:22 2022

@author: HP
"""


print("Sonlarni kiriting:")

a=input("a=")
b=input("b=")
c=input("c=")

c=int(a)+int(b)+int(c)
b=int(c)-int(b)-int(a)
a=int(c)-int(b)-int(a)
c=int(c)-int(b)-int(a)



print("a=",int(a),"b=",int(b),"c=",int(c))