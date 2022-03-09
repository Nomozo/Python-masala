# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 09:09:23 2022

@author: HP
"""

v1=int(input("Birinchi avtomabilning tezligini kiriting:"))
v2=int(input("ikkinchi avtomabilning tezligini kiriting"))
s=int(input("Ular orasidagi boshlang'ich masofani kiriting:"))
t=int(input("Ular qancha vaqt harakatlanganini kiriting"))
c=s-(v1-v2)*t

print("Ular orasidagi masofa",c,"ga teng")