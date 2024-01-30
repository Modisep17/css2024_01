# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 07:51:51 2024

@author: Phenyo Modise
"""
import pandas
file=pandas.read_csv("insurance_data.csv",skiprows=5)
print(file) 
print(file.describe)
