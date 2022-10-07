# wap pattern
# for i in range(5):
#     for j in range(5):
#         if i+j==2 or j-i==2 or i-j==2 or i+j==6 :
#             print("*",end="")
#         else:
#             print("",end=" ")
#     print()

# def reverse(string):
#     reverse_string=""
#     for i in string:
#         reverse_string=i+reverse_string
#     print("the reverse string:",reverse_string)
# string=input("enter the string:")
# print("the enter the string",string)
# reverse(string)

# n=["12345"]
# k=[123,3234,223,234]
# n.extend(k)
# print(n)

# gcd
# def computGCD(a,b):
#     if b==0:
#         return a
#     else:
#         return computGCD(b,a%b)
# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# print(computGCD(num1,num2))
# wap balance braket using stack
# import math
# import random
# import re
# import random
# import sys
# def isbalance(s):
#     stack=[]
#     bracket={'[':']','{':'}','(':')'}
#     for char in s:
#         if char in ['[','{','(']:
#             stack.append(char)
#         else:
#             if stack:
#                 top=stack.pop()
#                 if bracket[top]!=char:
#                     return "no"
#             else:
#                 return "no"
#     return "no" if stack else "yes"
# s=input("enter hte ")
# isbalance(s)

# pattern question
# n=5
# for i in range(n):
#    for j in range(n):
#     if i+j==4 or i==4 or i==0:
#         print("*",end=" ")
#     else:
#         print(" ",end=" ")
#    print()

# write counting 
# def table(n):
#   num=0
#   for row in range(n):
#      for column in range(0,2):
#             num=num+1
#             print(num,end=" ")
#      print()
# n=int(input("enter the number :"))
# table(n)

# write series 3,10,29,66,128..
# n=int(input("Enter the number: "))
# i=1
# for i in range(1,n):
#   i=(i**3)+2
#   print(i,end=" ")

#  revers string
# n=[]
# lst=n[::-1]
# print(lst,end=" ")

#reverse string .2
# def string(word):
#   string_new=" "
#   for i in word:
#     string_new=i+" "+string_new
#   print(string_new)
# n=input("enter the :")
# word=n.split()
# string(word)
# n=input("enter the number :")
# num=len(n)
# for i in range(num):
#   for j in range(num-i):
#     num[j]=num-1
#     print(num,end="")
#   print()
  
