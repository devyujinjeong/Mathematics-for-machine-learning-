# problem1
myList = [1,2,3,4,5]
myList.append(6)
print("pro1-1:",myList)

myList.remove(2)
print("pro1-2:",myList)

# problem2
thistuple = ("apple", "banana", "cherry", "date")
# 바나나 프린트 하기
print("pro2-1:",thistuple[1])
print("pro2-2:",thistuple[-3])

# date 프린트 하기
print("pro2-3:",thistuple[3])
print("pro2-4:",thistuple[-1])

# problem3
mySet = {1, 2, 3, 4}
mySet.add(5)
mySet.remove(2)
print("pro3:",mySet)

# problem4
list1 = ["apple", "banana", "cherry"]
list2 = ["date", "elderberry", "fig", "grape"]
list3 = list1[:2] + list2[2:]
print("pro4:",list3)

# problem5
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

my_dict["age"] = 26
my_dict["email1"] = "alice@example.com"
print("pro5:",my_dict)

# problem 6
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1-set2
print("pro6:",set3)

# problem 7
thistuple = (10, 20, 30, 40, 50)
temp_list = list(thistuple)
temp_list[2] = 35
thistuple = tuple(temp_list)
print("pro7:",thistuple)

# problem 8
students = {
    "student1": {"name": "John", "age": 18, "grade": "A"},
    "student2": {"name": "Jane", "age": 19, "grade": "B"},
    "student3": {"name": "Doe", "age": 20, "grade": "C"}
}
students["student3"]["grade"] = "A"
print("pro8:",students)

# problem 9
mystring = " Hello, World! "
mystring = mystring.strip()
print("pro9-(1):",mystring)

mystring = mystring.replace(",", "!")
print("pro9-(2):",mystring)

mystring = mystring.upper()
print("pro9-(3):",mystring)

# problem 10
pi = 3.1415926535
e = 2.7182818284
print("pro10:",f"Pi is approximately {pi:.2f} and e is approximately {e:.3f}.")


