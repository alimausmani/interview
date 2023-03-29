# a="Shalini"
# b="94"
# c="Madhu"
# d="2.04"
# print(a+b+c+d)

# birth_year=int(input("enter the birth_year:"))
# current_year=int(input("enter the current_year:"))
# if birth_year-current_year:
#     print(current_year-birth_year)
# elif birth_year<current_year:    
#      print("age") 
# else:
#     print("nothing")

  

# num1=int(input("enter the number:"))
# if num1>=20 and num1<=50:
#     print("Hello")
# elif num1>=10 and num1<=20:
#     print("Puzz")
# else:
#     print("Buzz")    


# a="Alima Usmani"
# print(a)

# a=[1,2,3,4,5,[7,6,8,9]]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         len(a[i])
#         if len(a)< len(a[i]):
#             print(a)
#         else:
#             print(a[i])
#     i+=1            

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# c=1
# i=0
# while i<len(a):
#     j=[a[i],a[c]]
#     b.append(j)
#     c+=2
#     i+=2
# print(b)   

# a=[["g","f","g"],"i","j"]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j],end=" ")
#         j+=1
#     i+=1  
# print()  

# a=[10,20,30,[40,50,60,70,80]]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         len(a[i])
#         if len(a)>len(a[i]):
#            print(a)
#         else:
#             print(a[i]) 
#     i+=1          


# a={"one":1,"two":2}
# key=input("enter the key:-")
# if key not in a:
#     value=input("enter the value:- ")
#     a.update({key:value})
# else:
#     a.pop(key)
# print(a)


# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number:"))
# num4=int(input("enter the number:"))
# if num1>num2 or num1>num3 or num1>num4:
#     print(num1,"it is a greater number")
# elif num2>num1 or num2>num3 or num2>num4:
#     print(num2,"it is greater number")
# elif num3>num1 or num3>num2 or num3>num4:
#     print(num3,"it is a greater number")
# elif num4>num1 or num4>num2 or num4>num3:
#        print(num4,"it is not a greater number") 
# else:
#     print("nothing")                  

# i=0
# while i<=10:
#     print(i)
#     i+=1    

# i=0
# while i<=10:
#     i+=1
#     print(i)

# i=0
# while i<5:
#     print(i)
# i+=1

# i=0
# while i<5:
#     print(i)
#     i+=1    

# i=0
# while i<=10:
#     i+=1
#     print(i)


# n=int(input("enter the number:"))
# row=0
# i=0
# while i<5:
#     j=0
#     while j<3:
#         space=space-row
#         print("",end="")
#         j+=1
# i+=1
# print("*",end="")
# print()        


# output=[7,14,29,12,11]

# i=0
# while i<=5:
#     j=0
#     while j<=i:
#         print(" ",end="")
#         j+=1
#     k=0
#     while k<=j:
#         print(j,end="")
#         k+=1
#     i+=1  
#     print()    

# def prime_number(num):
#     num=int(input("enter the number:"))
#     i=2
#     f=0
#     while i<=100:
#         if num%i==0:
#             print(i)
#             f+=2
#         i+=1
#     if f==0:
#         print("it is a prime numbe:")
#     else:
#         print("it is not a prime number:") 
# prime_number(2)                   

# i=0
# while i<=10:
#     if i%2==0:
#         print("even number",i)  
#     # else:
#     #     print("odd")      
#     i+=1        

# my_file=open("people.txt1","r")
# my_file.write("my name is alima")
# # my_file.write("my age is 16")
# # data=my_file("people.txt")
# my_file.close()


# my_file=open("people.txt1","r+")
# a=my_file.readlines()
# print(a)
# my_file.close()


# a=[25,257,8876,85,65]
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     while a[i]>0:
#       sum=sum+(a[i]%10) 
#       a[i]//=10 
#     b.append(sum)
#     i+=1
# print(b)      

# birth nikalna

# year=int(input("enter the year:"))
# if year>0 : 
#     month=int(input("enter the month:"))
#     if month>=1 and month<=12:
#         day=int(input("enter the day:"))
#         if day >=1 and day<=31:
#             print(day,"-",month,"-",year)
#             print("it is your date of birth")
#         else:
#             print("wrong day")
#     else:
#         print("wrong month")
# else:
    # print("wrong year")


