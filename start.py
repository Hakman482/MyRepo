#   # r = raw string
# #print('c:docs\nakeem')
# #print(r'c:docs\nakeeem')

# x= 8
# y = 9
# print(x + y)

# name = 'Hakeem'
# print(name[:-3])

# #STRINGS ARE IMMUTABLE
# #LISTS ARE MUTABLE
# #TUPLES ARE IMMUTABLE

# myName = 'Wat'+ name[3:]
# print(myName)

# nums = [5,20, 34,23,12]
# wows = ['hakman0', 45, 'titi', 24]

# print(nums + wows)
# print([nums, wows])
# nums.append(23) #add at the end of list
# nums.insert(1,80) #add based on index
# nums.remove(20) # remove via value
# nums.pop(3) # remove via index
# nums.pop() # remove last value  (pop and push in stacks)
# print(nums)

# del nums[3:] #removes more than one value
# nums.extend([15,42,56,68]) # add more than one value
# print(nums)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# nums.sort()
# print(nums)

# myTuple = (1,2,3,3,6,7,8,9,3)
# print(myTuple[4:])
# print(myTuple.index(6))
# print(myTuple.count(3))

# mySet = {23,45,76,12,34,29,23}
# #print(mySet)





# num = 3.45
# print(type(num))
# a = int(num)
# print(type(a))
# print(a)
# b= float(a)
# print(b)

# k = 6
# c= complex(k,b)
# print(c)


# print(b<k)
# print(type(b<k))

# print(int(True))
# print(int(False))


# print(list(range(10)))
# print(list(range(2,21,4))) #(start, end, difference)

# #DICTIONARIES
# d = {'Hakeem': 'Ice-cream', 'Issah':'Toffee', 'Maltiti':'Cake'}
# print(d.values())
# print(d.keys())
# print(d['Issah'])
# print(d.get('Issah'))


# print(set(range(10)))

# print(bin(0xf))
# print(oct(25))
# print(hex(123))


#BITWISE OPERATOR
#  ~ complement
#  & and
#  | or
# ^ xor
# << left shift
# >> right shift

# print(~12)
# print(25|12)
# print(12 & 13)
# print(12 ^ 13)
# print(10 << 2)
# print(10 >> 2)

#import math functions
#import math as m
# print(m.sqrt(25))
# print(int(math.sqrt(15)))
# print(math.ceil(5.45))
# print(m.floor(2.56))
# print(m.pow(3,2))
# print(m.pi)
# print(m.e)

# from math import pow,sqrt
# print(pow(4,5))

# x= int(input("Enter your number: "))
# y= int(input("Enter your number: "))

# z = x+y
# print("you have: ", z)


# ch = input("enter a char: ")[0]
# print(ch)

# wow = eval(input("enter the expression: "))
# print(wow)

# import sys as s   #enables input via command prompt
# x= int(s.argv[1])
# y= int(s.argv[2])
# z =x+y
# print(z)


#IF, ELSE, ELSEIF(elif), while, for STATEMENTS
# if False:
#     print("You're right")
# elif True:
#       print('Bye')
# else:
#     print("Whatever")

# x=0
# while x < 5:
#     print("Hakeem ", end="")
#     x += 1
    
    
# i=1
# while i<=5:
#     print("Hakman ",end="")
#     j=1
#     while j<=4:
#         print("Rocks ",end="")
#         j += 1
#     i += 1
#     print()

#for
# x=["hak", 45, 3.2]
# for i in x:
#     print(i)
    
# for i in range(20,10,-1):
#     if i%5 != 0:
#      print(i)



#Break = Coming out of a loop
# total = 5
# x= int(input("How many candies do you want?  "))

# i= 1

# while i<=x:
#     if i > total:
#         print("Out of stock")
#         break
#     print("Candy")
#     i+=1
  
#CONTINUE == skip values  
# for i in range(1,101):
#     if (i%2 != 0):            #if (i%3 == 0 or i%5 == 0):
#         continue               # or pass
#     print(i)
# print("Bye")

#PATTERNS
# for i in range(4):
#     for j in range(4):
#         print("#",end=" ")
#     print()
   
   
# for i in range(4):
#     for j in range(4-i):
#         print("#", end=" ")
#     print()




                #OBJECT-ORIENTED PROGRAMMING

# class Computer:
#     def __init__(self,cpu,ram):  #Automatically called
#         self.cpu = cpu
#         self.ram = ram
#        # print("Happy Birthday")
        
    
    
    
#     def config(self):
#        print("The specs are: ",self.cpu, self.ram)


# com1= Computer(54,45)
# com2 = Computer("AMD Ryzen", "32GB")

# com1.config()
# com2.config()

# #print(id(com1))



# class Student:
#     school = "KNUST"
    
#     def __init__(self,name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.lap = self.Laptop()
        
#     def show(self):
#         print(self.name, self.age, self.grade)
#         self.lap.show()
     
#     def avg(self):
#         print((self.age + self.grade)/2)
        
#     @classmethod   
#     def getSchool(cls):
#         return cls.school
    
#     @staticmethod
#     def moto():
#         print("The best school in Africa")
        
    
#     class Laptop:
#         def __init__(self):
#             self.cpu = "i5"
#             self.ram = "4GB"
#             self.colour = "Red"   
            
#         def show(self):
#             print(self.cpu, self.ram, self. colour)
       
       
       
       
       
        
# s1 = Student("Hakeem", 23, 9)
# s2 = Student("Titi", 34, 10)

# lap1 = Student.Laptop()
# lap1.show()
# s2.name = "Kofi"
# s2.show() 

# s2.avg() 
# print(s1.grade)
# print(Student.getSchool())



# class A:
#     def __init__(self):
#         print("A in init")
        
#     def feature1(self):
#         print("f1 is working")

