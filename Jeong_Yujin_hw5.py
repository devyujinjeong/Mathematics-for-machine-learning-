# problem1
print("Problem1:")

def greet():
    print("Hello,World!")
    
greet()
print()

# problem2
print("Problem2:")

def square(n):
    print(n**2)
    
square(4)
print()

# problem3
print("Problem3:")

def greet_user(name="Guest"):
    print(f"Hello, {name}")    
greet_user()
greet_user("정유진")
print()


# problem4
print("Problem4:")

def add(num1, num2):
    print(num1+num2)
add(5,10)
print()

# problem5
print("Problem5:")

def sum_all(*num):
    sum=0
    for i in num:
        sum+=i
    return sum

print(sum_all(1, 2, 3))
print(sum_all(5, 10))
print(sum_all(4, 7, 9, 12))
print()

# problem6
print("Problem6:")

def print_person(**person):
    for key, value in person.items():
        print(f"{key}: {value}")

print_person(name="Alice", age=30, city="New York")
print()
print_person(name="Bob", profession="Engineer")
print()

# problem7
print("Problem7:")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print()

# problem8
print("Problem8:")

getGcd = lambda x, y: x if y == 0 else getGcd(y, x % y)
        
print(getGcd(210,132))
print()

# problem9
import math

print("problem9:")

def AddVectPol(r1, th1, r2, th2):
    x1 = r1 * math.cos(th1)
    y1 = r1 * math.sin(th1)
    x2 = r2 * math.cos(th2)
    y2 = r2 * math.sin(th2)
    
    x = x1 + x2
    y = y1 + y2
    
    r = math.sqrt(x**2 + y**2)
    th = math.atan2(y, x)
    
    print(f"r:{r},th:{th}")

AddVectPol(5, 1.2, 13, 4.2)
AddVectPol(6, 8.3, 16, 1.26)
print()

# problem10
print("problem10:")
def apply_operation(numbers, operator):
    return [operator(x) for x in numbers]

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_operation(numbers, lambda x: x**2)
print("f(x) = x^2:", squared_numbers)
doubled_numbers = apply_operation(numbers, lambda x: 2*x)
print("f(x) = 2x:", doubled_numbers)