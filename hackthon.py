# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x. 
# 
# class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n<=0:
    #         return False
    #     while n>1:
    #         if n%2==1:
    #             return False
    #         n=n//2
    #     return True        
            

# You're given strings jewels representing the types of stones that 
# are jewels, and stones representing the stones you have. Each character 
# in stones is a type of stone you have. You want to know how many of the 
# stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".            
             
#  class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         j={}
#         for i in jewels:
#             j[i]=1
#         number=0
#         for i in stones:
#             if i in j:
#                  number+=1
#         return number        
              
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         address=address.split(".")
#         return "[.]".join(address)
        
# Given an integer number n, return the difference 
# between the product of its digits and the sum of its digits.

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         sum=0
#         product=1
#         while n>0:
#             product*=(n%10)
#             sum+=(n%10)
#             n//=10
#         return product-sum


# Given an integer num, return the number 
# of steps to reduce it to zero.
# In one step, if the current number is even, you have 
# to divide it by 2, otherwise, you have to subtract 1 from it.

 

# Example 1:

# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.

# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#         a=0
#         while num>0:
#             if num%2==0:
#                 num= num//2
#             else:
#                  num-=1
#             a+=1
#         return a   
        
# Given the array nums, for each nums[i] find out how many 
# numbers in the array are smaller than it. That is, for each 
# nums[i] you have to count the number of valid j's such that j != i 
# and nums[j] < nums[i].
# Return the answer in an array.

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         i=0
#         list=[]
#         while i<len(nums):
#             min=nums[i]
#             count=0
#             k=0
#             while k<len(nums):
#                 if nums[k]<min:
#                     count+=1
#                 k+=1
#             list.append(count) 
#             i+=1
#         return b        

# Input
# [0,1,2,3,4]
# [0,1,2,2,1]
# Output
# [0,1,3,6,10]
# Expected
# [0,4,1,3,2]
#         sum=0
#         i=0
#         list=[]
#         while i<len(nums):
#             sum=sum+nums[i]
#             i+=1
#             list.append(sum)
#         return list    
        
# You are given an m x n integer grid accounts where accounts[i][j] 
# is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return 
# the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their 
# bank accounts. The richest customer is the customer that has the maximum wealth.

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6  
# 
# class Solution:
    # class Solution:
    # def maximumWealth(self, a: List[List[int]]) -> int:
    #     list=[]
    #     for i in range(len(a)):
    #         sum=0
    #         for j in a[i]:
    #             print(j) 
    #             sum+=j
    #         list.append(sum)
    #     print(list) 
    #     max=0
    #     for i in range(len(list)):
    #         if list[i]>max:
    #             max=list[i]
    #     return max

# Given two arrays of integers nums and index. Your task is to create target array under the following rules:

#     Initially target array is empty.
#     From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#     Repeat the previous step until there are no elements to read in nums and index.

# Return the target array.

# It is guaranteed that the insertion operations will be valid.

 

# Example 1:

# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]

# Example 2:

# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]

# Example 3:

# Input: nums = [1], index = [0]
# Output: [1]

 

# Constraints:

#     1 <= nums.length, index.length <= 100
#     nums.length == index.length
#     0 <= nums[i] <= 100
#     0 <= index[i] <= i



# list1=[]
#         for i in range(len(nums)):
#             list1.insert(index[i],nums[i])
#         return list1            
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Find the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are   
# [5,6,7,...]. The 2nd missing positive integer is 6.

 

# Constraints:

#     1 <= arr.length <= 1000
#     1 <= arr[i] <= 1000
#     1 <= k <= 1000
#     arr[i] < arr[j] for 1 <= i < j <= arr.length

# Accepted
# 145,925
# Submissions
# 264,233      
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         count=0
#         for i in range(1,10000):
#             if i not in arr:
#                 count=count+1
#             if count==k:
#                 return i

# There is a programming language with only four operations and one variable X:

#     ++X and X++ increments the value of the variable X by 1.
#     --X and X-- decrements the value of the variable X by 1.

# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, 
# return the final value of X after performing all the operations. 
# 
# Example 1:

# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.
       
# class Solution:
    # def finalValueAfterOperations(self, operations: List[str]) -> int:
    #     x=0
    #     for i in operations:
    #         if i=="--X" or i=="X--":
    #             x=x-1
    #         elif i=="X++" or i=="++X":
    #             x=x+1
    #     return x


# nums=[0,1,0,3,12]               
# b = nums.count(0)   
# print(b) 
# i = 0
# while i < len(nums):
#     if nums[i] == 0 :
#        del nums[i]
#     i+=1
#     print(nums)
#     j = 0
#     while j < b :
#         nums.append(0)
#     j+=1
# print(nums)
                       
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count=0
#         n=len(nums)
#         for i in range(n):
#               for j in range(i+1,n):
#                     if nums[i] == nums[j]:
#                         count+=1
#         return count
#         class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count=0
#         n=len(nums)
#         for i in range(n):
#               for j in range(i+1,n):
#                     if nums[i] == nums[j]:
#                         count+=1
#         return count
        
# Given an integer array nums, move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         k = 0
#         for i in nums:
#             # if i in nums:
#                 nums[k] = i
#                 k = k + 1
#         for i in range(k, len(nums)):
#             nums[i] = 0
#         return (nums)
        
# Given an integer array nums, return the greatest common divisor 
# of the smallest number and largest number in nums.

# The greatest common divisor of two numbers is the largest positive 
# integer that evenly divides both numbers.

# Example 1:

# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.

        
# class Solution:
#     def findGCD(self, nums: List[int]) -> int:
#         x=max(nums)
#         y=min(nums)
#         for i in range(1,x+1):
#             if x%i==0 and y%i==0:
#                 hcf=i
#         return hcf        

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         if j==0 or j==i-1:
#             print("*",end=" ")
#         else:
#             if i!=n:
#                 print(" ",end=" ")
#             else:
#                 print("*",end=" ")
#     print()        


# size=5
# for i in range(size):
#     for j in range(size):
#         if i==0 or i==size-1 or j==0 or j==size-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        

                             
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#             print(" ",end=" ")
#     for k in range(2*i+1):
#         if k==0 or k==2*i:
#             print("*",end=" ")
#         else:
#             if i==n-1:
#                 print("*",end=" ") 
#             else:
#                 print(" ",end=" ")       
#     print()        


# for row in range(0,7):
#     for col in range(0,7):
#         if (row+col==3)or (col-row==3)or(row+col==9) or(row-col==3):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# num=int(input("enter the number:"))
# if num%3==1:
#     print("beautiful")
# elif num%3==2:
#     print("better") 
# else:
#     print("best")       

# num=int(input("enter the number:"))
# if (num-1)%3==0:
#     print("beautiful")
# elif (num-2)%3==0:
#     print("better") 
# else:
#     print("best")       

# import string


# num=int(input("enter the number:"))
# i=1
# while i<=num:
#     j=1
#     while j<=i:
#         if j%2==0:
#             print("*",end="")
#         elif j!=2 and j%2==0: 
#             print("*",end="")   
#         else:
#             print(j,end="")
#         j+=1
#     print()    
#     i+=2        

