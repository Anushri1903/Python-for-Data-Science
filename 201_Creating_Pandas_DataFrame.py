#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:34:38 2023

@author: anushrimore
"""

## Exploring and Understanding your dataset ##

import pandas as pd 
import numpy as np 

transaction = pd.read_excel('/Users/anushrimore/Dropbox/Mac/Documents/Data_Infinity/Python_fundamentals/grocery_database.xlsx',sheet_name = "transactions")
print(transaction.shape)
print(transaction.sample(10))
print(transaction.head(10))
print(transaction.tail(10))
print(transaction.describe())

# Outliers 
transaction.nlargest(5,"sales_cost")
transaction.nsmallest(5,"sales_cost")


### Find unique values in each column 
print(transaction.nunique(axis=0))

## Observing null values in data frame 
print(transaction.isna().sum())

## Adding and dropping columns 
temp_data = transaction.copy()
condition = [temp_data['num_items'] >= 8, temp_data['num_items']>= 2 , temp_data['num_items']<=1]
outcome = ["Shopping_lovers", "Moderate_Shoppers", "Dislike_shopping"]

temp_data['Customet_nature'] = np.select(condition,outcome,default="NA")
