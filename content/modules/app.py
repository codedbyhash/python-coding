#modules are used to organize code into separate parts of the file and can be imported into other files to use the functions defined in them
#modules decrease the need to write the same code again and again in different files, instead you can just import the module and use it
#modules are also used to separate the code into different files for better organization and readability. 

from support import greet
from support import subm
from support import arithmetic
from support import sq
from support import cu
from support import final

lst = [1,2,3,4,5]

print(greet('hash'))
print(subm(10,5))
print(arithmetic(10,5))
print(sq(lst))
print(cu(lst))
print(final(lst))