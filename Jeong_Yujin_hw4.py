# problem1
a = 0
print('problem1')
while a<20:
    a = a+2
    print(a)
print()

# problem2
fruits = ["apple", "banana", "cherry", "date"]
print('problem2')
for fruit in fruits:
    print(fruit)
print()

# problem3
print('problem3')
for i in range(0,6):
    print(i**2)
print()

# problem4
person = {"name": "Alice", "age": 30, "city":"New York"}
print('problem4')
for key,value in person.items():
    print(f'key: {key} and value:{value}')
print()

# problem5
print('problem5')
for i in range(1,6):
    for j in range(1,6):
        print(f'{i}*{j}={i*j}')
    print('...')

# problem6
print('problem6')
n= (4,20)
for i in n:
    for k in range(1,i):
        answer = (-1)**k*k/2**k
    print(f'n={i}:{answer}')
print()

# problem7
x1 = 1
err = 1

while err>=10**-6:
    x = x1-(x1**2-21)/(3*x1**2)
    err = x-x1
    x1 = x
print(f'problem7: {x1} \n')

# problem8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x**2 for x in numbers if x%2==0]
print(f'problem8: {evens} \n')

# problem9
count = 0
primes = []
for i in range(10,51):
    for j in range(2,i):
        if i%j==0:
            count = count+1
            
    if count==0:
        primes.append(i)
    count = 0

print(f'problem9: {primes} \n')

# problem10
nums = [[i * j for j in range(5)] for i in range(5)]
print(f'problem10: {nums} \n')

