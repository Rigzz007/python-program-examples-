# basics for python
'''
#name = "abc"
#age = 26
#print(name,age)

#name = "xyz"
#age= 16.0
#if age>20:
 #print("true")
#else:
# print("false")

#print(name)
#print(age)

#name= input("what is your name?")
#print("hello" + " " + name)

#old_age= input("enter your old age")
#new_age= int(old_age) + 2
#print(new_age)
#number= 18
#print(float(18))
#first = input("input your first number:")
#second = input(" input your second number:")

#sum = int(first) + int(second)
#print(sum)
#print("the sum is:" + " " + str(sum))

#name ="tony stark"
#print(name.upper())
#print(name.replace("tony stark","ironman"))
#print(name.replace("t","i"))
#print(name.find("s"))
#print(name.find("i"))
#print("t" in name)
#print(5+1)
#print(5/2)
#print(5//2)
#print(5%2)
#print(5**2)
#i = 5
#i =i + 2
#i += 2
#i -= 2
#print(i)
#result = 2 + 3 * 5
#print(result)
#result = (2 + 3) * 5
#print(result)
#print (3<2)
#print (3>2)
#print (3==2)
#print (3!=2)
#print(3>2 and 2>3)
#print(3>2 or 2>3)
#print( not 3>2 )
#age = 19
#if age >= 18:
#    print("you are an adult")
#    print("you can vote")
#print("thank you")
#elif age <18 and age >3:
 #   print("you are in school")
#else:
  #  print("you are a child ")
#first =input("enter first number:")
#operator = input("entre operator(+,-,*,/,%,**)")
#second = input("entre second operator:")
#first=int(first)
#second=int(second)
#if operator == "+":
#    print(first+second)
#elif operator == "-":
#    print(first-second)
#elif operator == "/":
#    print(first/second)
#else:
#    print("invalid operation")

#number = range(5)
#print(number)

#i = 1
# while i <=5:
 #    print(i)
 #    i=i+1




#i =1
#while i <=5:
 #    print(i * "*")
 #    i=i+1
#i = 5
#while i >=0:
 #    print(i * "*")
  #   i=i-1

#for i in range(5):
 #   print(i)

#marks = [95,98,97]
#print(marks)
#print(marks[0])
#print(marks[-1])
#print(marks[0:2])
#for score in marks:
 #   print(score)

#marks.append(99)
#marks.insert(0,99)
#print(marks)
#print(99 in marks)
#print(len(marks))
#i=0
#while i < len(marks):
 #   print(marks[i])
  #  i=i+1

#marks.clear()
#print(marks)

#students = ["ram", "shyam" , "kishan" , "radha" , "radhika"]
#for student in students:
 #   if student== "radha":
  #      break;
   # if student== "kishan":
    #    continue;
 #   print(student)


#toupple
#marks=(95,98,97)
#print(marks.count(95))
#print(marks.index(97))

#sets
#marks={95,98,97,97,97}
#print(marks)
#for score in marks:
 #   print(score)

#marks={"english": 95 , "chemistry":98}
#information={"ram":"balkishan"}
#print(marks["chemistry"])
#marks["physics"] =97;
#print(marks)
#marks["physics"] =99;
#print(marks)


#modual
#import math
#from math import sqrt
#print(dir(math))
#from math import *
#print(sqrt(16))

#function
#def print_sum(first,second):

#def print_sum(first,second=4):
 #print(first+second)
#rint_sum(1,2)
#print_sum(1)

#a=int(input("enter A:"))
#if a>0:
#    print(" a is positive nymber")
#else:
#    print(" a is negative number")

#a=int(input("enter A:"))
#if a%2!=1:
 #   print("a is evan number")
#else:
 #   print("a is odd number")
'''
# new code complete star from 1 to 5 from left to right
'''
n= 5
i=0
n=int(input("enter the number"))
for i in range(0,n):
  for j in range(0, i+1):
     print("*", end="")
  print()
'''
# new code complete start from 1 to 5 from right to left
'''
n=5
k=n-1
for i in range(n):
   for j in range(k):
    print(" ",end="")
   k=k-1
   for j in range(i+1):
    print("*", end="")
   print()

'''
# new code complete start from 1 to 5 from right to left
'''
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")          #print("*",end=" ")
    print()

'''
#complete  start from 5 to 1 left to right
'''
n=5
for i in range(n):
    for j in range(i,n):            #for j in range(n-i):
        print("*",end="")
    print()

'''
# new code complete with space between star from 1 to 5 right to left
'''
n=5
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2                       # decrement k value after each iteration
    for j in range(0, i + 1):
        print("* ", end="")         # printing star
    print("")

'''
# new code complet start from 5 to 1 left to right
'''
n=5
for i in range(n):
   for j in range(i):
     print(" ",end="")
    for j in range(n-i):
     print("*",end="")          #print("*",end="")
    print()
'''
# new code complete starr from christmus tree top to down
'''
n=10
m=(2*n)-2
for i in range(n):
    for j in range(0,m):
        print(" ",end="")
    m=m-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")                #print()
'''
# new code complete downward cristmus tree
'''
n=10
m=(2*n)-2
for i in range(n,-1,-1):
    for j in range(m,0,-1):
        print(" ",end="")
    m=m+1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")                   #print()
'''
# new code complete count of vowel and consonant in string
'''
s=input("enter the string:")
vowel=0
consonant=0
for i in s:
    if(i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="a"or i=="e"or
    i=="i"or i=="o"or i=="u"):
        vowel=vowel+1
    else:
        consonant=consonant+1
print("number of vowel",vowel)
print("number of consonant",consonant)
'''
#2) complete
'''
s=input("enter the string:")
vowel=0
consonant=0
for i in s:                            #NOTE
    if(i=="A","E","I","O","U"):        #this type of method is not working
        vowel=vowel+1
    else:
        consonant=consonant+1
print("number of vowel",vowel)
print("number of consonant",consonant)
'''
#3) complete with another method
'''
s=input("enter the string:")
vowel=0
consonant=0
for i in s:
 if i in("A","E","I","O","U","a","e","i","o","u"):
    vowel=vowel+1
 else:
    consonant=consonant+1
print("number of vowel is:",vowel)
print("number of consonant:",consonant)

'''

