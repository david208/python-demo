'''
Created on 2016年10月11日

@author: shim
'''


n = int(input("最大值"))
n1 =0
n2 =1
array = [n1,n2]
if n<=0:
    print("error")
elif n ==1:
    print(0)
else:
    for i in range(0,n):
        if(i== n1 +n2):
            array.append(i)
            n1 = n2 
            n2 = i
    print(array)
        

    