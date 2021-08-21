# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 22:16:44 2021

@author: sushmita
"""

##pandas





##library for importing data pydataset, installed using- pip install pydataset on Anaconda cmd
import pandas as pd
from pydataset import data

data('')

##csv is lightest file size our data set 

mt=data('mtcars')
mt
type(mt)
mt.head(10)
mt.t
#saved in C users sushmita cwd
mt.to_csv("mtcars.csv")
mt=pd.read_csv(r"F:\analytics\datasets\mtcars.csv")
mt


range(1,10)
s=pd.Series(range(1,10))
type(s)
#series into numpy array
s1=s.values
type(s1)




