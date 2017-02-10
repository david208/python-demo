'''
Created on 2016年10月10日

@author: shim
'''

import http;

http.client;

class people(object):
    '''
    classdocs
    '''
    name ='';
    age = 0;
    __count = 1;


    def __init__(self, name,age):
        '''
        Constructor
        '''
        self.age=age
        self.name=name
        
    def speak(self):
        print("%s 说: 我 %d 岁。总数%d" %(self.name,self.age,self.__count))

p = people('runoob',10)
p.speak()
