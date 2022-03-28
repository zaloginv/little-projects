# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:32:52 2020

@author: Murdikun
"""

import numpy as np
import skimage.draw 
import skimage.io 
import math 


print('Введите размерность (например, 1000 на 1000)')
a = int(input('Ширина: '))
b = int(input('Высота: '))
n = int(input('Введите глубину: '))

d = np.zeros((a,b), dtype=np.uint8) 

#основная функция
def KOHA (Aix,Aiy,Dix,Diy,ni): #деф - объявляем функцию Коха
    while ni > 0:                
        ni-=1
        koef=1/2 #находим по формуле вторую точку
        Bix=int((Aix+koef*Dix)/(1+koef)) #int здесь и далее - потому что с не-целыми числами не работает
        Biy=int((Aiy+koef*Diy)/(1+koef))
        koef=2 #меняем коэффициент, чтоб найти третью точку:
        Cix=int((Aix+koef*Dix)/(1+koef))
        Ciy=int((Aiy+koef*Diy)/(1+koef))
        #по формуле для равносторонних треугольников находим четвёртую:
        Fix=int((Bix+Cix-(Biy-Ciy)*math.sqrt(3))/2)
        Fiy=int((Biy+Ciy-(Cix-Bix)*math.sqrt(3))/2)
        #присваиваем значения координатам:
        Ai=(Aix,Aiy)
        Bi=(Bix,Biy)
        Ci=(Cix,Ciy)
        Fi=(Fix,Fiy)
        Di=(Dix,Diy)
        
        if ni==0: #если рекурсий больше не будет, можно рисовать
            d[skimage.draw.line(*Ai,*Bi)]=255
            d[skimage.draw.line(*Bi,*Fi)]=255
            d[skimage.draw.line(*Fi,*Ci)]=255
            d[skimage.draw.line(*Ci,*Di)]=255
        
        #рекурсия на себя
        KOHA (Bix,Biy,Fix,Fiy,ni)
        KOHA (Fix,Fiy,Cix,Ciy,ni)
        KOHA (Cix,Ciy,Dix,Diy,ni)
        
        #берём отдельный мелкий отрезок
        Dix=Bix
        Diy=Biy



Nachalo=0
Konec=a-1
Visota=int(b/2)

Ax=Nachalo
Ay=Visota
Dx=Konec
Dy=Visota

A=(Ax,Ay)
D=(Dx,Dy)
#присвоили координаты основным точкам

if n==0: 
    d[skimage.draw.line(*A,*D)]=255
    #просто нарисовали в случае 0
    
if n>=1:     
    KOHA(*A,*D,n)
    #запустили функцию


skimage.io.imsave('kriv.png', d)
skimage.io.imshow('kriv.png')
input()