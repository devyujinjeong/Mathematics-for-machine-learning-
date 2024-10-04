import numpy as np
import matplotlib.pyplot as plt

# ypoints = np.array([3,8,1,10])
# plt.plot(ypoints,'o:r')
# plt.show()

# x = np.array([1,2,3,4])
# y1 = 2*x
# y2 = -x+2
# plt.plot(x,y1,'o-r', label = "Line1")
# plt.plot(x,y2,'x-.b', label = "Line2")
# plt.show()
# plt.savefig("plot1.png")

# x = np.random.randint(50)
# y= np.random.randint(50)

# colors = np.random.randint(50)
# sizes = 1000*np.random.randint(50)

# plt.scatter(x,y,c=colors,s=sizes,cmap='plasma',alpha=0.6)
# plt.colorbar(label = 'Color Scale')
# plt.title("Scatter Plot With Coloring")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# 시드
np.random.seed(10) 

# 난수 생성
random_numbers = np.random.rand(5)
print(random_numbers)

np.random.seed(1) 

# 난수 생성
random_numbers = np.random.rand(5)
print(random_numbers)