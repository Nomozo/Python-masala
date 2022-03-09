# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:17:48 2022

@author: HP
"""

x=int(input("Sonni kiriting"))

a=(x//10)%10
b=x%10
d=x//100
c=b*100+a*10+d

print(c)