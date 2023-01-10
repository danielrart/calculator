# 1.1: What is a function?

'''A function a is part of a code that accomplishes certain tasks.
you can use functions everytime in the same code and they are pretty useful for little programs.
'''

# creating a function

'''A function has 3 parts: The name of the function, the arguments in the function and the body
'''

def testfunc(myname):
    print(f'Full_name: {myname}')
    print('hello, %s' % myname)


'''the name of the function is testfunc, myname is the argument 
 and the body is the code block followed right after the argument.A function can also have far more arguments
'''

# 1.2 what is a method?

'''Methods are functions that can only be called if a certain data type exists'''

# exempale

numbers = [2, 4, 8, 0, 5, 9, 3]

numbers.sort()

'''the method sort sorts the numbers in the list,
 this is its one and only task so it can only be called if a list tuple etc exists'''


# 1.3 Arguments in functions.


'''There three types of arguments 1.Are default arguments 2.position arguments 3.named arguments'''

# default arguments

def full_name(first_name, last_name, middle_name=''):
    print(f'full name: {first_name} {middle_name} {last_name}')

'''before calling the function you have to give the default argument a meaning'''

first_name = 'Tom'

middle_name = 'Berry'

last_name = 'peterson'

full_name(first_name, last_name, middle_name)

full_name(first_name, last_name)

# positioned argumnets

'''position arguments are connected to the position they have in the function'''


full_name('Tom', 'Berry', 'Peterson')

#  named arguments

'''Named arguments are connected to the meaning they have given in the function'''

full_name(first_name='Tom', middle_name='Berry', last_name='Peterson')


# 1.4 returning the meaning in a function

'''return is a statement that you can use to inside a function or method
 to send the functions result back to the caller'''

def test_variable():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable
print(test_variable())


'''the return statement multiplies the meanings of the two variables'''

# returning one meaning

'''if I return only the meaning of one variable in the funtion python gives us an error message'''

