#!/usr/bin/python3

import app;
import math;

app.hello("b");

if True:
    print(u"this is an unicode string")
else:
    print("abc")

name = input('Please input your name:')
print(name[1:] *10)

l1 = [1,3,'3']
print(l1[1])
l1.append("abcd")
print(l1)


dicta = {'a':'a'}
dicta['one'] = '2 - 123'
dicta[2]     = "2 - 123"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dicta['one'])       
print (dicta[2])           
print (tinydict)        
print (tinydict.keys())   
print (tinydict.values()) 

a=0
b=2
if (a and b):
    print("and")
elif (a or b):
    print("or")
    
c = [1,2,3,4,5]
d = (1,4,5,6)
if (b in c):
    print("in")
if (b not in d):
    print("not in")

e=1
f=1
if (e is f):
    print("is")

print(math.pi)
s1 = 'adafssd  dsaf s'
print( s1.title())
