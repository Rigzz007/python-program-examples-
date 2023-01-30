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

#complete star from 1 to 5 from left to right
#n= 5
#i=0
#n=int(input("enter the number"))
#for i in range(0,n):
#  for j in range(0, i+1):
#     print("*", end="")
#  print()

#complete start from 1 to 5 from right to left
#n=5
#k=n-1
#for i in range(n):
#   for j in range(k):
#    print(" ",end="")
#   k=k-1
#   for j in range(i+1):
#    print("*", end="")
#   print()


#complete start from 1 to 5 from right to left
#n=5
#for i in range(n):
#    for j in range(n-i-1):
#        print(" ",end="")
#    for j in range(i+1):
#        print("*",end="")          #print("*",end=" ")
#    print()


#complete  start from 5 to 1 left to right
#n=5
#for i in range(n):
#    for j in range(i,n):            #for j in range(n-i):
#        print("*",end="")
#    print()


#complete with space between star from 1 to 5 right to left
#n=5
#k = 2 * n - 2
#for i in range(0, n):
#    for j in range(0, k):
#        print(end=" ")
#    k = k - 2                       # decrement k value after each iteration
#    for j in range(0, i + 1):
#        print("* ", end="")         # printing star
#    print("")


#complet start from 5 to 1 left to right
#n=5
#for i in range(n):
#   for j in range(i):
#     print(" ",end="")
#    for j in range(n-i):
#     print("*",end="")          #print("*",end="")
#    print()

#complete starr from christmus tree top to down
#n=10
#m=(2*n)-2
#for i in range(n):
#    for j in range(0,m):
#        print(" ",end="")
#    m=m-1
#    for j in range(0,i+1):
#        print("*",end=" ")
#    print("")                #print()

n=10
m=(2*n)-2
for i in range(n,-1,-1):
    for j in range(m,0,-1):
        print(" ",end="")
    m=m+1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")                   #print()




#complete
#s=input("input string:")
#ch=0
#w=1
#sp=0
#n=0
#special=0
#for i in s:
#    if i.isalpha():
#        ch=ch+1
#    elif i.isspace():
#       sp=sp+1
#       w=w+1
#    elif i.isnumeric():
#        n=n+1
#    else:
#      special=special+1

#print("total special:",special)
#print("total character:",ch)
#print("total word:",w)
#print("total space:",sp)
#print("total number:",n)

#complete
#s="1233"
#if s.isalpha():
#    print("this is string")
#else:
#    print("this is not string")


#slicing complete
#  01234567890123456
#s="Tops Technologies"
#  76543210987654321

#print(s[3:13])
#print(s[:15])
#print(s[2:])
#print(s[3:15:3])
#print(s[::5])
#print(s[-14:-2])
#print(s[-5])
#print(s[-17:])
#print(s[-15:-1:4])
#print(s[::3])
#print(s[::-3])