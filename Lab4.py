## Question 1

salary, years = input().split()
if years >= 5:

    print("Your bonus is", salary +(0.05* salary))
else: 
    print("Your bonus is", salary)


## Question 2 
password = str(input())

if password == "s3cr3tlP@ssw0rd":
    print("Welcome")
else:
    print("Wrong Password")
    
## Question 3

shape = str(input("Enter whether the geometric shape is square, rectangle, circle or triangle"))
if shape == "triangle":
    base = int(input("Enter the base of the triangle"))
    height = int(input("Enter the height of the triangle"))
    print((1/2)*(base * height))
if shape == "square":
    side = int(input("Enter the side of the square"))
    print("Area= ", side * side)
if shape == "rectangle":
    length = int(input("Enter the length of the rectangle:"))
    breadth = int(input("Enter the breadth of the rectangle"))
    print("Area= ", length * breadth)
if shape == "circle":
    radius = int(input("Enter the radius of the circle"))
    Area = 3.14 * radius * radius
    print("Area of circle is", Area)


## Question 4
Hours, Minutes = input().split()

Hours = int (Hours)
Minutes = int(Minutes)
time = int (Minutes + 15)
if time >= 60:
    Hours = Hours + 1
    Minutes = time % 60
    print(Hours,":",Minutes)
else:
    Minutes = time
    print(f"{Hours:02d} : {Minutes:02d}")
        
## Question 5
period_of_day = str(input("Enter the day period is it day or night"))
kilometers = float(input("Enter the kilometers"))

if kilometers > 100:
    print("The cheaptest option for you is train for Rs", 2.88 * kilometers)
elif kilometers > 20:
    print("The cheapest option for you is bus for Rs", 4.32 * kilometers)
else:
    if period_of_day == "day":
        print("The cheapest option for you is taxi for Rs", 33.58 +(37.89 *kilometers))
    else:
        print("The cheapest option for you is taxi for Rs", 33.58 + (43.17 * kilometers))

## Question 6
holidays = int(input("Enter the number of holidays you have"))
work_days = 365 - holidays
Time_Holidays = holidays * 127
Time_workdays = work_days * 63
total_time = Time_Holidays + Time_workdays
if total_time > 30000:
    print("Tom will not sleep well")
else: 
    print("Tom will sleep well and the difference from the norm is " , 30000 - total_time, "minutes")

## Question 7
budget = float(input("Enter the amount of budget you have "))    
season = str(input("Enter the season summer or winter")) 

if budget > 1000:
    spent = 0.90 * budget
    print("Spent Money = ", spent, "Vacation place = Europe")
elif budget > 100:
    if season == "summer":
        print("Spent Money =", 0.40* budget, "Vacation place = Balkans")
    else: 
        print("Spent Money =", 0.80 * budget, "Vacation place = Balkans")
else:
    if season == "summer":
        print("Spent Money =", 0.30* budget, "Vacation place = Bulgaria")
  
    else:
        print("Spent Money =", 0.70* budget, "Vacation place = Bulgraria")

## Question 8
for kl in range (6,1001,10):
    print (kl,",")

## Question 9
n = int(input("Enter n"))
sum = 0
for i in range(1,n+1,1):
    num = int(input("Enter Number"))
    sum = sum + num 
print(sum)


##  Question 10
integer_N = int(input("Enter the +ve integer N"))
for i in range(1,21,1):
    print(integer_N,"×", i, "=", integer_N*i)