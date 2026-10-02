lst = [[1,2,3],[4,5,6],[7,8,9]]

print(lst)
print('-'*20)

#accessing the element
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print('-'*20)

lst[1][2] = 10
print(lst)
print('-'*20)

#appending the values
print(lst)
lst.append([9,10,11])
print(lst)
print('-'*20)

#modify the value
lst=[1,2,3,[4,5,6],[7,8,9]]
print(lst)
print(len(lst))
print('-'*20)

#reversing the element
print(lst[3])
print(lst[::-1])
print('-'*20)
