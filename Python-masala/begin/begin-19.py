# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:24:23 2022

@author: HP
"""
import math

print("Koordinatalarni kiriting")

x1=input("x1=")
y1=input("y1=")
x2=input("x2=")
y2=input("y2=")

x3=x2
y3=y1
x4=x1
y4=y2


a=math.sqrt(pow(int(x1)-int(x4),2)+pow(int(y1)-int(y4),2))
b=math.sqrt(pow(int(x1)-int(x3),2)+pow(int(y1)-int(y3),2))

s=int(a)*int(b)
p=2*(int(a)+int(b))

print("Perimetri:",int(p),"yuzasi:",int(p))