# new code for check string complete
'''
s=input("input string:")
ch=0
w=1
sp=0
n=0
special=0
for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
       sp=sp+1
       w=w+1
    elif i.isnumeric():
        n=n+1
    else:
      special=special+1

print("total special:",special)
print("total character:",ch)
print("total word:",w)
print("total space:",sp)
print("total number:",n)
'''
# new code for sting complete
'''
s="1233"
if s.isalpha():
    print("this is string")
else:
    print("this is not string")
'''

# neww code slicing complete
'''
#  01234567890123456
s="Tops Technologies"
#  76543210987654321

print(s[3:13])
print(s[:15])
print(s[2:])
print(s[3:15:3])
print(s[::5])
print(s[-14:-2])
print(s[-5])
print(s[-17:])
print(s[-15:-1:4])
print(s[::3])
print(s[::-3])
'''
# new code listasstack   LIFO:LAST IN FIRST OUT
'''
l=[]
l.append(10)        #append = add one value at a time like 10 then 20 then
print(l)            #30 then 40 then 50
l.append(20)
print(l)
l.append(30)
print(l)
l.append(40)
print(l)
l.append(50)
print(l)

l.pop()           #pop=remove last value like 50,40,30,20,10
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
'''
# new code LISTASQUEUE
'''
from _collections import deque
l=deque([])
l.append(10)
print(l)
print(list(l))     #casting method
l.append(20)
print(list(l))
l.append(30)
print(list(l))
l.append(40)
print(list(l))
l.append(50)
print(list(l))

l.popleft()           #_collections is a library and deque is a class of that
print(list(l))        #  library and popleft method provide that library which
l.popleft()           # remove last element first like 10,20,30,40,50
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
'''
#lucky numbers library random
'''
import random
print(random.randint(0,10))
l=[1,2,"tops","java","python",10,]  # for string choice method
print(random.choice(l))
'''
# new code for using list small project
'''
import random
l=[]
lucky=[]
for i in range(0,101):
    l.append(i)
for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)
print(l)
lucky.sort()                         #for assending order
lucky.sort(reverse=True)              #for disassending order
print(lucky)
'''
#new code touple
'''
# 1) touple only two library in toupple count and index
marks=(95,98,97)
print(marks.count(95))
print(marks.index(97))

'''
#2)
'''
t=(1,2,1.1,"tops",True,1,10)
print(t)
print(t.count(1))
print(t.index(2))
for i in t:          # this is called itterate
    print(i)
'''
#3)
'''
t=(1,2,1.1,"tops",[10,20,30],True,1,10)
print(t)                            #we can not change in toupple at run time
print(t.count(1))                   #But we can change list in toupple
print(t.index(2))                   #for exemple this program
for i in t:
    print(i)
print(1 in t)
print(len(t))
t[4].append(40)
print(t[4])
'''
# new code we can convert list in tuple
'''
l=[1,2,3]
t=tuple(l)
print(t)
l[2]=55
print(l)
'''
# new code we can convert tuple in list
'''
t=(1,2,3)
l=list(t)
print(l)
l[2]=100
print(l)
'''
#new code dictionary and list information
'''
#dictionary {}  store data using key and value form
#if we want to copy one dictionary to another then d1=d.copy() means d1 and d
#dictionary allocate differnet memory.
#if write d1=d then it's same memory allocate means d1 and d are same not copied
#in dictionary sequence is not matter and in list sequence is metter
#in dictionary we find data using key value pair
#in list we use pop to remove last data and pop(2) in which 2 is a index number
#in dictionary we use pop(2) in which 2 is key and pop() is not valid for dictionary
'''
#new code dictionary
'''
#complete key = (value)^2
d={}
n=int(input("enter the number: "))
for i in range (n):
    d[i]=i*i
print(d)
'''

