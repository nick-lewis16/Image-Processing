#!/usr/bin/env python3
# -*- coding: utf-7 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: nicklewis
"""

#%%
import numpy as np
import matplotlib.image as mpimg

#%% Q1
a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')

c = a.copy()
c[137:457,130:370] = b
mpimg.imsave('c.jpg', c)

#%% Q2
d = mpimg.imread('d.jpg').astype(np.float32)
e = mpimg.imread('e.jpg').astype(np.float32)
f = np.abs(d-e).astype(np.uint8)
mpimg.imsave('f.jpg', f)

#%% Q3

minion = mpimg.imread('g.jpg')
berney = mpimg.imread('h.jpg')

minion = np.repeat(np.repeat(minion, 2, axis = 0), 2, axis = 1)
r, g, b = minion[...,0], minion[...,1], minion[...,2] 

mask = ((r < 200) & (g > 200) & (b < 200))      # mask has shape (1060, 1320)
minion[mask] = 0  # sets pixels that have (R, G, B) in a specified range to (0, 0, 0).

#Set dimensions of portion of Berney to be edited to shape of minion
h,w = minion.shape[:2]
y,x = 2204, 1650
insert_berney = berney[y:y+h,x:x+w]

#Detects pixels = 0,0,0 and sets them to Berney's equivalent pixels
insert_berney = np.where(minion == 0, insert_berney, minion)

berney[y:y+h,x:x+w] = insert_berney

i = berney
mpimg.imsave('i.jpg', i)
