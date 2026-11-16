'''
#ans1
x = input("enter: ").split()
e = []
o = []
for i in x:
    if int(i)%2==0:
        e.append(i)
    else:
        o.append(i)
print(f"even: {e}")
print(f"odd: {o}")
'''

'''
#ans2
x = input("enter: ").split()
count = 0
f = []
for i in x:
    for j in i:
        count+=1
    if count>3:
        f.append(i)
    count = 0
print(f)
'''

'''
#ans3
x = input("enter: ").split()
count = 0
total =0
t = 0
b = 0
w = 0
rpo = []
for i in range(len(x)):
    if x[i]=="W":
        count+=1
        w+=1
        x[i]="0"
        if count==6:
            rpo.append(t)
            count= 0
count=0
x = [int(j) for j in x]
for i in range(len(x)):
    count+=1
    t+=x[i]
    total+=x[i]
    if count==6:
        rpo.append(t)
        count= 0
        t = 0
    if x[i]>=4:
        b+=1
    elif i == len(x)-1 and count!=0:
        rpo.append(t)
print(total,w,b,rpo)
'''

'''
#ans4
y = input("enter: ").split(" ")
x =[]
for i in y:
    i = int(i)
    x.append(i)
l = 0
s = 0
for i in range(len(x)):
    for j in range(len(x)-1-i):
        if x[j]>x[j+1]:
           x[j],x[j+1]=x[j+1],x[j]
print("smallest:",x[0]) 
print("largest:",x[-1])
'''

'''
#ans5
x = input("enter: ").split()
largest=0
l = ""
for i in x:
    count =0
    for j in i:
        count+=1
    if count>largest:
        largest = count
        count = 0
        l = i
print(l)
'''

'''
#ans6
m = input("enter items: ").split()
x = input("enter price: ").split()
x = [int(p) for p in x]
y = input("enter order: ").split()
total = 0
i_t = 0
for i in set(y):
    if i in m:
       a=m.index(i)
       b = y.count(i)
       i_t =  b * x[a]
       total =  total + i_t
       print(f"{i} X {b} = {i_t}")
print("Total: ",total)
'''

'''
#ans7
x = input("enter: ").split()
rev = ""
for i in x:
    for j in i:
        rev = j + rev
    print(rev,end=" ")
    rev = ""
'''

'''
#ans8
x = input("enter: ")
d = []
f = []
total = 0
for i in x:
    if i.isdigit():
        d.append(i)
for j in d:
    j = int(j)
    total+=j
    f.append(j)
print(f)
print(total)
'''

'''
#ans9
x = int(input("enter number of students:"))
seen = []
for i in range(x):
   y = input("enter student name: ").lower().split()
   name = ".".join(y)
   seen.append(name)
   count = seen.count(name)
   if count>1:
       print(name+str(count)+"@jklu.edu.in")
       
   else:
       print(name+"@jklu.edu.in")
'''

'''
#ans10
x = input("enter: ").split()
y = []
for i in x:
    i = int(i)
    y.append(i)
for i in range(len(y)):
    for j in range(len(y)-1-i):
        if y[j]==0:
            y[j],y[j+1]=y[j+1],y[j]
print(y)
'''
    
    
    
        