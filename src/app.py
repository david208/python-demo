#!/usr/bin/python3
import sys;

print(sys.path);

def hello(a):
    print(a);
        
hello("asb");

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print(__name__)

a = [343.435,43535.5646]
a.count(3);

b = [3*x for x in a if x > 3]
print(b)

c = b,"1",5

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for  v in knights.keys():
    print(v)
    
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

