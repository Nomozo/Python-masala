# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:20:44 2022

@author: HP
"""

x=int(input("Sonni kiriting"))

a=(x//10)%10
b=x%10
d=x//100
c=d*100+b*10+a

print(c)