# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:03:21 2022

@author: HP
"""

x=int(input("Sonni kiriting"))

a=x//100
b=(x//10)%10
c=x%10
d=c*100+b*10+a

print(d)