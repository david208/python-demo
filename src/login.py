def name_test(input_name, namelist):
    if input_name in namelist:
        return True
    else:
        print('Name is None.')
        return False

def pw_test(pw ,index_pw):
    if pw == index_pw:
        print ('Welcome.')
       
        return 1
    else:
        print ('Password is None.')

namelist = []
pwlist = []
with open('a.txt','r') as f:
    for i in f:
        namelist.append(i.split()[0])
        pwlist.append(i.split()[1])

index_pw = []
name = ''
pw=''
name_num = 0
pw_num = 0
inloopnum = 0

name = input('Please input your name:')
name_num +=1
while True:  
    if name_test(name, namelist):
        index_pw = pwlist[namelist.index(name)]
        pw = input('Please input your password:')
        pw_num +=1
        inloopnum = pw_test(pw, index_pw)                                        
    else:
        name = input('Please input your name again:')        
        name_num +=1

    if name_num ==3:
        print ('You have no chance.')
        break
    if pw_num==3:
        print ('You have no chance')
        break
    if inloopnum==1:
        break
    