# num=input("enter the number:")
# i=0
# while i<len(num):
#     if num[i]==str(1):
#         print("one",end=" ")
#     elif num[i]==str(2):
#         print("two",end=" ")
#     elif num[i]==str(3):
#        print("three",end=" ")

# dict={0:14,1:100}
# total=0
# for i in dict.values():
#        total=total+i
# print(total)    

# dict={0:14,1:100}
# sum=0
# for i in dict.values():
#     sum=sum+i
# print(sum)    

# dict={0:14,1:100}
# print(sum(dict.values()))

# from turtle import update


# dict1={1:100,2:200,3:300}
# dict2={4:400,1:500,2:600}
# dict3={}
# dict4 = {}        
# for i in dict1:
#     for j in dict2:
#         if i == j :
#             dict3[i] = dict1[i]+dict2[j]
#         elif i not in dict2 and j not in dict1:
#             dict4[i] = dict1[i]
#             dict4[j] = dict2[j]
# print("",dict3 ,"\n",dict4)
        

# dict2={4:400,1:500,2:600}
# max=0
# max1 = 0
# for i in dict2:
#     if dict2[i]>max:
#        max=dict2[i]
# for i in dict2:
#     if dict2[i]>max1 and max!= dict2[i]:
#         max1= dict2[i]
# print(max1)      


# dict2={4:400,1:500,2:600}
# max=max(dict2.values())
# max2=0
# for i in dict2.values():
#     if (i>max2 and i<max):
#         max2=i
# print(max2)        
  

# creating a new dictionary
#  print the second largest value
# new_dict ={"google":12, "amazon":9, "flipkart":4, "gfg":13}
# max = max(new_dict.values())
# max2 = 0
# for v in new_dict.values():
#      if(v>max2 and v<max):
#             max2 = v
# print(max2)            
 

  

# revers number

# num=int(input("enter the number:"))
# rev=0
# while num>0:
#     rev=num%10
#     num=num//10
#     print(rev,end="")

# perfect number

# a=int(input("enter the number:"))
# i=1
# sum=0
# while i<a:
#     if a%i==0:
#         sum+=1
#     i+=1
# print(sum)
# if a==sum:
#     print("it is a perfect number")
# else:
#     print("it is not a perfect number")        
  
# prime number

# num=int(input("enter the number:"))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("it is a prime number:") 
# else:
#     print("it is not a prime number")           


# yes no question
# num=int(input("enter the number:"))
# if num>=100:
#     print("yes")
# else:
#     print("no")    

# last digit number
# num=int(input("enter the number:"))
# b=num%10
# if b%10:
#     print(b,"last digit number")
# else:
#     print("wrong")    


# age 
# current_year=int(input("enter the current year:"))
# birth_year=int(input("enter the birth year:"))
# if current_year>0:
#     print("it is your age",current_year-birth_year)
# else:
#     print("Wrong age")    


# num=int(input("enter the number"))
# i=1
# sum=0
# while num<=i:
#       sum=sum+0


# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.      
            
# key=["alima","dimple","aayushi","anjali","ankita","deepu"]
# value={}
# for i in key:
#     value[i] = len(i)
# print(value)
            
# list1=[[1,2,3],4,5,6,[7,8,9]]
# b=[]
# for ele in list1:
#     if type(ele) == list:
#         for i in ele :
#             b.append(i)
#     else:
#         b.append(ele)
# print(b)

# list1=[1,2,3,4,5,6,7]
# i=0
# while i<len(list1):
#     i+=1
# print([i])   

# list1=[1,2,5,10,12,13,16,20]

# list1=[1,5,10,12,16,20]
# list2=[1,2,10,13,16]
# for i in list2:
#     if i not in list1 :
#         list1.append(i) 
# list1.sort() 
# print(list1)  


# list1=[1,5,10,12,16,20]
# list2=[1,2,10,13,16]
# list1.sort()
# print(list1)

# a=["44aa","34bb","65cc","04dd"]
# b=[]
# i=0
# while i<len(a):
#     if a[i]==int:
#         b.append(a[i])
#     i+=1
# print(b)        

# output=[[3,2][4,6][0,10][13,9]]

