import numpy as np
import matplotlib.pyplot as plt

# Problem 1
C1 = (np.sin(1), np.sin(np.sin(1)), np.sin(np.sin(np.sin(1))))
C2 = (np.log(3), np.log(np.log(3)), np.log(np.log(np.log(3))))
C3 = (2**(1/2), (2**(1/2))**(1/2), ((2**(1/2))**(1/2))**(1/2))

norms = {
    "C1": np.linalg.norm(C1),
    "C2": np.linalg.norm(C2),
    "C3": np.linalg.norm(C3)
}
cloest_point = min(norms, key=norms.get)
print("Problem 1:",cloest_point)

# Problem 2
A = np.array([[1, -1, 2],[-2, 0, 3],[1, 1, 4]])
b = np.array([[1],[-1],[2]])
x =  np.linalg.solve(A,b)

A_det = np.linalg.det(A)
A1_det = A_det * x[0, 0]  
A2_det = A_det * x[1, 0]
A3_det = A_det * x[2, 0] 

print("Problem 2:")
print(f"A_det = {A_det:.1f}, A1_det={A1_det:.1f}, A2_det={A2_det:.1f},  A3_det={A3_det:.1f}")

# Problem 3
xpoints = np.array([-1, 2, 3])
ypoints = np.array([9, 12, 25])

x1, y1 = xpoints[0], ypoints[0]
x2, y2 = xpoints[1], ypoints[1]
x3, y3 = xpoints[2], ypoints[2]

A = np.array([[x1**2, x1, 1], 
              [x2**2, x2, 1], 
              [x3**2, x3, 1]])

coefficients = np.linalg.solve(A, ypoints)
a, b, c = coefficients

def quadratic(x):
    return a * x**2 + b * x + c

x_range = np.linspace(-2, 4, 100)
y_range = quadratic(x_range)

plt.title('Problem 3')
plt.plot(x_range, y_range, 'r-')
plt.scatter(xpoints, ypoints, color='blue', marker='o')

plt.show()

# Problem 4
theta = np.linspace(0, 2 * np.pi, 1000)

r = 2 - 2 * np.sin(theta) + np.sin(theta) *np.sqrt(np.abs(np.cos(theta)))/(np.sin(theta)+1.4)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.title('Problem 4')
plt.plot(x, y)
plt.show()

# Problem 5
np.random.seed(10)

C1 = (1, 1)
C2 = (-1, -1)

group1_x = np.random.normal(loc=C1[0], scale=1, size=20)
group1_y = np.random.normal(loc=C1[1], scale=1, size=20)

group2_x = np.random.normal(loc=C2[0], scale=1, size=30)
group2_y = np.random.normal(loc=C2[1], scale=1, size=30)

plt.title('Problem 5')
plt.scatter(group1_x, group1_y, color='red', label='Group 1')
plt.scatter(group2_x, group2_y, color='blue', label='Group 2')
plt.show()

# Problem 6
np.random.seed(10)

x_points = np.random.uniform(-3, 3, 50)
y_points = np.random.uniform(-3, 3, 50)

colors = []

for i in y_points:
    if i > 0:
        colors.append('red')
    else:
        colors.append('blue')

plt.title('Problem 6')
plt.scatter(x_points, y_points, color=colors)
plt.show()

# Problem 7
x1 = np.array([1,2,3,4])
x2 = np.array([1,2,3,4])

def function1(x):
    return 2*x

def function2(x):
    return -x+2
    
y1 = function1(x1)
y2 = function2(x2)

plt.title('Problem 7')
plt.plot(x1,y1,'x-.r',label='x-title')
plt.plot(x2,y2,'o--b',label='y-title')
plt.legend()
plt.show()

# Problem 8
def sin_function(x):
    return np.sin(x)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def taylor_polynomial(x, degree):
    result = 0
    for n in range(1, degree + 1):
        if n % 2 == 1: 
            result += ((-1)**((n - 1) // 2) * (x**n) / factorial(n))
    
    return result

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

y_sin = sin_function(x)
y_taylor_1 = taylor_polynomial(x, 1)
y_taylor_3 = taylor_polynomial(x, 3)
y_taylor_5 = taylor_polynomial(x, 5)
y_taylor_7 = taylor_polynomial(x, 7)

plt.title('Problem 8')
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_taylor_1, label='Taylor Degree 1')
plt.plot(x, y_taylor_3, label='Taylor Degree 3')
plt.plot(x, y_taylor_5, label='Taylor Degree 5')
plt.plot(x, y_taylor_7, label='Taylor Degree 7')
plt.legend()
plt.show()

# Problem 9
num_points = int((2 * np.pi) / 0.1) + 1 
x = np.linspace(0, 2 * np.pi, num_points) 
y = np.cos(x)
z = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Problem 9")
ax.plot(x, y, z)
plt.show()

# Problem 10
start = -5
stop = 5
step = 0.2

num_points = int((stop - start) / step) + 1

x = np.linspace(start, stop, num_points) 
y = np.linspace(start, stop, num_points)  
x,y = np.meshgrid(x,y)
z = np.sin(np.sqrt((x**2 + y**2)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z) 
ax.set_title('Problem 10')
plt.show()