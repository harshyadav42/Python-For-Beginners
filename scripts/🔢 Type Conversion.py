#type casting --jo programmer krta h   or type conversion --jo  krta interpreter khud krtaa h
# anything we are taking input is string as default so we need to type cast it 
age=input("Enter your age: ")
print(type(age))      

new_age=int(age) + 1
print(new_age)
print(float(new_age))

a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
sum=a+b
print("The sum of", a, "and", b, "is", sum)
