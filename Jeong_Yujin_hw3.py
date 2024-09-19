# problem 1
print("Problem 1:")
x =(5,15)
for i in x:
    if i >= 10:
        print("x is greater than 10")
print()

# problem 2
print("Problem 2:")
y =(4,0,-3)
for i in y:
    if i > 0:
        print("y is positive")
    elif i < 0:
        print("y is negative")
    else:
        print("y is zero")
print() 

# problem 3
print("Problem 3:")
coordinates = [(4, 10), (7, 7), (-2, -10)]

for coor in coordinates:
    a, b = coor
    if a > b:
        print("a is greater than b")
    elif a < b:
        print("a is less than b")
    else:
        print("a is equal to b")
print()  

# problem 4
print("Problem 4:")
n =(3,15)
for i in n:
    if i >= 10 and i <= 20:
        print("n is between 10 and 20")
    else:
        print("n is not between 10 and 20")
print() 

# problem 5
print("Problem 5:")
s = 85
if s >= 90:
    print("A")
elif s >= 80 and s <= 89:
    print("B")
elif s >= 70 and s <= 79:
    print("C")
elif s >= 60 and s <= 69:
    print("D")
else:
    print("F")
print()  

# problem 6
print("Problem 6:")
h = (45, 38)
hourly_wage = 40
overtime_rate = hourly_wage * 0.5

for i in h:
    if i <= 40:
        pay = i * hourly_wage
        print(pay)
    else:
        regular_hours = 40
        overtime_hours = i - regular_hours
        pay = (regular_hours * hourly_wage) + (overtime_hours * overtime_rate)
        print(pay)
print()  

# problem 7
print("Problem 7:")
age = 20
registered_voter = True

if age >= 18 and registered_voter:
    print("You can vote")
else:
    print("You can't vote")
print()  

# problem 8
print("Problem 8:")
k = 4
if k % 2 == 0:
    print("Even")
else:
    print("Odd")
print() 

# problem 9
print("Problem 9:")
num = 75
if num >= 100:
    print("High")
elif num <= 50:
    print("Low")
else:
    print("Medium")
print()  

# problem 10
print("Problem 10:")
# 각 식의 계수 (a, b, c)를 튜플 형식으로 저장
equations = [
    (2, 8, 8),     
    (-5, 3, -4), 
    (-2, 7, 4)  
]

for a, b, c in equations:
    D = b**2 - 4*a*c
    print(f"{a}x^2 + {b}x + {c} = 0")

    if D > 0:
        print("The equation has two roots.")
        print((-b + D**(1/2)) / (2*a))
        print((-b - D**(1/2)) / (2*a))
    elif D == 0:
        print("The equation has one root.")
        print((-b + D**(1/2)) / (2*a))
    else:
        print("The equation has no real root.")
    
    print() 