# list1=[2,3,4,6,0,10,13,9]
# b=[]
# j=0
# i = 0
# j = 1
# while j < len(list1):
#     if list1 not in b:
#         a = [list1[i],list1[j]]
#         b.append(a)
#     i+=2
#     j+=2
# print(b)   

# list1=[2,3,4,6,0,10,13,9]
# b=[]
# j=0
# for i in range(1,len(list1),2):
#     if list1 not in b:
#         a=[list1[i],list1[j]]
#         b.append(a)
#     j+=2
# print(b)  

# i = 1
# while i <= 10 :
#     print(1*i,2*i,3*i,4*i,5*i,6*i,7*i,8*i,9*i,10*i)
#     i+=1      


# i=1
# sum=0
# while i<=5:
#     num=input("enter the number:")
#     sum=sum+int(num)
#     print(sum) 
#     i+=1
 
# sum=0
# for i in range(5):
#     num=input("enter the number:")
#     sum=sum+int(num)
# print(sum) 

#  https://docs.google.com/spreadsheets/d/1Z81-Hdl0HFEAtrBKOxuRez0ofYusi2L9CQ1QSouTKwI/edit?pli=1#gid=535849058  


# s=[12345678]
# i=0
# while i<len(s):
#     i+=1
# print(i)    

# a=[5,6,7,7,6,5,3,2,2,1,1,1,1,1]
# b=[]
# i=0
# while i<len(a):
#     if a.count(a[i])>=2:
#         pass
#     else:
#         b.append(a[i])
#     i+=1
# print(b)        

# a=[5,6,7,7,6,5,3,2,2,1,1,1,1,1]
# b=[]
# i=0
# while i<len(a):
#     if a.count(a[i])==1:
#         b.append(a[i])
#     i+=1
# print(b)        

# list1=["anjali","alima","aayushi","dimple","ankita","deepu"]
# d={}
# for i in  list1:
#     d[i]=len(i)
# print(d)    

# a=[110,100,1900,1200,1300]
# i=0
# b=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             b.append(a[i])
#             break
#         a[i]=a[i]//10
#     i+=1
# print(b)        


# name=["teena","alima","dimple","lina"]
# i=0
# while i<len(name):
#     c=0
#     if len(name[i]):
#         c+=1
#     i+=1
# print(c)   
# name=["teena","alima","dimple","lina"]   
# animal=["dog","camel","goat","cat"]
# age=["1","2","3","4"]
# i=0
# b=[]
# while i<len(name):
#     c=name[i]+"the",animal[i]+"is",age[i]
#     b.append(c)
# i+=1
# print(b)    

# a=[5,6,7,7,6,5,3,2,2,1,1,1,1,1]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==3:
#         b.append(a[i])
#     i+=1
# print(b)        

# list1=[1,2,4,5,6,8,[2,3,4,5,7]]
# sum=0
# i=0
# while i<len(list1):
#     if type(list1[i])==list:
#         j=0
#         while j<len(list1[i]):
#             sum=sum+list1[i][j]
#             j+=1
#         i=i+1
# print(sum)

# list1=[1,[1,2,3],2,[4,6,7],3,[7,8,9]]
# i=0
# sum=0
# while i<len(list1):
#     j=list1[i]
#     if type(j) is list:
#         for b in range(len(j)):
#             sum=sum+j[b]
#             b+=1
#     else:
#         sum=sum+list1[i]
#     i=i+1
# print(sum)

# a=["a,l,i,m,a"]
# i=0
# while i<len(a):
#     i+=1
# print(i)


# a={"one":1,"Two":2,"Three":3}
# key=input("enter the key:")
# if key not in a:
#     value=input("enter the value:")
#     a.update({key:value})
# else:
#     a.pop(key) 
# print(a)       

# a=[["g","f","h"],"i","j"]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j],end="")
#         j+=1
#     i+=1    
# print()

# output=[10,30,45,55]

# l=[10,23,30,33,45,55,23,41]
# b=[]
# i=0
# while i<len(l):
#     if (l[i])%5==0:
#         b.append(l[i]) 
#     i+=1 
# print(b)       




# nums=[1,2,3,4,5,6]
# i=0
# sum=0
# b=[]
# while i<len(nums):
#     sum=sum+nums[i]
#     b.append(sum)
#     i+=1
# print(b)

