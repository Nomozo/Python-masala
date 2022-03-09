# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:47:50 2022

@author: HP
"""
import math
print("Aylananing uzunligini kiriting:")

L=input("l=")
pi=3.14

R=int(L)/2*int(pi)
s=math.pow(int(R),2)
print("Radiusi:",int(R), "Yuzasi", int(pi)*int(s))
