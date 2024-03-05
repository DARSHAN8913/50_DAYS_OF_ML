#Basic Syntax:
#def funname():
    #  body

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# l=[2,5,656,]
# print(type(l))           # type() function return type of var entered
# o/p:             
# <class 'list'>

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def test():
#                              #returns error if no statements are present 
# avoid this by writing "pass"
# def test():
#     pass
# doesnt throws any exceptions
# the "pass" keyword is a null operation or a no-op statement. It serves as a placeholder where syntactically
# some code is required but you don't want to perform any action. It is often used as a placeholder in situations 
# where the syntax requires a statement but no action is desired or necessary.

# def test():
#     print("my first test")
# # test()                          #    o/p:my first test
# print(test()+"fgth" )                  #TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
                                #means that as print returns None data type and cant concatenate with string

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# fixing above scenario by returning the string:
# def test():
#     return "test"
# print("my first "+test())               #    o/p:my first test

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def multi():
#     return 3,4.6,"gge",[446,5156,64646]        #functions can return multiple variables
# a,b,c,d=multi()
# print(a,b,c,d)                              #      o/p:   3 4.6 gge [446, 5156, 64646]

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def sinc(a,b):
#     return a+b
# print(sinc(5,6.2))      #o/p:  11.2
# print(sinc("hello"," everyone"))        #o/p: hello everyone  
# print(sinc([1,2,3],[3,4,5]))                #o/p:  [1, 2, 3, 3, 4, 5]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Extract INT values from given list 

# def test7(l):
#     l1=[]
#     for i in l:
#         if type(i)==int or type(i)==float:
#               l1.append(i)
#     return l1
# l=[2,4,5,6,3,"fvf","vfv",[8,7,6,0,4]]
# l2=test7(l)
# print(l2)                                      #  o/p: [2, 4, 5, 6, 3]

# Extract INT values from given list of list and also from list

# def test7(l):
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
# l2=test7(l)
# print (l2)                                #  o/p: [2, 4, 5, 6, 3, 8, 7, 0, 4]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# *args (called as static of args) is the tuple of n arguments (dynamical parameters)
def asd(*args):
    return args
# print(type(asd()))                   # o/p: <class 'tuple'>

#example:
print(asd(1, 2, 3))                    # o/p: (1, 2, 3)







