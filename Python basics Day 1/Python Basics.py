# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:52:18 2021

@author: sushmita
"""

print("Hi welcome to CPBA")
print("Hi",'welcome',"to","CPBA")


print("Hi",'welcome',"to","CPBA",sep='-')
print("Hi welcome to CPBA",'Thanks',sep='-')

print("Hi",'welcome',"to","CPBA",end='-------')
print("Hi welcome to CPBA",'Thanks',sep='-')

print("Hi",'welcome',"to","CPBA",end='\n')
print("Hi welcome to CPBA",'Thanks',sep='-')

print("Hi",'welcome',"to","CPBA",end='\t''\t')
print("Hi welcome to CPBA",'Thanks',sep='-')


print?

help(print)

!pip install pandas


!pip list

!pip --version

import pandas
pandas.__version__

import numpy
numpy.__version__

pandas?


country='India'
b=3.5
c=True


print('I love India')
print ('I love ','India')
print('I love my ',country)


country=input()
print('I love my ',country)


country=input('Enter country name->')
print(country)


print("I love {country}")

print(f"I love {country}")
print(f"I love {a} ,{b}")

print(f"sum of a={a} and b={b} is {a+b}")

print("sum of a={} and b={} is {}".format(a,b,a+b))

print("sum of a={0} and b{1} is {2}".format(a,b,a+b))


## types of variables

a=10
b=3.5
c="hi"
d=True

#missed conversion



a=int(input("Enter something"))

x=3
print(type(x))
print(x+1)
print(x-1)
print(x/2)
print(x*2)
print(x**2)
print(x%2)

num=int(input("enter a number"))
if(num%2==0):
    print("even")
    print('Even')
else:
    print("odd")
    
#And operator

"""
A B And
0 0 0
0 1 0
1 1 1
1 0 0
"""

#OR operator

"""
A B OR
1 1 1
0 1 1
0 0 0
1 0 1
"""
t=True
f=False
print(t and f)
print(t and t)
print(f and f)
print(t and f)
print(t or t)
print(f or f)

print(not(t))


#String Handling

Fname="Sushmita"
Lname="Rai"
Fname+Lname
Fname+" "+Lname

s="hello"
s.capitalize()

#string cant be modified

s=s.capitalize() 
print(s)

s.rjust(10)
s.ljust(10)
s.center(10)

s='I like to work in JAVA'
s=s.replace("JAVA","PYTHON")

s=input("Enter your name -->")

s.strip()
s=s.strip()

#list,set,tuple,dictionary
#tuple is indexed, mutable, collection, ordered,can hold heterogenous data types 

a=1,2,3,4,5

print(a)
print(a[0])
print(a[3])



#1. lists is indexed,mutable,collection, unordered, heterogenous data  types

l1=[]
l1=[1,2,'hatt']
l3=[1,"v","CPBA",True,2.55]
l4=[45,85,1,0,-2,1000]
l4[3]='sushmita is sweet'
l4.append(5.44)
l4.append('SDP')
b=l4.pop()
#now b contains SDP, last added value is shown, popped









