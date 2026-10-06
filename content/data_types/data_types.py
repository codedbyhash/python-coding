name = "Hashmeet"
age = 19
height = 5.4
student = True
print(type(name))
print(type(age))
print(type(height))
print(type(student))

print(name[1])  # character at index 1
print(len(name))  # length of the string
print("hi\n" * 3)  # repeating the string
text = "python"
print(text.upper())  # uppercase all the string values
print(text.lower())  # lowercase all the string values
print(text.capitalize())  # capitalize the string

# practice

Name = input("Enter your name: \n")
print("Welcome " + Name)
print("Length:", len(Name))
print(Name.capitalize())

# lists

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # accessing the first element
print(fruits[1])  # accessing the second element
print(fruits[2])  # accessing the third element
print(len(fruits))
fruits.append("orange")
fruits.remove("cherry")

# loop through the list

for fruit in fruits:
    print(fruit)

# tuples
colors = ("red", "green", "blue")
print(colors[0]) # accessing the first element

#dictionaries 
#key:value format 
#example
student={
    "name": "hashmeet",
    "age": 19,
    "course": "BCA"
}
print(student["name"]) # accessing the value using key
print(student["age"])
print(student["course"])

# practice
phone = {
    "brand": "Apple",
    "model": "iPhone 13",
    "price": 80000
}
print(phone)
phone["color"] = "Black"
print(phone)

name=input("Enter your name: \n")
print(name)
age = int(input("Enter age: "))
print(age)

# practice
student = {}
student["name"] = input ("Enter your name: \n")
student["age"] = int(input("Enter your age: \n"))
student["course"] = input("Enter your course: \n")
print(student)  
student["course"] = "MCA"
print(student)
python = "Python is a great programming language."
print(python.split())  # splitting the string into a list of words

print(python.split("a"))  # splitting the string at each occurrence of "a" 

