# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 08:50:45 2022

@author: HP
"""

v=int(input("qayiqning tezligini kiriting:"))
u=int(input("daryoning tezligini kiriting:"))
t1=int(input("oqim bn yurgan vaqtni kiriting:"))
t2=int(input("Oqimga qarshi yurgan vaqtni kiriting:"))

s1=(v+u)*t1
s2=(v-u)*t2
s=s1+s2

print("oqim bn yurgan yo'li,",s1,"oqimga qarshi yurgan yo'li ",s2,"Umumiy masofa",s)
