'''
#ans1
x = input("enter your string: ")
rev = '' 
for i in x:
    rev = i + rev
print(rev)
'''
'''
#ans2
x = input("enter your string: ")
count = 0
for i in x:
    count+=1
    if i == " ":
        count=0
print(count)
'''
'''
#ans3
x = input("enter your string: ")
w = input("enter your word: ")
count =0
for i in x:
    if i == w:
        count= count + 1
print("count: ",count)
if count==0:
    print(f"there is no '{w}' in the string")
'''
'''
#ans4
x  = input("enter your string: ")
x = x.lower()
a = "qwertyuiopasdfghjklzxcvbnm"
count = 0
for i in a:
    if a in x:
        count+=1
if count==26:
    print(f"{x} is a pangram")
else:
    print(f"{x} is not a pangram")
'''
'''
#ans5 method1
x = input("enter your string: ")
shift = int(input("enter shift value: "))
y = "abcdefghijklmnopqrstuvwxyz"
c = 0
for i in x:
    if i.isalnum():
        for q in y:
            if i!=q:
                c+=1
            if i==q:
                w = c+shift
                for p in range(w+1):
                    if w>25:
                        w = w%26
                        if p == w:
                            print(y[p],end='')
                  
                    else:
                        if p == w:
                            print(y[p],end='')
                break
        c = 0
    else:
        print(i,end="")
'''
'''
#ans5 method2
x = input("enter your string:").strip()
shift = int(input("enter shift:"))
n =""
for i in x:
  a = ord(i)
  if 65<=a<97:
    base = 65
  elif 97<=a<=122:
    base = 97
  else:
    n = n+i
    continue
  a_normal = a-base
  s = a_normal+shift
  s = s%26
  n = n + chr(s+base)
print(n))
'''
'''
#ans6
x = int(input("enter your number: "))
n = []
total=0
while x!=-1:
    n.append(x)
    x = int(input("enter your number: "))
    total+=1
for i in range(1,11):
        f = n.count(i)
        p=(f * 100) / total
        if (((p%5)*10)/5)>=5:
            p = p//10+1
        else:
            p = p//10
        print(f"{i}: {'#'*int(p)}{(f * 100) / total:.2f}%")
 '''       
 
'''
#ans7
x = input("enter your string: ")
if x==x[::-1]:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")
'''
'''
#ans8
x = list(map(int,input("enter your numbers with 1 space:").split(",")))
add = 0
pro=1
sd=9999999
l = 0
for i in x:
    add = add+i
    pro = pro*i
    if sd>i:
        sd=i        
print(f"\naddition of all numbers in this list: {add}\n")
print(f"product of all numbers in this list: {pro}\n")
print(f"the smallest number in this list: {sd}")
'''
'''
#ans9
x = input("enter items to put in list:").split()
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j]< x[j+1]:
            a = x[j]
            x[j]= x[j+1]
            x[j+1] = a
print(x)
'''
'''
#ans10
x = input("enter with -:").split("-")
for j in range(len(x)):
    for i in range(len(x)-1):
        if a[i]> a[i+1]:
            z = x[i]
            x[i] = x[i+1]
            x[i+1] = z
x = "-".join(x)
print(x)
'''
'''
#ans11
a = input("enter your paragraph: ")
d = 0
sl = 0
cl = 0
sc = 0
for i in a:
    if i.isdigit():
        d+=1
    elif i.isupper():
        cl+=1
    elif i.islower():
        sl+=1
    else:
        sc+=1
print(f"total digits in paragraph: {d}") 
print(f"total capital letters in paragraph: {cl}") 
print(f"total small letters in paragraph: {sl}") 
print(f"total special characters in paragraph: {sc}")    
'''
'''
#ans12 method1
x = input("enter your sentence: ")
for i in range(len(x)):
    a = x[i]
    count = x[0:i+1].count(a)
    if count==1:
        print(a,end="")
'''
'''
#ans12 method 2
x = input("enter your sentence:")
printed = ''
for i in x:
    if i not in printed:
        print(i,end="")
        printed+=i
'''






