'''
nums=[1,2,3,4,5,6]
i=0
sum=0
b=[]
while i<len(nums):
    sum=sum+nums[i]
    b.append(sum)
    i+=1
print(sum)'''


# i=4
# while i>0:
#     print(i*"*")
#     i-=1

# a=["Aayushi","Alima","Dimple","AayushiAlimaDimple"]
# i=0
# for i in a:
#     print(i,len(i))

# n=int(input("enter the number:"))
# i=0
# sum=0
# b=[]
# while i<(n):
#     a=int(input("enter the number:"))
#     b.append(a)
#     sum+=b[i]
#     i+=1
# print(b,sum)   

# name=["alima","aayushi","dimple"]
# animal=["cat","goat","dog"]
# age=["1","2","3"]
# i=0
# while i<len(name and animal and age):
#     print(name[i],"the",animal[i],"is",age[i])
#     i+=1       

# '''a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     i+=1
#     b.append([sum])
# print(b)  '''     


# a=["alima","dimple","anjali","ankitava"]
# i=0
# while i<len(a):
#     d=a[i]=len(a[i])
#     i+=1
# print(d)    

# l=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7]
# b=[]
# i=0
# while i<len(l):
#     if l[i] not in b:
#         b.append(l[i])
#     i+=1    
# print(b)        

# l=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7]
# b=[]
# for i in l:
#     if i not in b:
#         b.append(i)
# print(b)        


# n=int(input("enter the number:"))
# l=[]
# sum=0
# for i in range(n):
#     lose=input("enter the duplicates value:")
#     l.append(lose)
# print("my list",l)    


# output=[10,8,8,8,7,4,4,4,4,4]
# l=[4,10,1,2,8,7,3,0,1,4]
# i=0
# max=0
# b=[]
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#         b.append(l[i])
#         print(b)   

#     i+=1
# print(b)   

# output=[25,101,26,37]
# num=[12,10,5,6]
# nu=[101,110,1011,110]
# output=[11,11,111,11]


#  10 number me se maximum number
# '''i=0
# max=0
# b=[]
# while i<10:
#     n=int(input("enter the number:"))
#     b.append(n)
#     while i<len(b):
#         if b[i]>max:
#             max=b[i]
#         i+=1
# print(b)
# print(max) '''   


# a = [10, 20] 
# b = a 
# b += [30, 40] 
# print(a) 

# x = 6 
# y = 2 
# print(x ** y) 

# x = 6 
# y = 2 
# print(x ** y) 
# print(x // y) 

# print(36/4)

# x = 10 
# y = 50 
# if (x ** 2 > 100 and y < 100): 
#    print(x,y) 



# # print(10 - 4 * 2)

# y=10 
# x=y+=2
# print(x) 
# alist=[4,8,12,16]
# alist[1:4]=[20,24,28]
# print(alist)
# a = 4 
# b = 11 
# print(a | b) 
# print(a >> 2) 

# x=5+'my' 
# print(x)

# x='my'
# y='name'
# print(y+y)

# a="alima"
# a="usmani"

# from hashlib import algorithms_available


# output=alima
#         usmani


# for I in range(2,40):
#     print(I)

# a=2
# def add():
#     b=3
#     print(a+b)
# add()


# char_list=["a","n","j","a","l","i","d","i","v","y","a"]
# i=0
# l=[]
# while i<len(char_list):
#     j=0
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count+=1
#         j+=1
#     if char_list[i] in l:
#         i+=1
#         continue
#     l.append(char_list[i])
#     print(char_list[i],"-",count,"times ")


# n=int(input("enter:"))
# for i in range(n):
#     print('  '(n-i-1)+"   "*(i+1))
# for i in range(n-1):
#     print('  '(i+1)+"   "*(n-i-1))


# zero remove

# def remove0(a):
#     i=0
#     b=[]
#     while i<len(a):
#         while a[i]>0:
#             if a[i]%10!=0:
#                 b.append(a[i])
#                 break
#             a[i]//=10
#         i+=1
#     print(b)
# remove0([100,400,300])

# x="welcom to my blog"
# j="i"
# for j in x:
#     print(j)
# for i in  range(0,2,-1):
#     print("hello")

# for i in range(5):
#     for j in range(5):
#         print("As"*i,"\n")



