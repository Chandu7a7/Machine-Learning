# print("hello")


#----------------input for user name and print it----------

# Name = input("What is your name? ")
# print("Hello " + Name)


#------------------Type conversion---------------------
# str()
# float()
# int()
# bool()
# old = input("What is your age? ")
# newage= int(old)+2
# print("Your age after 2 years will be " + str(newage))

# number = 20
# print(float(number))

#------------- sum calculator----------- 

# first = input("Enter the first number :")
# second = input ("Enter the second number :")
# sum = int(first) + int(second)
# print(sum)


#-----------------String----------------

# name ="Hello World"
# print(name.find('W'))
# print(name.replace('World','Universe'))
# print(name)


#-----------------Arithmetic operater----------------

# print(10/3)

# print(2+3)
# print(2-3)
# print(2*3)
# print(2/3)
# print(5%2)
# print(5**2)

#-----------------comperioson operater----------------

# print(5 > 3)

# print( 3 != 3)
 
#---------------- Logical operater 

# print (5>3 and 3>2)
# print (5>3 or 3>2)

#-----------------if else statement----------------

# if 5>3:
#     print("5 is greater than 3")

# if 3>5:
#     print("3 is greater than 5")
# else:
#     print("5 is greater than 3")

#-------------------loops-------------------

# i=1
# while i<=5:
#     print(i)
#     i=i+1

# i= 1
# while i <=5:
#     print(i * "*")
#     i=i+1


# for i in range(5):
#     print(i)


# ------------------list [ ] --------------------

# marks = [98 , 44 , 45 ,55]
# print(marks[2])    #print 3rd element
# print(marks[0:2])



# marks = [98 , 44 , 45 ,55]
# marks.append(99)
# print(marks)
# print(99 in marks)

#--------------------- Touple ( )  immutable  -----------------

# marks = (95 , 98 , 97 , 96 )
# print(marks.count(95))


#--------------------- set { } -----------------

# marks={ 95 , 98 , 97 , 96 }
# print(marks)

#--------------------- Dictionary { key : value } -----------------

# marks = { "Maths" : 95 , "Science" : 98 , "English" : 97 , "History" : 96 }
# print(marks["Maths"])


#--------------------- Function -----------------


# from math import *
# print(sqrt(36))

def print_sum(first, second):
    print(first + second)


print_sum(2,3)