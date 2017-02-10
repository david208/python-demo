#!/usr/bin/python3
import pickle
# 打开一个文件
f = open("/foo.txt", "r+")
str = f.read()
print(str)
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

output = open('data.pkl', 'wb')
pickle.dump(data1, output)
output.close()

pkl_file = open('data.pkl', 'rb')
data2 = pickle.load(pkl_file)
print(data2)
pkl_file.close()

try:
    x = 1/1;
except  ZeroDivisionError:
    print("error")
else:
    print("info")
finally:
    print("ok")
