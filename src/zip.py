'''
Created on 2016年10月11日

@author: shim
'''
import zlib

if __name__ == '__main__':
    s = b'witch which has which witches wrist watch'
    print(len(s))
    t = zlib.compress(s);
    
    print(len(t))
    
for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()