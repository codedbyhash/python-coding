lst = ['Hashmeet', 'Sahil', 'Raghav', 'Shivam', 'Satyarth', 'Anshul']

print(lst)
print('-'*20)

#access the elements of the list
print(lst[0])
print(lst[4])
print(lst[-1])
print('-'*20)

#modify values
print(lst)
lst[0] = 'Anshul'
print(lst)
print('-'*20)

#slicing
print(lst[0:4])
print('-'*20)

#reverse a string
print(lst)
print(lst[::-2])
print('-'*20)

#acessing the elemets of a list using loops
print(lst)
for i in lst:
    print (i)
print ('-'*20)

#acessing the elments of a list using indexing 
print(lst)
for i in range(len(lst)):
    print(lst[i])
print ('-'*20)

#length of the list
print(lst)
print(len(lst))