# new code list
#1) list in which can devide by 5 and not devide by 7
'''


d=[]
for i in range(2000,3201):
    if i%5==0 and i%7!=0:
        d.append(i)
print(d)
'''
# 2) complete check each number odd or even in a number like 1234 in which 1 is odd 2 is even 3 is odd 4 is even and if all number is even then store in list
'''
l=[]
for i in range(1900,3001):
    s=str(i)                       #we can apply this method in string not numbers because in in string we can excess each element and not in numbers
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
        l.append(i)
print(l)
'''
#3)complete match two list and add common into new list
'''
l1=[10,20,30,40,50]
l2=[12,20,45,50,90]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

'''
#4) merge two list
'''

l1=[10,20,30,40,50]
l2=[60,70,80,90,100]
l1.extend(l2)
print(l1)
'''
#5) list functions
'''

l=[10,20,30,40,50]
l.pop()   #lasr element remove
l.pop(2)  #index number 2 is remove
l.clear() #clear all list
l.remove(20) # remove 20 number of data
del l[2]  #delete 2 index data
del l[1:3] #delete data from index number 1 to 2
del l
l[2]=100 #update 2 number of index number data
l[2:4]=[100,200] #update 2 to 4 number of index number data
l.insert(3,100) # insert 100 data in index number of 3
l.append(100) # add new data on new upcomming index number
print(l)

'''
#file management
'''
file=open("tops1.txt","w")    #threemode main w=wrie,r=read,a=append, and others are w+=write and read and r+=read and write
file.write("this is file managemnet demo using python")
file.close()
print("file return successfully")
file=open("tops1.txt","r")
print(file.read())
file.close()
file=open("tops1.txt","a")
file.write("\nthis file is appended")
file.close()
'''

