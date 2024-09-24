#a=20
'''b=30
c=40
if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")'''

'''a=3
if a==1:
    print("value is 1")
if a==2:
    print("value is 2")
if a==3:
    print("value is 3")
else:
    print("value not found")

if a==1:
    print("value is 1")
elif a==2:
    print("value is 2")
elif a==3:
    print("value is 3")
else:
    print("value not found")'''


'''for i in range(5):
    print(i)

for i in range(6):
    print(i,end="")'''

'''for i in range(1,6):
    for j in range(1,8):
        print(j,end="")
    print()'''


'''for i in range(1,4):
    for j in range(1,4):
        print('laya',end="")
    print()'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print('*',end="")
    print()
print()
print()'''
#......................................................
'''for i in range(1,6):
    for j in range(1,7-i):
        print(j,end="")
    print()'''

'''for i in range(1,6):
    for j in range(1,7-i):
        print('*',end="")
    print()'''
#.........................................
'''for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()'''

#..............
'''for i in range(1,6):
    for k in range(1,6-i):
        print("",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
#............................with space    
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()'''
#............
'''for i in range(1,6):
    for j in range(1,6):
        if j==1:
            print('@',end="")
        else:
            print('*',end="")
    print()
print()
print()
#.....................
for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==5:
            print('@',end="")
        else:
            print('*',end="")
    print()
print()
print()
#.....................................
for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==5 or j==5:
            print('@',end="")
        else:
            print('*',end="")
    print()    
print()
print()
print()
#.....................................
for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==5 or j==5 or i==1:
            print('@',end="")
        else:
            print('*',end="")
    print()
print()
print()
#..................................
for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==5 or j==5 or i==1:
            print('@',end="")
        else:
            print(' ',end="")
    print()
#.....................................
for i in range(1,10):
    if i==5:
        break
    print(i)
print()
print()

for i in range(1,10):
    if i==5:
        continue
    print(i)
print()


for i in range(1,6):
    pass
print()'''
#......................
#i=1
#while i<6:
#    print(i)
#..................................practice
'''for i in range(1,6):
    for j in range(1,6):
        if i==2 or i==4:
            print('*',end="")
        else:
            print(j,end="")
    print()
print()
print()
#..........................................2
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==3 or i==5:
            print(i,end="")
        else:
            print('*',end="")
    print()
print()
print()
#...................................
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print()
print()
#...................................
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end="")
    print()
print()
print()
#...................................
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
print()
print()
#...................................
for i in range(1,6):
    for j in range(1,7-i):
        print(j,end="")
    print()
print()
print()'''
#.................................
'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print()
print()

for i in range(1,6):
    for j in range(5,-1):
        print(j,end="")
    print()'''
#...............................24/09/24
#while loop
'''i=1
while i<6:
    print(i)
    i=i+1

print()
print()
#......................
i=1
while i<6:
    j=1
    while j<6:
        print(j,end="")
        j=j+1
    print()
    i=i+1'''
#......................
temp=("hello world")
print(temp[0])
print(temp[2])
print(temp[-11])
print(temp[0:3])#[:3]
print(temp[:3])
print(temp[6:9])
print(temp[8:11])#[8:]
print(temp[0:11:2])#starting...ending...intervel
print(temp[::2])




        
    
    
















    

    

    
    
    
    