# a=["44aa","34bb","65cc","04dd"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=""
#     while j<len(a[i]):
#         if a[i][j].isdigit():
#             sum+=a[i][j]
#         j+=1
#     b.append(sum)  
#     i+=1
# print(b)           

# def f(s,a):
#     count=0
#     b=""
#     for i in range(len(s)):
#         # if s[i]==" ":
#         if count==3:
#             # print(b)
#             b=""
#             count=0
#         else:
#             count+=1
#             b+=s[i]
#     # print(count)
# f("meena na maaa s",80)


# a=[1450,9600000,300]
# i=0
# b=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             b.append(a[i])
#             break
#         a[i]//=10
#     i+=1
# print(b)

# a=30 or 40+3**2//5+(3+False)
# print(a)

# a=9//5
# print(a)

# a=30 or 40
# print(a)
# a=3**2
# print(a)

# a=20
# b=10
# if a<b:
#     print(a)
# if a>b:
#     print(a)
#     if a>b:
#         print(a)
#         if a>b:
#             print(a)
#     if a<b:
#         print(a)
#     if a>b:
#         print(a)
#         if a>b:
#             print(a)
#     else:
#         print("ok") 
# else:
#     print("no")             


# a=[[2,3,4],[5,6,7],[8,9,2]]
# j=0
# for i in a:
#     print(i[j])
#     j+=1

# c=[]
# p=[]
# d=[]
# i=0
# while i<len(a):
#     c.append(a[i][0])
#     i=i+1
# print(c)
# j=0
# while j<len(a[i]):
#     p.appen(a[i][1])
#     j=j+1
# print(p)


# l=[[2,4,5],[3,6,9],[1,7,8]]
# # [[2,3,1],[4,6,7],[5,9,8]]
# for i in range( len(l)):
#     a=[]
#     for j in range(len(l[i])):
#         a.append(l[j][i])
#     print(a,end="")


# num=int(input("enter the number :- "))
# count1=0
# a=1
# while a<=1000:
#     i=1
#     count=0
#     while i<=a:
#         if a%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         count1+=1
#         print(count1,a)
#     if count1==num:
#         break
#     a=a+1

# a={"apple":100,"banana":200,"grapes":300,"kivi":400}
# b={"apple":100,"2":200,"3":300,"kivi":400}
# dict={}
# for i in a:
#     if i in b:
#         dict[i]= a[i]+b[i]
#     if i not in b:
#         dict[i]=a[i]
#     for j in b:
#         if j in a:
#             dict[j]=a[j]+b[j]
#         if j not in a:
#             dict[j]=b[j]
# print(dict)
# print(a[j])

# a=5
# b=2
# print(a/b)


# def get():
#     global a
#     a=input("enter the number:")
#     return a
# get()    

# def take():
#     if a=="10":
#         print(a)
# take() 

# var=[[4,5,6],8[7,8,9],7[5,8,9],4[7,6,9]]


# li=[4,5,6],[5,6,8],[9,10,11]
# sum=0
# i=0
# while i<len(li):
#     if i==0:
#         for j in li[i]:
#             sum+=j
#     elif i!=0:
#         s=len(li[i])
#         sum+=(li[i][s-1])
#     i+=1
# print(sum)                

# li=[4,5,6],[5,6,8],[9,10,11]
# i=0
# sum=0
# while i<len(li):
#     j=0
#     while j<len(li[i]):
#         if i==0:
#            sum+=li[i][j]
#         if (len(li[i])-1)==j and i!=0:
#             sum+=li[i][j]   
#         j+=1    
#     i+=1  
# print(sum)      



# a=[1,2,3,4,5,6,7,1,2,35,5]
# i=0
# while i<len(a):
#     i+=1
# print(i)    

# li = [1,2,3,'a','b','c']
# print(li[:3])
# print(li[3:])

# print(li[::3])

# a=[1,2,3,4,5,6,7,8,9,10]
# print(a[4])
# print(a[4])

# Lst = [50, 70, 30, 20, 90, 10, 50]
# print(Lst[1:5])

# list2=['yes','no','ok','thik','bye']
# i=0
# while i<len(list2):
#     i+=1
# print(i) 

# list2=['yes','no','ok','thik','bye']
# print(len(list2))

# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