'''
file=open("tops2.txt","w+")
file.write("this is w+ mode exemple")
print("current position:",file.tell()) #file.tell() function gives your cursor position
file.seek(0)     # seek is a library function which take a cursor on your given position
print(file.read())   # without this file.tell() and file.seek() function in w+ mode our cursor start at the end like after exemple
file.close()
file=open("tops2.txt","r+")
print(file.read())
file.write("\nthis is r+ mode exemple")
file.close()
'''

'''
import random
data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
        #print(data.read().split(",")[:-1])
        #data.close()
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt","w")
notprime=open("notprime.txt","w")

l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2!=0:
      for j in range(3,int(int(i)/2)+1):
          if int(i)%j==0:
            #break

            notprime.write(i+",")
            #print(j,"is not prime" )
            break

      else:
             prime.write(i+",")

    else:
            #prime.write(i+",")
         notprime.write(i+",")
            #print(j,"is prime")


#    if i==1 :
#        prime.write(i+",")
        #print(i,"is prime")
        #prime.write(i+",")
    if int(i)%2==0:
        even.write(i+ ",")

    else:
        odd.write(i+ ",")
data.close()
even.close()
odd.close()
prime.close()
notprime.close()

print("data file content")
data=open("data.txt","r")
print(data.read())
data.close()

print("even file content")
even=open("even.txt","r")
print(even.read())
even.close()

print("odd file content")
odd=open("odd.txt","r")
print(odd.read())
odd.close()

print("prime file content")
prime=open("prime.txt","r")
print(prime.read())
prime.close()

print("notprime file content")
notprime=open("notprime.txt","r")
print(notprime.read())
notprime.close()
'''
#new code list expand
'''
#l=[1,2,3]
#l1=[4,5]
#l.extend(l1)
#print(l)
'''
#new code prime number
'''
#n=int(input("enter the number:"))
#n=15
#if n>1:
#    for i in range(2,int(n/2)+1):
#        if (n%i)==0:
#            print(n, "is not prime number")
#            break
#    else:
#            print(n,"is prime number")
#else:
#    print(n,"is not prime number")
'''
#new code user define function
'''
#userdefine function : it is a set of instruction that perform a specific task.
'''
#1) function with no arhument and no return value.
'''
#def function name(arguments):     ():called  perameters
def printline():
    print("*"*50)
printline()
print("welcome to user defined function in python.")
printline()
'''
#2)
#function with arguments and without return value

'''
def add(a,b):
    print("addition:",a+b)
printline()
x=int(input("entre the first  value:"))
y=int(input("entre the second value"))
add(x,y)
#add(10,20)
printline()
'''
#3)
#function with argument and with return value

'''
def sub(a,b):
    return a-b
printline()
x=int(input("entre the first  value:"))
y=int(input("entre the second value"))
ans=sub(x,y)
print("subtraction:",ans)
print("subtraction:",sub(x,y))
printline()
'''
#4)
'''
def test(a=40,b=30,c=20,d=10):
    print("A :", a,"B :" ,b," C :" ,c," D :" ,d)
test(1,2,3)
test(1,2,3,4)
test(1,2)
test(1)
test()
'''
#5)
'''
#arbitary argument
#add last of all last arguments values using *
def test(a,b,c,*d):
    #print("A :", a,"B :" ,b," C :" ,c," D :" ,d) # give tuple last in d
    print("A :", a,"B :" ,b," C :" ,c," D :" ,list(d)) # give list last in d
test(1,2,3,4)
test(1,2,3,4,5,6,7,8,9)

#add dictionary **     this is also called arbitary argument
def test(a,b,c,*d,**e):
    print("A :", a,"B :" ,b," C :" ,c," D :" ,list(d)," E :",e)
test(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)
'''

#new code exception
#1)
'''
#exception handling  is an abnormal situation that arise during the run time of a program
try:
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    c=a/b
    print("division:",c)
except:
    print("exception caught:")
'''
#2)

