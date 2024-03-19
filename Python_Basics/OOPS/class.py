class test :
    def pr(self):                #self keyword binds the function with class
        print("this is class")      #self is not a keyword and only acts as a pointer 
    # def __init__(self,ph_number,)
    
a=test()
a.pr()          #o/P:this is class
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# passing data to the class
class test1:
    def __init__(self,ph_num,email,name): 
        self.ph_num=ph_num                     
        self.email=email                  
        self.name=name 


    def returning_data(self):
        return self.ph_num,self.email,self.name   # self keyword must be associated as shown 
                                                  # to access a variable inside a class
        
rh=test1(651616,"ksfnv@gmail.com","tyson")
print(rh.returning_data())

class test1:
    def __init__(self,ph_num,email,name): 
        self.ph_num1=ph_num              # ph_num is a parameter used during initialization,
                                         # while ph_num1 is an attribute of the instance that holds 
                                         # the value passed to ph_num during instantiation.
        self.email=email                  
        self.name=name                 


    def returning_data(self):
        return self.ph_num,self.email,self.name  
tim=test1(46846484,"prashant@ukkali","ptim")
print(tim.ph_nm)                               # AttributeError: 'test1' object has no attribute 'ph_nm'
print(tim.ph_num1)                # O/p:  46846484

                                  
