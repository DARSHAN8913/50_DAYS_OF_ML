class test :
    def pr(self):                #self keyword binds the function with class
        print("this is class")
    # def __init__(self,ph_number,)
    
a=test()
a.pr()          #o/P:this is class
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# passing data to the class
class test1:
    def __init__(self,ph_num,email,name):
        self.ph_num=ph_num                     
        self.email=email
        self.name=name

    def returning_data(self):
        return self.ph_num,self.email,self.name
rh=test1(651616,"ksfnv@gmail.com","tyson")
print(rh.returning_data())

