# # wap to take input for user check armstrong or not
# i=int(input("enter the number"))
# num=i
# result=0
# n=len(str(i))
# while(i!=0):
#     digit=i%10
#     result=result+digit**n
#     i=i//10
# if num==result:
#     print("The number is armstrong number")
# else:
#     print("the number is not armstronge number")

# wap patterm hollow tringle
# n=30
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==i or i==n or j==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
        
#     print()

# wap using fatorial function program
# import math
# num=int(input("enter the number: "))
# result=math.factorial(num)
# print("enter the no",num,"is fatorial",result)

# using recursion
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter the number"))
# result=fact(n)
# print(result)

# loop
# n=5
# result=1
# for i in range(n,0,-1):
#     result=result*i
# print(result)

# hollow tringal next shape
# n=5
# for i in range(1,n):
#     for j in range(1,n):
#         if i==1 or i==j or j==4:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# wap patter floy's triangle
# n=int(input("enter the number"))
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end="")
#         num=num+1
#     print()

# wap string pattern program
# n="python"
# num=len(n)
# for i in range( 0, num):
#     for j in range(i+1):
#         print(n[j],end="")
#     print()

# wap fibonacci series program
# from tkinter import Y
# n=int(input("enter the number to show fiboncci serie: "))
# x=0
# y=1
# z=0
# for i in range(0,n):
#     print(z)
#     x=y
#     y=z
#     z=x+y

# wap right tringle opp. pattern prg.
# n=5
# for i in range (n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 2
# n=5
# num=0
# for i in range (n,0,-1):
#     for j in range(1,i+1):
#         num=num+1
#         print(num,end=" ")
#     print()

# wap check whether is  prime number or not
# n=int(input("enter the number: "))
# if n>1:
#     for i in range(2,n):
#         if (n%i)==0:
#             print("it is not prime number")
#             break
#     else:
#             print("it is prime number")
# else:
#     print("it is not prime")
    
# wap for hollow equilateral triangle 
# for i in range(1,5):
#     for j in range(1,8):
#         if i==4 or i+j==5 or j-i==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# wap for perfect number
# n=int(input("enter the number "))
# result=0
# for i in range(1,n):
#     if n%i==0:
#         result=result+i
# if result==n:
#         print("the number is perfect number")
# else:
#         print("the number is not perfect number")

# n=5
# for i in range(1,n):
#     for j in range(1,n):
#         if i==1 or i==j or j==4:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# wap patter right triangel
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# wap of counting
# n=int(input("enter the number"))
# num=0
# for i in range(0,10):
#     for j in range(0,10):
#         num=num+1
#         print(num,end=" ")
#     print()

# wap for pyramit
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,2+i-1):
#         print("*",end=" ")
#     print()

# wap pattern
# for i in range(5):
#     for j in range(5):
#         if i+j==2 or j-i==2 or i-j==2 or i+j==6 :
#             print("*",end="")
#         else:
#             print("",end=" ")
#     print()

# Wap to reverse string
# def reverse(string):
#     reverse_string=""
#     for i in string:
#         reverse_string=i+reverse_string
#     print("the reverse string:",reverse_string)
# string=input("enter the string:")
# print("the enter the string",string)
# reverse(string)

# gcd
# def computGCD(a,b):
#     if b==0:
#         return a
#     else:
#         return computGCD(b,a%b)
# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# print(computGCD(num1,num2))
# from turtle import position

# wap for caesar cipher
# num=input("enter the string:")
# lst="abcdefghijklmnopqrstuvwxyz"
# key=5
# ency=""
# for i in num:
#     position=lst.find(i)
#     new_position=(position+5)%26
#     ency+=lst[new_position]
# print(ency)

# num=int(input("enter the number"))
# for i in range(1,num+1):
#     for j in range(1,num-i+1):
#         print(end=" ")
#     for j in range(i,0,-1):
#         print(j,end="")
#     for j in range(2,i+1):
#         print(j,end="")
#     print()

# def current(string):
#     output=""
#     for i  in string:
#         if i not in output:
#             output=output+i
#     print(output)
# string=input("enter the string:")
# current(string)
# class employee():
#     def __init__(self,id,name,salary):
#          self.e_id=id
#          self.s_name=name
#          self.s_salary=salary
#     def info(self):
#         print( self.e_id,self.s_name,self.s_salary)
# per=employee(5,"ankit",1000)
# per.info()