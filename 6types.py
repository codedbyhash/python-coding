#Math module
import math

x=10.8
print('For x =',x)
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print('-'*20)

x = 3
print('For x =',x)
print(math.exp(x))
print(math.log(x))
print('-'*20)

x = 90
print('For x =',x)
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print('-'*20)

#Random module
import random 

random.seed(40)
print(random.random())
print(random.randint(1,11))
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5],2))
print(random.uniform(1.0,9.0))
print('-'*20)

#date time
import datetime
print(datetime.datetime.now())
print(datetime.datetime(2023,10,28, 10,20,0))
print(datetime.datetime.now().strftime("%d-%m-%y"))
date_1 = datetime.datetime(2023,10,28, 10,20,0 )
date_2 = datetime.datetime.now()
print(date_2-date_1)
print('-'*20)

#collections module
from collections import Counter, OrderedDict, defaultdict
list1 = [1,2,3,4,5,5,6,6,6,7,8,8,8,8]
print(Counter(list1))
print('-'*20)

#default dictionary 
d = defaultdict(int)
d['a'] += 1
print(d)

d = OrderedDict()
d['a'] = 1
d['b'] = 2
print(d)
print('-'*20)

#strings 
import string 
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
