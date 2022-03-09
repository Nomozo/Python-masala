# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:18:40 2022

@author: HP
"""

x=int(input("Sonni kiriting"))

a=(x//10)%10
b=x%10
d=x//100
c=a*100+d*10+b

print(c)