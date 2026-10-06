class person:
    name = 'Hash'
    age = 18

p1 = person()
print(p1.name)
print(p1.age)

print('-'*20)

p1.name = 'hashmeet'
p1.age = 20
print(p1.name)
print(p1.age)

print('-'*20)

p2 = person()
print(p2.name)
print(p2.age)

print('-'*20)

class mathematics:
    name = 'hash'

    def greet(self):
        print('hello world')
        print(self.name)

math = mathematics()
math.greet()
print(math.greet())
