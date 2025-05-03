print("hello")

# name = input("enter your name:")
# age= int(input("enter your age:"))

# print(name)
# print(age)

for i in range(0,10):
    print(f"this is {i}")


def fun(n):
    print(f"the number is {n}")


fun(10)

#list

li = [1, 2, 3, 4, 5]
print(li)
print(li[0])

set1 = {1, 2, 3, 4, 5}
print(set1)

set2 = {1, 2, 3, 4, 5}
print(set2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

#tuple
tup = (1, 2, 3, 4, 5)
print(tup)


dict = {"name": "john", "age": 25}
print(dict)
print(dict["name"])


print(3*"hai")
print("City name"+"bangalore")



a,b=2,4
print(a)
print(a,b)
print(a,b,sep=",")
print(a,b,sep=":")
print("hello all!\n",end="")
print("how are you?")

name = input("Enter your name:")
age = input("enter your age:")
salary = int(input("Enter your salary:"))
print("Name and type:",name,type(name))
print("Salary and type",salary,type(salary))


