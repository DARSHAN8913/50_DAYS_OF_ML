# #Basic Syntax:
# # def funname():
#      #  body

# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# l=[2,5,656,]
# print(type(l))           # type() function return type of var entered
# # o/p:             
# # <class 'list'>

# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # def test():
# #                              #returns error if no statements are present 
# # avoid this by writing "pass"
# def test():
#     print("hello 5554")
#     pass                     #o/p: null (bcoz no statement is executed) if "pass" is present
#     print("hello 5556")

 
# # doesnt throws any exceptions
# # the "pass" keyword is a null operation or a no-op statement. It serves as a placeholder where syntactically
# # some code is required but you don't want to perform any action. It is often used as a placeholder in situations 
# # where the syntax requires a statement but no action is desired or necessary.

# def test1():
#     print("my first test")
# test1()                          #    o/p:my first test
# print(test()+"fgth" )    #TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
#                          # means that as print returns None data type and cant 
#                          # concatenate with string

# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # fixing above scenario by returning the string:
# def test2():
#     return "test"
# print("my first "+test2())               #    o/p:my first test

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def multi():
#     return 3,4.6,"gge",[446,5156,64646]        #functions can return multiple variables
# a,b,c,d=multi()
# print(a,b,c,d)                              #      o/p:   3 4.6 gge [446, 5156, 64646]

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def sinc(a,b):
#     return a+b
# print(sinc(5,6.2))      #o/p:  11.2
# print(sinc("hello"," everyone"))        #o/p: hello everyone  
# print(sinc([1,2,3],[3,4,5]))                #o/p:  [1, 2, 3, 3, 4, 5]

# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# #Extract INT values from given list 

# def test3(l):
#     l1=[]
#     for i in l:
#         if type(i)==int or type(i)==float:
#               l1.append(i)
#     return l1
# l=[2,4,5,6,3,"fvf","vfv",[8,7,6,0,4]]
# l2=test3(l)
# print(l2)                                      #  o/p: [2, 4, 5, 6, 3]

# # Extract INT values from given list of list and also from list

# def test4(l):
#     #following is a Docstring that tells the purpose of function once we mention it in our code and 
#     # want to access its purpose quickly  
#     """this is a test to find INT values from given list of list and also from list"""
#     l1=[]
#     for i in l:
#         if type(i)==int or type(i)==float:
#               l1.append(i)
#         elif type(i)==list:
#              for  j in i:
#                   if type(j)==int or type(j)==float:
#                      l1.append(j)
                  
# #     return l1
# # l=[2,4,5,6,3,"fvf","vfv",[8,7,0,4]]
# l2=test4(l)
# print (l2)                                #  o/p: [2, 4, 5, 6, 3, 8, 7, 0, 4]

# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # *args (called as static of args) is the tuple of n arguments (dynamical parameters)
# def asd(*args):
#     return args
# print(type(asd()))                   # o/p: <class 'tuple'>
# # also "args" is not a keyword it can be anything

# # #example:
# print(asd(1, 2, 3))                    # o/p: (1, 2, 3)

# def asd2(*args,a):
#     return args,a
# print(asd2(1,5,6,7))    #o/p: TypeError: asd2() missing 1 required keyword-only argument: 'a'
#                         # creates abiguity for value assignments if values
#                         #  are not specified clearly

# print(asd2(1,6,2,a=10))          #o/p: ((1, 6, 2), 10)
#                         #here values (1,6,2) are considered as for args var and
#                         #  a has been passed as a=10

# def asd3(c,d,a=9,t=7):        #default set must be follwed by non-default args
#     return c,d,a,t
# print(asd3(5,6,10,t=56))      #o/p: (5, 6, 10, 56)
#                               #default set values can be overwritten

# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def asd4(**kwargs):
#     return kwargs      #kwargs is a dict

# print(asd4([1,2,3,5],"vv",56.23))   #o/p: asd4() takes 0 positional arguments
#                                     # but 3 were given
#                                     # it says only key value pair args are allowed

# print(asd4(a=[0,98,7], b="khbjoij",c=56565.216)) 

# # o/p:{'a': [0, 98, 7], 'b': 'khbjoij', 'c': 56565.216}

################################################################################################

# Generator functions:
# functions that generate an ordered sequence of data serially 
#examples: range() function

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q: Gen a Fibonacci sequence
# def fib(n):
#     a,b=0,1
#     for i in range(0,n):
#         yield a
#         b,a=b+a,b           #this type of assignment executes parelelly i.e even 
#                             #even though we change b,a to a,b and respectively in RHS
#                             #we get the same result
# for i in fib(10):
#     print(i,end=" ")

# iter() function:

# iter() is used to obtain an iterator from an iterable object.
#  Iterators are used to iterate over a sequence of elements, such as a list, tuple,
#  or other iterable objects.(also int and float are not supported)
# Syntax: iterator = iter(iterable) 
# next() function:

# next() is used to retrieve the next element from an iterator.
# Syntax: element = next(iterator, default), where default is optional and specifies
# a value to return if the iterator is exhausted.

# Create a list
# my_list = [1, 2, 3, 4, 5]

# # Obtain an iterator from the list using iter()
# my_iterator = iter(my_list)

# # Retrieve elements using next()
# print(next(my_iterator))  # Output: 1
# print(next(my_iterator))  # Output: 2
# print(next(my_iterator))  # Output: 3

# # Using next() with a default value when the iterator is exhausted
# print(next(my_iterator, "End of List"))  # Output: 4
# print(next(my_iterator, "End of List"))  # Output: 5
# print(next(my_iterator, "End of List"))  # Output: "End of List"



        








