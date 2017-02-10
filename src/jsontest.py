'''
Created on 2016年10月12日

@author: shim
'''

import json ;


data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com',
    'array' : (2,4,"66")
}

print(data)
print(json.dumps(data))
print(json.loads(json.dumps(data)))

