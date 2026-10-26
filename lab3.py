# question-1
# import math

# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# r = float(input("Enter radius: "))

# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))

# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# if distance < r:
#     print("The point lies inside the circle")
# elif distance == r:
#     print("The point lies on the boundary of the circle")
# else:
#     print("The point lies outside the circle")



# question-2
# import math

# s = float(input("Enter the side of the pentagon: "))

# area = (5 * s**2) / (4 * math.tan(math.pi / 5))

# print("Area of pentagon =", area)





# question-3
# a = float(input("Enter first angle: "))
# b = float(input("Enter second angle: "))
# c = float(input("Enter third angle: "))

# if a <= 0 or b <= 0 or c <= 0 or a + b + c != 180:
#     print("Invalid triangle")
# elif a < 90 and b < 90 and c < 90:
#     print("Acute-angled triangle")
# elif a == 90 or b == 90 or c == 90:
#     print("Right-angled triangle")
# else:
#     print("Obtuse-angled triangle")



# question-4
# n = int(input("Enter a 4 digit number: "))

# a = n // 1000
# b = (n // 100) % 10
# c = (n // 10) % 10
# d = n % 10

# sum1 = a + b
# sum2 = c + d

# print("Sum of first two digits =", sum1)
# print("Sum of last two digits =", sum2)

# if sum1 == sum2:
#     print("Both sums are equal")
# else:
#     print("Both sums are not equal")




# question-5
# n = int(input("Enter a 5 digit number: "))

# a = n // 10000
# b = (n // 1000) % 10
# c = (n // 100) % 10
# d = (n // 10) % 10
# e = n % 10

# if a >= b and a >= c and a >= d and a >= e:
#     print("Largest digit =", a)
#     print("Position =", 1)

# elif b >= c and b >= d and b >= e:
#     print("Largest digit =", b)
#     print("Position =", 2)

# elif c >= d and c >= e:
#     print("Largest digit =", c)
#     print("Position =", 3)

# elif d >= e:
#     print("Largest digit =", d)
#     print("Position =", 4)

# else:
#     print("Largest digit =", e)
#     print("Position =", 5)



# question-6
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# a = a + b + c
# b = a - b - c
# c = a - b - c
# a = a - b - c

# print("a =", a)
# print("b =", b)
# print("c =", c)




# question-7
# n = int(input("Enter a 3 digit number: "))

# a = n // 100
# b = (n // 10) % 10
# c = n % 10

# sum = a + b + c

# if n % sum == 0:
#     print("Harshad number")
# else:
#     print("Not a Harshad number")




# question-8
# import math

# V = float(input("Enter initial quantity of water: "))
# N = int(input("Enter number of days: "))

# if V < 0 or N < 0:
#     print("Invalid input")
# else:
#     water = V * (0.95 ** N) + 10 * (1 - 0.95 ** N) / (1 - 0.95)
#     print("Quantity of water after", N, "days =", water, "litres")






# question-9
# a1 = float(input("Enter a1: "))
# b1 = float(input("Enter b1: "))
# c1 = float(input("Enter c1: "))

# a2 = float(input("Enter a2: "))
# b2 = float(input("Enter b2: "))
# c2 = float(input("Enter c2: "))

# D = a1 * b2 - a2 * b1
# Dx = c1 * b2 - c2 * b1
# Dy = a1 * c2 - a2 * c1

# if a1 == 0 and b1 == 0:
#     print("Invalid first line")

# elif a2 == 0 and b2 == 0:
#     print("Invalid second line")

# elif D != 0:
#     x = Dx / D
#     y = Dy / D
#     print("Point of intersection = (%.2f, %.2f)" % (x, y))

# elif Dx == 0 and Dy == 0:
#     print("The lines are coincident")

# else:
#     print("The lines are parallel")