'''
try:
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    c=a/b
    print("division:",c)

    l=[1,2,3,4,5]
    index=int(input("entre index number:"))
    print(l[index])
except ZeroDivisionError as e:
    print("exception caught:",e)

except ValueError as e:
    print("exception caught:",e)

except IndexError as e:
    print("exception caught:",e)
except Exception as e:            # parent class exception means all type of run time exception are includeed
    print("exception caught:",e)
finally:
    print("finally called")
'''
#new code prime number

'''
n=int(input("enter the number:"))
#n=15
if n>1:
    for i in range(2,int(n/2)+1):
        if (n%i)==0:
            print(n, "is not prime number")
            break
    else:
            print(n,"is prime number")
else:
    print(n,"is not prime number")
'''
#new code  prime number

'''
if n%2!=0:
    for i in range (3,int(n/2)+1,2):
        if n%i==0:
          print(n,"is not prime")
          break
    else:
        print(n,"is prime")
else:
    print(n,"is not prime")
'''
#new code import module UDF

'''
import UDF

while True:
    print("*"*20)
    print("1.oddeven")
    print("2.maxoftwo")
    print("3.maxofthree")
    print("4.fibonacci")
    print("5.prime")
    print("6.pattern")
    print("7.exit")
    print("*"*20)

    choice=int(input("enter your choice:"))
    print("*"*20)
    if choice==1:
        a=int(input("enter value:"))
        UDF.oddeven(a)
        print("*"*20)
        break
    elif choice==2:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        UDF.maxoftwo(a,b)
        print("*"*20)
        break
    elif choice==3:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        c=int(input("enter value:"))
        UDF.maxofthree(a,b,c)
        print("*"*20)
        break
    elif choice==4:
        a=int(input("enter value:"))
        UDF.fibonacci(a)
        print("*"*20)
        break
    elif choice==5:
        a=int(input("enter value:"))
        UDF.prime(a)
        print("*"*20)
        break
    elif choice==6:
        a=int(input("enter value:"))
        UDF.pattern(a)
        print("*"*20)
        break
    else:
        print("thank you")
        break
'''
# new code  forclass and object
'''
class Student:
    def getdata(self,fname,lname):
        self.f=fname
        self.l=lname
    def putdata(self):
        print("first name:",self.f)
        print("last name:",self.l)
s1=Student()
s1.getdata("rignesh","patel")
s1.putdata()

'''
#2) example of cass and object
'''
from datetime import datetime
class Bank:
    def openaccount(self,cname,balance,acno):
       self.cname=cname
       self.balance=balance
       self.acno=acno
       print("hellow ",self.cname,"your account number ",self.acno,"is opened with",self.balance,"Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("sorry you need another ",self.needs,"Rs.")
    def checkbalance(self,balance):

        print("current balance :",self.balance)

b1=Bank()
cname=input("enter customer name: ")
balance=int(input(" enter initial balance: "))
acno=int(input(" enter account number: "))

b1.openaccount(cname,balance,acno)
file=open(str(acno)+".txt","w")

while True:
    print("*******************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4.Exit")
    print("*******************************")
    choice=int(input("enter your choice: "))
    print("*******************************")
    if choice==1:
        amount=int(input("enter deposit amount:"))
        b1.deposit(amount)

        print("*******************************")
        file.write("\namount deposited:"+str(amount)+"on time: "+str(datetime.now()))

    elif choice==2:
        amount=int(input("enter withdraw amount:"))
        b1.withdraw(amount)


        print("*******************************")
        file.write("\namount withdrawal:"+str(amount)+"on time: "+str(datetime.now()))

    elif choice==3:
        b1.checkbalance(balance)

        print("*******************************")
        file.write("\nbalance checked at"+str(b1.checkbalance(balance))+"on time:"+str(datetime.now()))

    else:
        print("thank you")
        file.write("\ntransaction completed on time: "+str(datetime.now()))
        break
file.close()
'''
#3) exemple for inheritance

