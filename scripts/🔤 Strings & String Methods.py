#string operations  --strings are immutable means we cannot change the string once it is created
name="Tony Stark"  
grade="A"
print(name.upper())
print(name.lower())

#find  -- returns the index of the first occurrence of the substring
print(name.find("St"))

#replace  -- replaces the substring with another substring
print(name.replace("Tony", "Iron"))
print(name.replace("Stark", "Man"))
print(name.replace("To","ph"))

#check presence
print("S" in name) #true


#question
product_a=input("Enter a product price: ")
product_b=input("Enter another product price: ")
product_c=input("Enter another product price: ")

total_bill=float(product_a) + float(product_b) + float(product_c)
avg_bill=total_bill/3
print("Total bill:", total_bill)
print("Average bill:", avg_bill)
