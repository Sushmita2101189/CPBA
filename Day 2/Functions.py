# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 22:35:11 2021

@author: sushmita
"""

#Functions in python

def oper():
    a=10
    b=20
    print(a+b)
    print(a*b)
    print(a/b)
    print(a-b)
    
oper()

    
def oper1(a,b):
    print(a+b)
    print(a*b)
    print(a/b)
    print(a-b)
    
    
oper1(10,50)
oper1('Sushmita','Sudhanshu')
oper1(True,False)

def printhello(name):
    print('Hello '+name)
    


def printhello(name='Unknown'):
    print('Hello '+name)
    

e_id=[]
e_name=[]
mb=[]
em=[]
#important default values are given from left to right
def emp(eid,ename,mobile,email='None'):
    e_id.append(eid)
    e_name.append(ename)
    mb.append(mobile)
    em.append(email)
    
emp(1,'V',99,'s@wig.com')
emp(2,'F',991)


emp(1,'d')

def maxinlist(lst):
    mx=0
    for n in lst:
        if(n>mx):
            mx=n
    return (mx)


l1=[5,2,7,6,9,1]
maxinlist(l1)
    

