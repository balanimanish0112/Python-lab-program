'''
#ans1
print("        Addition Table")
print("    1  2  3  4  5  6  7  8  9")
print("    -------------------------")
for r in range(1, 10):
    print(r, "|", end=" ")
    for c in range(1, 10):
        if r + c < 10:
            print(r + c, end="  ")
        else:
            print(r + c, end=" ")
    print()
'''
'''
#ans2
n = int(input("enter:"))
for i in range(1,1001):
    if i%n == 0:
        if i%4 !=0:
            print(i,end =" ")
'''
'''
#ans3
n = int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
    
for i in range(n):
    for j in range(n):
        if
'''
'''
#ans4
x = int(input(""))
a = ""
for i in range(x):
    while x!=0:
        r = x % 8 
        a = str(r) + a
        x = x//8
print(a)
'''
'''
#ans5
n= int(input("enter no. of students:"))
l = 0
sl = 0
for i in range(n):
    x = int(input("enter the distance:"))
    if x>l:
        sl = l
        l = x
    elif l>x>sl:
        sl = x
print(f"largest: {l}")
print(f"second largest: {sl}")
'''
'''
#ans6
x = int(input("enter number:"))
for i in range(1,x+1):
    v = i
    y = i
    an = 0
    c = 0
    while y >0:
        x = (y%10)
        c+=1
        y = y//10
    y = v
    
    for i in range(c):
        an = (v%10)**c + an
        v = v//10
        
    if an == y:
        print(y)
'''
'''
#ans7
x = int(input("enter:"))
print("N  N^2  N^3  Square Root")
for i in range(1,x+1):
    s = i**2
    c = i**3
    sr = i**0.5
    print(f"{i}  {s}    {c}     {sr}")
'''
'''
#ans8

x = int(input("enter:"))
for i in range(1,x+1):
    for j in range(i,x):
        print(" ",end="")
    for j in range(i):
        print(i,end="")
    print()
'''
'''
#ans9
n = int(input("Enter number of lines: "))
    count = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()
'''
'''
#ans10
x = int(input(""))
for i in  range(1,x+1):
     if i<=(x+1)//2:
         s = 2* i-1
     else:
         s = 2*(x-1)+1
     print("*"*s)
'''
























