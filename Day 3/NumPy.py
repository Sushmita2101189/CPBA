# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 18:01:44 2021

@author: sushmita
"""
## Data Science begins

import random
#randint function impo
from random import randint

x=randint(1,100)
x

#or we can use this

import random as rd
x=rd.randint(100,120)
x


#to choose a no randomly from a list we have a choice() function
""" random.choice(sequence)
Parameters: 
sequence is a mandatory parameter that
can be a list, tuple, or string.
Returns:  
The choice() returns a random item. """


l1=[123,144,156,111,188]
rd.choice(l1)
professions=["scientist","philosopher","doctor"]
rd.choice(professions)

#to create a list of  random numbers
l2=[]

for i in range(500):
    l2.append(rd.randint(1,10))
print(l2)







##numpy is used for performing multiple operations on matrix data, base for data science


import numpy as np
np.random.randint(100,1000)
 #randint has also different some more features
 #to generate more than one random number, here 10 random numbers
x1=np.random.randint(100,1000,size=10)
x1
#as you can see it returns an array not a list, since we will get homogenous data
#numpy deals with arrays only, data created using numpy is further is used for functions
type(x1)
#shape functions give the dimensions of array
np.shape(x1)


#multi dimensional array by random

x2=np.random.randint(10,20,size=(3,3))
x2
np.shape(x2)


#now to traverse the produced array, i.e each element should be accessible
#ans is indexes
x1[0]
x1[1]
#to return last ele
x1[-1]
#to return start to end
x1[:-1]
x1
#first four ele
x1[:4]

x1[2:5]

x1[2:]
x1[-4:]
x1
x1[-4:-2]


##Double dim 
x2
x2[0][0]
#can also write using ,
x2[0,0]

x2
x2[0,0:2]

x2[0]
#dealing all the values of first array
x2[:,0]

#if we have to access values columnwise instead rowwise
#accessing second column
x2[:,1]

x2[:,1:]

##multidimensional list
l1=[[1,2,3],[4,5,6]]

##3D array size, depth, row, column
x3=x2=np.random.randint(10,20,size=(2,3,4))
x3.shape
x3
# example of 3D array 3 customers data in 4 fields, but there are two categories of customers, depth is 2 which is category, row is 3, as customers are 3 in each category, and 4 fields are saved related to each customer
x3[0]
x3[0:2]
x3[0,0]
x3[0,:,0]
x3


x4=np.random.randint(10,20,size=(7,7))
#now to access one row and skipping one row
#all the rows,skip 1 rows 
x4
x4[::2]

#skipping coulumns

x4[:,::2]

#skip both row column at the same time
x4
x4[::2,::2]




##different functions of numpy

import numpy as np

#to create a range - arange
a1=np.arange(20)
a2=np.arange(0,100)
a2
a3=np.arange(0,100,5)
a3

#array values can be muted

#to reshape the array in some other dimensyion- reshape, but the restriction is total elements in previous and new array
a4=a3.reshape(5,4)
a5=a4.reshape(20)
a5


#create a numpy array of 0s with a particular shape

a=np.zeros((3,4))
a
#by default is float

b=np.zeros((3,4),dtype='int')
b

c=np.ones((3,4))
c
d=np.random.randint(0,100,size=(3,4))
d=d*c
d


#to append a new array to an existing array, then an empty array is created
np.empty((3,4))
np.eye(4,4)


#if i want to divide a line into exact parts

np.linspace(0,10,num=4)
#used in dividing x or y axis into speccific parts while plotting values


# different statistical functions of numpy
import numpy as np

r1=np.random.randint(0,100000,size=10000)
r1.shape
np.min(r1)
np.max(r1)
np.mean(r1)
np.std(r1)
np.var(r1)

#this will take a lot of time
def mininlist(lst):
    mx=lst[0]
    for n in lst:
        if(n<mx):
            mx=n
    return (mx)


np.floor([1.2,2.6])
np.ceil([1.2,2.6])
np.trunc([1.2,2.6])
np.round([1.2,2.6])

np.ceil([-1.2,-1.6])
np.floor([-1.2,-1.6])
np.trunc([-1.2,-1.6])

#requirement of splitting, data set of 100 rows and we want to train 70%, testing 30% 
#odd number of length of cell cant be divided into two VAlueError
x=np.arange(10,20)
x
np.split(x,2)
y=np.arange(10,19)
y
np.split(y,2)

x1=np.random.randint(10,20,size=(4,4))
x1
#rowwise splitting
x2=np.split(x1,2,axis=0)
x2
#columnwise splitting
x3=x2=np.split(x1,2,axis=1)
x3

np.multiply(x3,5)
x3


x1
#min vALUE OF EACH column
x1.min(axis=0)
#min value of each column
x1.min(axis=1)



#np.split on an array gives a list of arrays so to use it as an numpy array convert it into numpy array
x2=np.array(np.split(x1,2,axis=0))
x2
x2.shape
type(x2)
#note there is a difference between numpy aray and a normal array


x2.max()
x2.max(axis=1)


np.sum(x1,axis=0)
x1
sum(np.equal(x1,17))

np.equal(x1,17)
np.less(x1,15)
sum(np.less(x1,15))
np.sum(np.greater(x1,15))



np.arange(1,13)
np.arange(1,13).reshape(3,4)
#to save the values in row wise manner C and columnwise F
np.arange(1,13).reshape(3,4, order='C')
np.arange(1,13).reshape(3,4, order='F')

#skipped part

a=np.ma.array([1,2,3,4,5])



##statistical outcome



import matplotlib
from matplotlib import pyplot as plt
import numpy as np
#parameters mean, stdev, no of values
n_arr=np.random.normal(100,20,1000)
n_arr
l1=list(range(50,150))
plt.hist(n_arr,bins=l1)
plt.title("histogram")
plt.show()
