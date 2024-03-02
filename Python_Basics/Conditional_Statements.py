mk=int(input("enter the marks")) #conversion to int
                                 #as comparison  is with int (typecast)
if mk>=80:
    print("A grade!!!")
elif mk>=60 and mk<80:
    print("b Grade!!!!")
else:
    print("C grade :((")
#Nested if:
if mk>=60:  
    if mk>=80:
        print("A grade!!!!")
    elif mk>=70:
        print("A- grade :)")
else:
    print("C grade :((")
#------------------------------------------------------------------------------------------------------------------------------------------------

l=[1,3,5,6,7,8]
l1=[]
# For Loop:
for i in l:
    l1.append(i+1)
print(l1)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

l2=["hi","should","efn"]
l3=[]
for i in l2:
    l3.append(i.upper())
print(l3)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l4=[1,2,3,4,"hi","should",567,6.89,"efn"]
l_int=[]
l_str=[]
for i in l4:
    if type(i)==int or type(i)==float:
        l_int.append(i)
    elif type(i)==str:
        l_str.append(i)
print(l_str)
print(l_int)

#-----------------------------------------------------------------------------------------------------------------------
#For-Else:
ls=['sid','fgt',"geg"]
for i in ls:
    if i=='fgt':
        break
    print(i)
else:
     print("$$ BREAK-CASE,exec if for lp is able to complete itself")

for i in ls:
    if i=='fgt':
        continue
    print(i)
else:                #here else part executes bcoz for loop is executed successfully
    print("$$CONT-CASE, exec if for lp is able to complete itself")
#------------------------------------------------------------------------------------------------------------------------
#Range: it produces desired seqence of data 
# Sytx: range(start, end,step)
# list(range(5))  # Output: [0, 1, 2, 3, 4]
#list(range(2, 7))  # Output: [2, 3, 4, 5, 6]
# print(list(range(11, 0, -2)))  # Output: [11, 9, 7, 5, 3, 1]
# print(list(range(11, 0,0))) #ValueError: range() arg 3 must not be zero
#--------------------------------------------------------------------------------------------------------------------------------
l4=[1,2,3,4,"hi","should",567,6.89,"efn"]
for i in range(len(l4)-1,-1,-1):
    print(l4[i])               
# 6.89
# 567
# "efn"
# should
# "hi"
# 4
# 3
# 2
# 1
# This code snippet prints the elements of the list `l4` in reverse order, starting from the end of the list and 
# moving backwards to the beginning. The `range()` function is used with a step of -1 to achieve this. also end 
# is designated as -1 instead of 0 bcoz range()function ommits the last element of the list 
#--------------------------------------------------------------------------------------------------------------------------------

#Even Element print:
for i in range(0,len(l4),2):
    print(l4[i])
# 1
# 3
# hi
# 567
# efn
#--------------------------------------------------------------------------------------------------------------------------------
# ls=[1,2,3,4,5]
# print(sum(ls))  output:15
d={"k1":"hi","k2":"hello","k3":"open","k4":"close"}
for i in d.keys():
    print(d[i])    #accesing values using keys
for i in d.values():
    print(i)         #accesing values directly

for i in d.items():
    print(i)           #returns key value pair in tuples:
#('k1', 'hi')
# ('k2', 'hello')
# ('k3', 'open')
# ('k4', 'close')
 
#--------------------------------------------------------------------------------------------------------------------------------
# sum of nur till limit:
n=input("entr ur limit")
sum=0
while n>0:
    sum+=1
    n-=1
#--------------------------------------------------------------------------------------------------------------------------------

#Factorial :
n=int(input("entr nor"))
f=1
while n>0:
    f=f*n
    n-=1
print(f)

#--------------------------------------------------------------------------------------------------------------------------------

#Fibonacci algorithm:
num=int(input("enr the number u aare looking for:"))
a,b=0,1
c=0
count=0
while count<num:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1

#--------------------------------------------------------------------------------------------------------------------------------

#reversing str:
word = input("entr str: ")
leng=len(word)
rev=''
while leng>0:
    rev+=word[leng-1]
    leng-=1
print(rev)

#--------------------------------------------------------------------------------------------------------------------------------

#while-else:
n=5
i=1
while i<n:
    print(i)
    if i==3:
        break
    i+=1
else:
    print("execs if while while completely execs")



    



    





