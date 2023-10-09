#write a program to swapping of two numbers
#First Menthod
a=int(input("Enter a value"))
b=int(input("enter b value:"))
print("Before Swapping")
temp=a
a=b
b=temp
print("After Swapping")
print(a)
print(b)
#Second Method
a=a+b
b=a-b
a=a-b
print(b)
print(a)
#Third Method
a,b=b,a
print(a)
print(b)4