#     def feature2(self):
#         print("f2 is working")
    
# class B:   
#     def __init__(self):
#         super().__init__()
#         print("B in init")
        
#     def feature3(self):
#         print("f3 is working")
#                                 #METHOD RESOLUTION ORDER (LEFT TO RIGHT)
#                                 #MULTILEVEL AND SINGLE LEVEL INHERITANCE
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("C in init")
        
#     def features4(self):
#         print("f4 is working")
        
# #a0 = A()       
# #a1 = B()
# a2 = C()
# a1.feature1()
# a2.feature1()
# a0.feature4()


        #DUCK TYPING

# class PyCharm:
#     def execute(self):
#         print("Running...")
#         print("Processing...")
        
# class VSCode:
#     def execute(self):
#         print("Hurraayyyy")
#         print("Running...")
#         print("Processing...")
        
# class Laptop:
#     def code(self, ide):
#         ide.execute()
        
# ide = PyCharm()
# lap1 = Laptop()

# lap1.code(ide)


        #OPERATOR OVERLOADING  defining opereations in classes since they are not originally
        #applied in classes
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
        
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1, m2)
        
#         return s3
    
#     def __gt__(self, other):
#         s1 = self.m1 + self.m2
#         s2 = other.m1 + other.m2
#         if s1 > s2:
#             return True
#         else:
#             return False
    
#     def __str__(self):
#         return "{} {} ".format(self.m1, self.m2)
#         #return self.m1 + self.m2
# s1 = Student(50, 34)
# s2 = Student(23,57)

# s3 = s1 + s2
# print(s3)
# print(s1)

# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")






        #METHOD OVERLOADING two methods with same name but
        # different number of arguments 
# class Student:       
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
        
#     def sum(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             s = a + b + c
#         elif a!= None and b!=None:
#             s = a + b
#         else:
#             s = a

#         return s


# s1 = Student(23,34)

# print(s1.sum(2,4))

        #METHOD OVERRIDING two classes with same methods and parameters

# class A:
#     def show(self):
#         print("A in show")
        
# class B(A):
#     def show(self):
#         print("B in show")
        
        
        
# a1 = B()
# a1.show()


#Logical Error(wrong output), Runtime Error(divide by zero), Syntax Error(misspelling)
# a = 4
# b = 0
# try:
#         print(a/b)
#         k = int(input("Enter your number"))
#         print(k)

# except ZeroDivisionError as e:
#         print("Can't be done", e)

# except ValueError as e:
#         print("Not an integer")
        
# except Exception as e:                  #Error you don't know about
#         print("Something went wrong")
       
# finally:
#         print("case Closed")  #Would be executed with or without error





                #MULTITHREADING
#                 #THere arae three threads: t1, t2, and main thread
# from threading import *
# from time import sleep


# class Hello(Thread):
#         def run(self):
#           for i in range(5):
#                 print("Hello")
#                 sleep(1)
                
# class Hi(Thread):
#         def run(self):
#                 for i in range(5):
#                         print("Hi")
#                         sleep(1)
                        
# t1 = Hello()
# t2 = Hi()

# t1.start()                     #start used to call thread methods
# sleep(0.2)
# t2.start()

# t1.join()               #join enables executiion of t1 and t2 before main thread
# t2.join()

# print("Bye!")   #Handled in main thread
             
             
             
             
                #FILE HANDLING
                #w= write, r=read, a= append

# f = open("Myself.txt", "r")
# #print(f.read())

# f1 = open("Mine.txt", "w")
# f1.write("I'll always be with you ")

# #Copying data
# for data in f:
#         f1.write(data)

# #Copying image
# f = open("RAIL.jpg","rb")
# ##print(f.read())

# f1 = open("MyPic.jpg", "wb")

# for pixel in f:
#         f1.write(pixel)
        
        

        #LINEAR SEARCH
# pos = -1
# def search(myList, n):
#         for i in range(0,len(myList)):
#                 if myList[i] == n:
#                         globals()["pos"] = i
#                         return True
                
#         return False

# myList = [3,6,4,8,6,5,7,9]
# n= int(input("What's the number?: "))

# if search(myList, n):
#         print("Found at index ", pos)
# else:
#         print("Not Found")



                #BINARY SEARCH(ALL VALUES HAVE TO BE SORTED)
# pos = -1 

# def search(list, n):
#         low = 0
#         high = len(list) - 1
        
                
#         while low <= high:
#                 mid = (low + high)//2
#                 if list[mid] == n:
#                         globals()['pos'] = mid
#                         return True
#                 elif list[mid] > n:
#                         high = mid-1
#                 else:
#                         low = mid+1
#         return False
                 


# list = [4,6,10,16,23,45]
# n=44

# if search(list, n):
#         print("Found at index: ", pos)
# else:
#         print("Not Found")




                        #BUBBLE SORT
# def sort(list):
#      for i in range(len(list)-1,0,-1):
#         for j in range(i):
#              if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
                                                        
                        
                        
# list = [2,5,1,6,7,9,0]

# sort(list)
# print(list)


                #SELECTION SORT

# def sort(list):
#         for i in range(len(list)-1):
#              minpos = i
#              for j in range(i,len(list)):
#                      if list[j] < list[minpos]:
#                              minpos = j
                             
#              temp = list[i]
#              list[i] = list[minpos]
#              list[minpos] = temp



                                                        
                        
                        
# list = [2,5,1,6,7,9,0]
# print(len(list))

# sort(list)
# print(list)      
                
                
                
                
                
                
                        #MYSQL
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="hak@kata1652", database = "Hakeem")


mycursor = mydb.cursor()

mycursor.execute("select * from Hobbies")

### result = mycursor.fetchall()  #fetchone alt: store values in variable

for i in mycursor:
        print(i)