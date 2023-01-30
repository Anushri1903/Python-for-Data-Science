#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:55:34 2023

@author: anushrimore
"""
import numpy as np

# creating 1 d array
my_1d_array = np.array([1,2.,4,5])
my_2d__array = np.array([[1,2,3],[4,5,6],[7,8,9]])

## Creating default array
zero_array = np.zeros(10)
ones_array = np.ones(7)
specific_value_array = np.linspace(1,10,8)

# Arrange 
my_array = np.arange(1,20,3)
my_array_random= np.arange(10)

# Generating Random numbers using numpy 
random_1d_array =np.random.rand(3,10)
# randint
random_int = np.random.randint(20,49,(7,7))

## Use of reshape functionality
random_array = np.random.randint(1,100,25)
reshape_random_array = random_array.reshape((5,5))
