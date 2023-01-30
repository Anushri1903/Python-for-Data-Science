#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:29:15 2023

@author: anushrimore
"""
import numpy as np

new_array_1 = np.array([1,2,4,5,6])
print(new_array_1.max())
print(new_array_1.min())
print(new_array_1.mean())
print(new_array_1.std())

new_array_2 = np.random.randint(20,49,(7,7))

## Index of values 
print(new_array_2.argmax(axis=0))# column wise max value index
print(new_array_2.argmin(axis=1))  # row wise min alue index
print(new_array_2.max())
print(new_array_2.min())
print(new_array_2.mean())
print(new_array_2.std())

## Dot product
a = np.random.randint(1,4,(2,3))
b= np.random.randint(1,10,(3,3))
c= np.dot(a,b)
print("Dot product",c)

## np.where np.argwhere 
np.where(a > 2)
np.argwhere(a > 2)
print(a.flatten())
a[np.where(a > 2)] = 500

## Hstack Vstack

a_b_v = np.vstack((a,b))
a_a_h = np.hstack((a,a))
