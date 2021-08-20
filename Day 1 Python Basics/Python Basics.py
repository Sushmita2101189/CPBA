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


# looping Day 2 starts here

for i in l3:
    print(i)
    
r1=range(100)

print(r1)
r2=list(r1)
for i in r2:
    
r3=range(-100)
print(r3)
x=list(r3)
for i in x:
    print(i)
    
l5=[3,2,9,8,5,1]
l5.sort()

l4.reverse()

fruits=['apple','orange','lemon']
fruits.sort()
#ASCII value of A is smaller than a
fruits.append('APPLE')

l6=list(range(1,10,3))
print(l6)

#one common mistake when we create a new list by copying contents using '=' the memory of both lists is same, if one is changed other also changes, to overcome this we have copy function

l7=[8,9,4,2]
l8=l7
print(l8)
l8[1]=69
print(l7)

l9=l7.copy()
l7.append(-3)
print(l9)


#2. set is not indexed,mutable,collection, ordered, heterogenous data  types 
#properties of set is followed like unique elements
s1={1,2,1,4,3,7}
s2={1,2.5,'Vikas',False}
#when we define the list then initially it is not sorted but when we utilize it then it becomes sorted
print(s2)

#we can add multiple values to a set by using update
s2.update(['ZZZ','25'])
s2.remove('ZZZ')
#once removed cant be removed again
s2.remove('ZZZ')

# discard function doesnt throw error when we remove a value twice
s2.discard(2.5)
s2.discard(2.5)


#set operations union, intersection


setA={'India', 'Pakistan','New Zealand'}
setB={'India','Bangladesh','Sushmita'}
setA.union(setB)
setA.intersection(setB)
setA.difference(setB)

#3. tuples are immutable,indexed, unordered
#used when we want to create collection of values which can't be changed in case
t1=(1,2,3,4,5)
t1[3]
for i in t1:
    print(i)
    
#4.VVVImp dictionaries have key value pairs, not indexes but keys,heterogenous, mutable
d1={}
type(d1)

student={'rollno':1,'name':'Sushmita','branch':'BA'}
student['branch']

car={'brand':'honda','model':'jazz','year':2021}
car.get('brand')
car.keys()
car.values()

for i in car:
    print(i)


#using items, it creates tuples of key value pair    
for i in car.items():
    print(i)
    
#we can also display key value in a specific format
for i,j in car.items():
    print(i,'------>',j)
    
student={'rollno':[1,2,3,4]}
student
student['rollno'][2]


car.pop('year')
car.popitem()

car['color']='Black'

car.clear()

#conditional statements
a=30
b=20
if(a>b):
    print("b is lesser")
    
if(False):
    print("a is greater")


if(a<b):
    print('a is lesser')
else:
    print('b is greater')
    


marks=int(input("Enter your marks-->"))

if(marks>90):
    print('A')
elif(marks<=90 and marks>80):
    print('B')
elif(marks<=70 and marks>60):
    print('D')
else:
    print('Fail')


marks=int(input("Enter your marks-->"))

if(marks>90):
    print('A')
else:
    if(marks>80):
       print('B')
    else:
        if(marks>60):
            print('D')
            else:
                print('Fail')
                
                
#looping stmt

l1=list(range(0,10))

for i in l1:
    print(i)


teamA=['India','Australia','Pakistan','England']
len(teamA)


for i in range(len(teamA)):
    print(teamA[i])
    teamA[i]=str(teamA[i])+"_A"
    print(teamA[i])
    
#break

while(True):
    p=input("Enter Password:")
    if(p==password):
        break
    print("enter correct password")
   
    
   
    



