result = [num*2 for num in [1,2,3]]

print(result)
print('-'*20)

#using conditions(filtering) using list comprehensions

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even=[num for num in numbers if num%2==0]
print(even)
print('-'*20)

#example: names longer than 5 characters
names=["John", "Alexander", "Tom", "Jessica", "hullaaaa", "bobbybrown"]
long_names = [name for name in names if len(name)>5]
print(long_names)
print('-'*20)

#conditional expressions(if-else)
numbers = [1,2,3,4,5]
result = ["Even" if num % 2==0 else "Odd" for num in numbers]
print(result)
print('-'*20)

#working with strings
word="python"
letters = [char.upper() for char in word]
print(letters)
print("-"*20)

#extract vowels
word="developer"
vowels=[char for char in word if char in "aeiou"]
print(vowels)
print("-"*20)

#working with list of strings
names=['john', 'alice', 'bob']
capitalized = [name.capitalize() for name in names]
print(capitalized)
print('-'*20)

#using functions inside list comprehensions
def square(x):
    return x*x
numbers=[1,2,3,4]
result=[square(num) for num in numbers]
print(result)
print('-'*20)

#nested list comprehensions
pairs=[(x,y) for x in [1,2] for y in [10,20]]
print(pairs)
print('-'*20)

#how to flatten a matrix into one list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flatten=[num for row in matrix for num in row]
print(flatten)
print('-'*20)

#dictionary data processing
students=[
    {"name":"John","marks":90},
    {"name":"Alice","marks":80},
    {"name":"Bob","marks":95}
]
names=[student["name"] for student in students]
print(names)
print("-"*20)

#student management system
students=[
    {"name":"Andrew","marks":90},
    {"name":"Armani","marks":70},
    {"name":"Tristan","marks":95}
]
toppers=[
    student["name"]
    for student in students
    if student["marks"]>80
]
print(toppers)
print('-'*20)

#expense tracker
expenses=[200,500,1000,150,700]
updated = [expense *1.18 for expense in expenses]
print(updated)
print('-'*20)

#data cleaning
data=["john","bob","tom"]
clean=[name.strip() for name in data]
print(clean)
print('-'*20)

#generator expressions
G = (n ** 2 for n in range(12))
print(G)
print("-"*20)

#a generator expression is single-use
G = (n**2 for n in range(12))
for n in G:
    print(n, end= " ")
    if n>30: break
print("\ndoing something in between")
for n in G: 
    print(n, end=" ")
