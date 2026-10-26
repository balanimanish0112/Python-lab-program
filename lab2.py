# question-1
# num = int(input("Enter a number: "))

# if num % 5 == 0:
#     print("Hi")
# else:
#     print("Bye")


# question-2
# X = float(input("Enter X: "))
# Y = float(input("Enter Y: "))
# H = float(input("Enter H: "))

# area = ((X + Y) * H) / 2

# print("Area of trapezoid =", area)



# question-3
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))

# bmi = weight / (height * height)

# print("BMI =", bmi)

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Slightly overweight")
# elif bmi < 35:
#     print("Obese")
# else:
#     print("Clinically obese")



# question-4
# ch = input("Enter an alphabet: ")

# if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#     print("Vowel")
# else:
#     print("Consonant")



# question-5
# initial = 2.19e14
# final = 4.68e14

# growth = ((final - initial) / initial) * 100

# print("Percentage growth =", round(growth))



# question-6
# months = int(input("Enter number of months: "))

# years = months // 12
# remaining_months = months % 12

# print("Years =", years)
# print("Months =", remaining_months)




# question-7
# color = input("Enter the beacon color: ")
# status = input("Enter steady or flashing: ")

# if color == "blue" and status == "steady":
#     print("Clear view")
# elif color == "blue" and status == "flashing":
#     print("Clouds due")
# elif color == "red" and status == "steady":
#     print("Rain ahead")
# elif color == "red" and status == "flashing":
#     print("Snow instead")
# else:
#     print("Invalid input")




# question-8
# cost = float(input("Enter cost: "))
# revenue = float(input("Enter revenue: "))

# if revenue == cost:
#     print("Break even")
# elif revenue > cost:
#     print("Profit =", revenue - cost)
# else:
#     print("Loss =", cost - revenue)




# question-9
# widgets = int(input("Enter number of widgets: "))

# if widgets >= 100:
#     cost = widgets * 0.20
# else:
#     cost = widgets * 0.25

# print("Total cost =", cost)




# question-10
# pounds = float(input("Enter number of pounds: "))
# cash = float(input("Enter cash tendered: "))

# cost = pounds * 2.50

# if cash >= cost:
#     change = cash - cost
#     print("Change = $", format(change, ".2f"))
# else:
#     owe = cost - cash
#     print("You owe $", format(owe, ".2f"), "more.")



# question-11
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b:
#     if a > c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b > c:
#         largest = b
#     else:
#         largest = c

# print("Largest number =", largest)




# question-12
# basic = float(input("Enter basic salary: "))

# HRA = 20 / 100 * basic
# TA = 5 / 100 * basic
# DA = 10 / 100 * basic

# gross = basic + HRA + TA + DA

# print("Gross Salary =", gross)


# question-13
# basic = float(input("Enter basic salary: "))

# HRA = 20 / 100 * basic
# TA = 5 / 100 * basic
# DA = 10 / 100 * basic

# gross = basic + HRA + TA + DA

# print("Gross Salary =", gross)

# if gross < 300000:
#     tax = 0
#     print("Income Tax = 0%")
# elif gross <= 1000000:
#     tax = 10 / 100 * gross
#     print("Income Tax = 10%")
# elif gross <= 2500000:
#     tax = 20 / 100 * gross
#     print("Income Tax = 20%")
# else:
#     tax = 30 / 100 * gross
#     print("Income Tax = 30%")

# print("Tax Amount =", tax)