# 1) single inheritance
'''
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
b1=B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()
'''
#2) multilevel inharitance
'''

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)


c1=C()
c1.getA(10)
c1.getB(20)
c1.getC(30)
c1.putA()
c1.putB()
c1.putC()
'''
#3) multiple inharitance
'''
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B():
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)


c1=C()
c1.getA(10)
c1.getB(20)
c1.getC(30)
c1.putA()
c1.putB()
c1.putC()
'''
#4) hierarchi inheritance which is not use mostely
'''
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)

class D(A):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D:",self.d)

b1=B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()


c1=C()
c1.getC(30)
c1.putC()

d1=D()
d1.getD(40)
d1.putD()

'''
#5) hybrid inheritance
'''
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D:",self.d)


d1=D()
d1.getA(10)
d1.getB(20)
d1.getC(30)
d1.getD(40)
d1.putA()
d1.putB()
d1.putC()
d1.putD()

'''
# example of polymorphism

#two types overiding which is also called run time and over loading which is also called compile time but over loading does not support in python so only one is valid over riding
# if we use same method prototype in base class and derived class  and if you call that method using the object of derived class then only derived class method will be called then it is overriding method and to solve it we use super method to solve overiding
# so you can say that method of derived class overrides the method of base class.
'''
class A:
    def show(self):
        print("show from A:")
class B(A):
    def show(self):
        print("show from B:")
class C(B):
    def show (self):
        print("show from C:")
c1=C()
c1.show()

'''
'''
class A:
    def show(self):
        print("show from A:")
class B(A):
    def show(self):
        super().show()
        print("show from B:")
class C(B):
    def show (self):
        super().show()
        print("show from C:")
c1=C()
c1.show()
'''

'''
class A:
    def show(self):
        print("show from A:")
class B(A):
    def show(self):
        super().show()
        print("show from B:")
class C(A):
    def show (self):
        super().show()
        print("show from C:")
class D(B,C):                         # in which we write super in d then it goes in b then we write super in b then according to our thought
    def show (self):                  #it goes in A but it goes in c because in d we pass two arguments class first B and then C so if we want
        super().show()                # to go in A then we should write super in class c then it goes in A class.
        print("show from D:")

d1=D()
d1.show()
'''
'''
str="allinpython"
print(str.find('e'))
'''
'''
l=[20,40,60]
l.append(80)
print(l.remove(20))
'''
'''
l=[1,2,3,4,5,6,7,8]
l1=[2*x for x in l]
print(l1)
'''
''''
val=5
def fun():
    val=15
    print(val, end=" ")
fun()
print(val)
'''
'''
my_list = ["Hello", "Python"]
print("-".join(my_list))
'''
'''
sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)
'''
'''
l = ['a', 'b', 'c', 'd']
l1=l.copy
print(l1)
'''
'''
aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])
print(aList[1][3])
'''
'''
l = [None] * 10
print(len(l))
'''
'''
sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

aList = [5, 10, 15, 25]
print(aList[::-2])

list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))

resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']
#newList = listOne.extend(listTwo)
#newList.extend(listOne, listTwo)
#newList = extend(listOne, listTwo)
newList = listOne + listTwo
print(newList)
'''
#new code operator overloading
'''
class point:
    def __init__(self):
        print("init called")
p1=point()

'''
'''
class point:
    def __init__(self,x,y):
        print("init called")
p1=point(10,20)
'''
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("init called")
p1=point(10,20)
'''
'''
class point:
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str called")
        return ""

p1=point(10,20)
print(p1)
'''
'''
class point:
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str called")
        #return "({0},{1})".format(self.x,self.y)
        #return "[{0},{1}]".format(self.x,self.y)
        return "{0},{1}".format(self.x,self.y)

p1=point(10,20)
print(p1)
'''
'''
class point:
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str called")
        #return "({0},{1})".format(self.x,self.y)
        #return "[{0},{1}]".format(self.x,self.y)
        return "{0},{1}".format(self.x,self.y)
    def __add__(self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return point(x,y)

p1=point(10,20)
print(p1)
p2=point(30,40)
print(p2)
print("addition :",p1+p2)
'''
******************
'''
print('x\96\x94')
'''
'''
def foo(k):
    k[0]=1
m=[0]
foo(m)
print(m)
'''