# L1=[2,3,7]
# L2=[4,5,8]
# i=1
# s=""
# d=""
# while i<len(L1)+1:
#     s+=str(L1[-i])
#     d+=str(L2[-i])
#     i+=1
# b=(int(s)+int(d))
# e=""
# c=str(b)
# print(c)
# for i in range(1,len(c)+1):
#     e+=c[-i]
# print(e)


# s="welcome to my blog"
# print(s[-2:1])
# print(s[-10:-2:2])   


# unit=5
# no_of_rate=int(input("enter the no_of_rate:"))
# no_of_houses=int(input("enter the no_of_houses number:"))
# i=0
# unit_list=[]
# while i<(no_of_houses):
#     no_of_units=int(input("enter the no_of_units:"))
#     unit_list.append(no_of_units)
#     i+=1 
# print(unit_list)   
# b=no_of_rate*unit
# print(b)
# sum=0
# count=0
# for i in range(0,len(unit_list)):
#     sum=sum+unit_list[i]
#     count+=1
# print("Sum of all elements in given list: ",sum,"number of houses",count)   
# i=0
# while i<len(unit_list):
#     if sum>=b:
#         print("sufficent")
#         break
#     else:
#         print("not sufficent")
#         break
#     i+=1



'''l=[1,1,1,1,2,2,2,3,4,4,5,5,5]
i=0
b=[]
while i<len(l):
    if l[i]==3:
        b.append(l[i])
    i+=1
print(b)   '''


'''
a=[1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,7,8]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)    ''' 


# a=[14500,9600,300]
# i=0
# b=[]
# while i<len(a):
#         if a[i]!=0:
#             b.append(a[i])
#         i+=1
# print(b)           



# unit=int(input("enter the unit:"))
# no_of_rate=int(input("enter the no_of_rate:"))
# no_of_houses=int(input("enter the no_of_houses number:"))
# i=0
# unit_list=[]
# while i<(no_of_houses):
#     no_of_units=int(input("enter the no_of_units:"))
#     unit_list.append(no_of_units)
#     i+=1 
# print(unit_list)   
# b=no_of_rate*unit
# print(b)
# sum=0
# count=0
# for i in range(0,len(unit_list)):
#     sum=sum+unit_list[i]
#     count+=1
# print("Sum of all elements in given list: ",sum,"number of houses",count)   
# i=0
# while i<len(unit_list):
#     if sum>=b:
#         print("sufficent")
#         break
#     else:
#         print("not sufficent")
#         break
#     i+=1


# score=[4,5,6,6,7,3,2,8]
# i=0
# a=[]
# while i<len(score):
#     j=score[i]
#     if j not in a:
#         a.append(j)
#     i+=1
# # print(a)
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# # print(max)
# second_max = 0
# i=0
# while i<len(a):
#     if a[i]>second_max:
#         if a[i]!=max:
#             second_max=a[i]
#     i=i+1
# print(a,second_max)


# runup

# 
# a=[3,4,5,6,8,9,10,12]
# Python Program to find Largest and Smallest Number in a List 
 
# number = []
# n = int(input("Enter the Total Number of List Elements: "))
# for i in range(1, n + 1):
#     value = int(input("Enter the Value of %d Element : " %i))
#     number.append(value)
# sorted_list = sorted(number)
# print("Sorted elements in list : ",sorted_list)
# print("The Third Smallest Element in this List is : ", sorted_list[2])
# print("The Third Largest Element in this List is : ", sorted_list[-3])



# def hcf(x, y):
#    while(y):
#        x, y = y, x % y
#    return x
# hcf = hcf(54, 24)
# print("The HCF is", hcf)


# def lcm(x, y):
#    if x > y:
#        greater = x
#    else:
#        greater = y

#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1

#    return lcm

# num1 = int(input("enter the num1 "))
# num2 = int(input("enter the num2 "))

# print("The L.C.M. is", lcm(num1, num2))



# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# l=[]
# count=0
# while i<len(n):
#     if n[i]  not in l:
#         l.append(n[i])
#         count+=1
#     i+=1
# print(l,)        


# list1=[1,2,3,4,5,65,78,23,3,9,4]
# for i in range(0,len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]>=list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)
# k=int(input("enter number you want sum :- "))
# sum=list1[k-1]+list1[-k]
# print(sum)