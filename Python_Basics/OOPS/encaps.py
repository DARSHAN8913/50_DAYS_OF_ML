# Encapsulation helps in hiding the internal state of an object from the outside world and accessing it only
# through well-defined interfaces. This way, it provides a way to protect the data from accidental
# corruption and ensures that the object's integrity is maintained.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class car:
    def __init__(self,year,make,model,speed):
        self.__year = year                # adding __ makes an attribute or a function private i.e it is can 
        self.__make = make                # only be accessed within the class and not even by subclasses
        self.__model=model
        self.__speed = speed

    def set_speed(self,speed):
        self.__speed = 0 if speed<0 else speed
    
    def get_speed(self):
        return self.__speed
    
c=car(2006,"toyota","fortuner",120)
c.__year=1000                                         
print(c.__year)        # o/p: 1000
print(c._car__year)    # o/p: 2006 i.e if we use _class-name__attribute-name we can access the 
                       # original  variable 
                         # c.__year creates a new attribute specific to the instance c, while c._car__year 
                         # accesses the original attribute defined in the class. This demonstrates the 
                         # mangling behavior of Python to enforce some level of name privacy.
c.set_speed(23)
print(c.get_speed())   # o/p: 23    