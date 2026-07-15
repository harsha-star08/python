"""
a=int(input())
b=int(input())
a,b=b,a
print(a,b)
"""
"""
a=int(input())
if(a<0):
    print("negative")
elif(a>0):
    print("positive")
else:
    print(zero)
"""
"""
x=input()
b=ord(x)
print(b)
"""
"""
x=int(input())
b=chr(x)
print(b)
"""
"""
a=int(input())
d=input()
b=str(a)
c=float(a)
print(b)
print(type(b))
print(c)
print(type(c))
e=a+d
print(e)
print(type(e))
"""
"""
a=int(input())
b=int(input())
c=int(input())
if(a==b and a>c):
    print(" a and b is greater")
elif(a==c and a>b):
    print(" a and c is greater")
elif(b==c and b>a):
    print(" b and c is greater")
elif(a>b and a>c):
    print(" a is greater")
elif(b>a and b>c):
    print(b is greater)
elif(a==b and b==c and a==c):
    print("a,b,c is grester")
else:
    print(c is greater)
"""
"""
a=input()
if(ord(a)>=65 and ord(a)<=90):
    print("uppercase")
elif(ord(a)>=97 and ord(a)<=122):
    print("Lowercase")
elif(ord(a)>=48 and ord(a)<=57):
    print("digit")
else:
    print("special character")
"""
"""
a=int(input())
if(a%4==0):
    print(a, "is leap year")
else:
    print(a ,"is not leap year")
"""
"""
n=3
for i in range(1,4):
    print("*" *i)
"""
"""reverse with loop
a=234
rev=0
while(a>0):
    last=a%10
    rev=(rev*10)+last
    a=a//10
print(rev)
"""
""" reverse the string without loop
n=123
o=n%10
n=n//10
t=n%10
n=n//10
h=n%10
c=o*100+t*10+h*1
print(c)
"""
"""
p=int(input())
n=int(input())
r=int(input())
si=(p*n*r)/100
print(si)
"""
""" eve
for i in range(1,101):
    if(i%2==0):
        print(i)
"""
""" natu
for i in range(100,0,-1):
    print(i)
"""
""" sum and avdg
a=int(input())
b=int(input())
sum = a+b
avg =sum/2
print (sum)
print(avg)
"""
""" vowels
alp=input()
if(alp=='a' or alp=='e' or alp=='i' or alp=='o' or alp=='u'):
    print("Vowel")
else:
    print("Consonant")
"""
""" tables
a=int(input())
for i in range(1,11,1):
    print(a,"*",i,"=",a*i)
"""
""" 5 and 11
a=int(input())
if a%5==0:
    print(" True")
elif a%11==0:
    print("True")
else:
    print("False")
"""
"""square root
import math
a=int(input())
b=math.sqrt(a)
print(b)
"""
""" nxt method
a=int(input())
for i in range(1,a):
    if(i*i==a):
        print(i)
"""
"""factorial
a=int(input())
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
"""
""" count 
a=int(input())
even=0
odd=0
for i in range(1,a+1,1):
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd:",odd)
"""
"""reverse
a=int(input())
rev=0
while a>0:
    last dig=a%10
    rev=rev*10+dig
    a=a//10
print(rev)
"""
"""
def myfun(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
myfun(3)
"""
"""
even=lambda a:a%2==0
print(even(2))
"""
"""
sample=lambda a:print("even") if a%2==0 else print("odd")
sample(int(input()))
"""
""" palindrome
def samp(a):
    rev=0
    org=a
    while(a>0):
        dig=a%10
        rev=rev*10+dig
        a=a//10
    return rev==org
print(samp(int(input())))
"""
""" count
def vow(x):
    count=0
    for ch in x:
        if ch in'aeiouAEIOU':
            count=count+1
    return count
print(vow(input()))
"""
""" rev str
def fun(a):
    rev=""
    for ch in a:
        rev=ch+rev
    return rev
print(fun(input()))
"""
""" prime
def func(a):
    count=0
    for i in range(1,a+1):
        if(a%i==0):
            count=count+1
    if(i==2):
        return True
    else:
        return False
print(func(int(input())))    
"""
""" 3&8
def func(a):
    if(a%3==0 and a%8==0):
        return True
    else:
        return False
print(func(int(input())))
"""

"""day 4 
 
 sum 
l=list(map(int,input().split()))
sum=0
for i in l:
    sum+=i
print(sum)
"""
""" elements
l=list(map(int,input().split()))
print(len(l))
"""
""" large
l=list(map(int,input().split()))
l.sort(reverse=True)
print(l[0])
"""
""" small
l=list(map(int,input().split()))
l.sort()
print(l[0])
"""
""" count 
l=list(map(int,input().split()))
even=0
odd=0
for i in l:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)
"""
"""rev
l=list(map(int,input().split()))
print(l[::-1]) """
""" present
l=list(map(int,input().split()))
n =int(input())
if n in l:
    print("present")
else:
    print(" not present")
"""
""" merge
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l2:
    l1.append(i)
print(l1)
"""
""" sepearte
l1=list(map(int,input().split()))
l3=[]
l2=[]
for i in l1:
    if(i%2==0):
        l2.append(i)
    else:
        l3.append(i)
print(l3)
print(l2)
"""
""" sec lar
l1=list(map(int,input().split()))
l1.sort(reverse=True)
print(l1[1])
"""
""" count
t=tuple(map(int,input().split()))
ele=int(input())
print(t.count(ele))
"""
""" rev
t=tuple(map(int,input().split()))
print(t[::-1]) """
""" unpack
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
t = (name, age, city)
name,age,city=t
print(age)
"""
""" iterate
t=tuple(map(int,input().split()))
for i in t:
    print(i) """
"""exist
t=tuple(map(int,input().split()))
n=int(input())
if n in t:
    print("exist")"""
""" con
t = (10, 20, 30, 40)
l = list(t)
print(l)
"""
""" exist
s=set(map(int,input().split()))
n =int(input())
if n in s:
    print("exist")
else:
    print("no")
"""
""" op
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)
"""
""" dupl
l = list(map(int, input().split()))
l = list(set(l))
print(l)
"""
""" up
name = input()
age = int(input())
city = input()
student = {
    "name": name,
    "age": age,
    "city": city
}
print(student)
student.update({"course":"Python"})
print(student)
print(student.items())
"""
"""
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
"""
"""squa
d={}
for i in range(1,6):
    d[i]=i*i
print(d)
"""
"""Area
import math
class Circle:
    def __init__(self,rad):
        self.radius=rad
    def cal(self):
        area=math.pi *self.radius*self.radius
        print(area)
c1=Circle(int(input()))
c1.cal()
"""
""" Book
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
title=input()
author=input()
b=Book(title,author)
b.display()
"""
""" inherits
class Student:
    def __init__(self,marks,performance):
        self.marks=marks
        self.perf=performance
    def overall(self):
        print("performance of a student is",self.perf)
class Person(Student):
    pass
marks=int(input())
performance=input()
s1=Person(marks,performance)
s1.overall()
"""
""" method
class School:
    school_name="vasavi"
    @classmethod
    def display(self):
        print(self.school_name)
s=School()
s.display()
"""
""" rec area
class Rectangle:
    def __init__(self,length,breadth):
          self.len=length
          self.bred=breadth
    def area(self):
         area=self.len*self.bred
         print("area:",area)
len=int(input())
bred=int(input())
r=Rectangle(len,bred)
r.area()
"""
""" lib management
class Library:
    def __init__(self,book,author):
        self.book=book
        self.author=author
    def issued(self):
        print(self.book, "is issued")
    def returnbook(self):
        print(self.book ,"is returned")
book=input()
author=input()
l=Library(book,author)
l.issued()
l.returnbook()
"""

"""count
f=open("file1.txt","r")
count=0
for i in f:
    count+=1
print(count)
f.close()
"""
""" overriding
class Vehicle:
    def start(self,a):
        print(a,"vehicle starts")
class Car(Vehicle):
    def start(self,a):
        print(a,"car starts")
a=input()
c1=Car()
c1.start(a)
"""
"""except
try:
    n=int(input())
    print(100/n)
except ZeroDivisionError as z:
    print("enter a value not a zero",z)
except ValueError as v:
    print("enter a number",v)
finally:
    print("succesfull")
"""
"""range
class101 MarksError(Exception):
    pass
try:
    a=int(input("enter a marks:"))
    if(a<0 or a>100):
        raise MarksError("enter a crt marks")
    print("mark entered")
except MarksError as e:
    print(e)
"""
""" neg
class NegativeError(Exception):
    pass
try:
    a=int(input("enter a number:"))
    if(a<0):
        raise NegativeError("enter a positive number")
    print(" successfull")
except NegativeError as e:
    print(e)
 """
"""over
import math
class Shape:
    def area(self,a,b):
        print("area")
class Rectangle(Shape):
    def area(self,a,b):
        print(a*b)
class Circle(Shape):
    def area(self,a,b):
        print(math.pi*a*a)
a=int(input())
b=int(input())
c=Circle()
c.area(a,b)
"""
"""vowels
f = open("file1.txt", "r")
count = 0
for line in f:
    for ch in line:
        if ch in "aeiouAEIOU":
            count += 1
print("Number of vowels =", count)
f.close()
"""
"""copy
import csv
f=open("data.csv","r")
reader=csv.reader(f)
f1=open("file1.txt","w")
for i in reader:
    f1.write(str(i))
    f1.write("\n")
f.close()
f1.close()
"""
"""
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
"""
"""
a=int(input())
for i in range(1,a+1):
    print(str(i)*i)
"""
"""
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""
"""
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end="")
        i=i+1
    print()
"""
"""
a=int(input())
count=1
for i in range(1,a+1):
    for j in range(i):
        print(count,end="")
        count+=1
    print()
"""
"""
a = int(input())
for i in range(1, a+1):
    for j in range(a-i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()
"""
"""
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i),str(i)*i)
"""
"""
a=int(input())
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
"""
"""
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))
    print(" "*(a-i),"*"*(2*i-1)) 
    difference is if we put comma it take extra space  but + give means it take only the given sapce
    
"""
"""
a=int(input())
b = a * (a+ 1) // 2
for i in range(1,a+1):
    for j in range(i,a+1):
        print(b,end="")
        b-=1
    print() 
"""
"""
a=4
b = a * (a+ 1) // 2
for i in range(1,a+1):
    for j in range(1,i+1):
        print(b,end="")
        b-=1
    print() 
    """
"""
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
a=7
for i in range(1,a+1):
        if(i<=(a//2)+1):
           print("*"*i) 
        else:
              print("*"*((a-i)+1))
"""
"""
a=7
n=a//2
b=a-n
for i in range(1,a+1):
    if(i<=n):
        print("*"*i)
    else:
        print("*"*b)
        b-=1
"""
'''
words=["cat","dog","apple"]
d={i:len(i) for i in words}
print(d)'''

'''a=int(input())
d={i:"even" if i%2==0 else "odd" for i in range(1,a+1) }
print(d)'''

'''data={"a":1,"b":2,"c":3}
d={v:k  for k,v in data.items}
print(d)'''

'''
a=int(input())
for i in range(1,a+1):
    print("*"*a)'''

'''a=int(input())
for i in range(a):
    for j in range(a):
      if i==0 or i==a-1  or j==0 or j==a-1:
         print("*",end="")
      else:
         print(" ",end="")
    print()
'''
'''a=int(input())
for i in range(a):
    print(" "*i+"*"*a)'''
'''a=int(input())
for i in range(a):
    print("*"*a,end="")
    print()'''
'''a=int(input())
for i in range(a):
    for j in range(a):
      if i==0 or i==a-1 or j==0 or j==a-1:
         print("*",end="")
      else:
         print(" ",end="")
    print()'''
'''a=7
for i in range(a+1):
        print(" "*(a-i),end="")
        print("*"*((i*2)-1))
for i in range(a):
        print(" "*i,end="")
        print("*"*(((a-i)*2)-1))
print()'''
'''n = int(input("Enter n: "))
for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    elif i == n - 1:
        print("*" * (2 * n - 1))
    else:
        print("*" + " " * (2 * i - 1) + "*")'''
'''n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("*" * i)'''
'''n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")'''
'''nums=[1,15,6,3]
sum=0
dif=0
for i in range(len(nums)):
          sum=sum+nums[i]
for i in nums:
   for j in str(i):
     dif+=int(j)
print(sum-dif)
'''
'''n=[1,3,6,10,12,15]
a=0
count=0
for i in range(len(n)):
  if(i%2==0):
    if(i%3==0):
         count+=1
         a+=i
if count==0:
 return 0
c=a//count
print(c) '''
'''a=[2,2,1]
d={}
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for k,v in d.items():
    if v==1:
        print(k)
'''
'''nums=[1,2,3,1,1,3]
count = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
                  count += 1
return count
''' 
'''
nums=[0,1,0,3,12]
a=len(nums)
for i in range(0,a):
   for j in range(a,0,-1):
        if(i==0):
            a[i]=a[j]
print(nums)'''
'''
a=[1,3,2,5,4]
k=2
for i in range(len(a)-k+1):
    print(max(a[i:i+k]),end=" ")
    in this + and - have same op precedence so we take from left to right
''''''
num=int(input())
rev=0
while num>0:
    dig=num%10
    rev=(rev*10)+dig
    num=num//10
print(rev)
''''''
text = "Hello"
rev = text[::-1]
print(rev)   # Output: olleH
'''

'''n=5
b=1
for i in range(n,0,-1):
    if(i==n):
        print("*"*((2*n)-1))
    else:
        print("*"*i+" "*b+"*"*i)
        b+=2'''
'''arr=[1,2,3,4,3,2,3,6,7,5]
c=0
n=len(arr)
for i in range(n):
    count=0
    for j in range(n):
        if(arr[i]==arr[j]):
            count+=1
    if count>1 and arr[i] not in arr[:i]:
        c+=1
print(c)'''
'''class WeakpassError(Exception):
    pass

try:
    passwo=int(input())
    if(passwo>8):
        print("Valid")
    else:
        raise WeakpassError("enter correctly")
except WeakpassError as e:
    print(e) if we give in str we can use len() 
'''
'''class central:
    def rules(self):
        print("High demand")
class state:
    def order(self):
        print("Low demand")
class loc_pep(central,state):
        pass

a=loc_pep()
a.rules()
a.order()'''
'''d={1:1,2:2,3:3,4:1,5:1,6:1,7:1}
arr=[1,2,3,4,3,2,3,6,7,5]
c=0
n=len(arr)
odd=0
for i in range(1,n+1):
    for j in range(i+1,n):
        if(arr[i]==arr[j]):
            c+=1
print(c)

for k,v in d.items():
    if(v%2!=0):
        odd+=1
print(odd)
    '''
'''n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")

    for j in range(1,i+1):
       print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()'''

'''n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
       print(chr(64+j),end="")
    for j in range(i-1,0,-1):
        print(chr(64+j),end="")
    print()'''
'''celsius=36.50
arr=[]
kel=celsius+273.15
fah=celsius*1.80+32.00
arr.append(kel)
arr.append(fah)
print(arr)
        '''
'''nums=[-1,-2,-3,-4,1,2,3]
sum=1
for i in range(len(nums)):  
    sum*=nums[i]
if sum>0:
    print(1)
elif sum<0:
    print(-1)
else:
    print(0)'''
'''class Solution(object):
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return nums[i]
'''
'''class Solution(object):
    def minCostToMoveChips(self, position):
        odd = 0
        even = 0

        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(odd, even)
'''
'''class Solution(object):
    def findNumbers(self, nums):
        even = 0

        for num in nums:
            count = 0

            while num > 0:
                count += 1
                num //= 10

            if count % 2 == 0:
                even += 1

        return even'''
'''a=[2,1,5,1,3,2]
k=3
wind=sum(a[:k])
maxim=wind
for i in range(k,len(a)):
    wind=wind+a[i]-a[i-k]
    maxim=max(maxim,wind)
print(maxim)
'''
'''a=[2,1,5,1,3,2]
k=3
wind=sum(a[:k])
maxim=wind
for i in range(k,len(a)):
    wind=wind+a[i]-a[i-k]
    maxim=max(maxim,wind)
print(maxim/float(k))'''
'''s="abciiidef"
k=3
count=0
for i in range(k):
    if s[i] in "aeiou":
        count+=1
maxi=count
for i in range(k,len(s)):
    if s[i-k] in "aeiou":
        count-=1
    if s[i] in "aeiou":
        count+=1
    maxi=max(maxi,count)
print(maxi)'''
'''a=[2,1,5,1,3,2]
k=3
wind=sum(a[:k])
w_avg=sum(a[:k])/k
maxim=w_avg
for i in range(k,len(a)):
    wind=((wind+a[i])-a[i-k])
    w_avg=wind/k
    maxim=max(maxim,w_avg)
print(maxim)'''
'''a=[1,2,4,5,6]
k=3
c=0
for i in range(k):
    if a[i]%2==0:
        c+=1
print(c,end=" ")
for i in range(k,len(a)):
    if a[i-k]%2==0:
        c-=1
    if a[i]%2==0:
        c+=1
    print(c,end=" ")
   *sliding= Old Sum - Leaving + Entering    window = window - a[i-k] + a[i]'''
'''# First window
count = 0

for i in range(k):
    # process arr[i]

ans = count

# Sliding
for i in range(k, len(arr)):

    # remove arr[i-k]

    # add arr[i]

    ans = max(ans, count)   skeleton code of sliding '''
'''a = [1,2,1,0,1]
tar = 4
left = 0
window_sum = 0
max_len = 0
for right in range(len(a)):
    window_sum += a[right]
    while window_sum > tar:
        window_sum -= a[left]
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)'''
'''s="rahul like pyth34on ufhv87"
v=0
c=0
d=0
a=0
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            v+=1
        else:
            c+=1
    elif i.isdigit():
        d+=1
    else:
        a+=1
print(v)
print(c)
print(d)
print(a)'''

'''class Solution(object):
    def triangleType(self, nums):

        if nums[0] + nums[1] <= nums[2] or \
           nums[0] + nums[2] <= nums[1] or \
           nums[1] + nums[2] <= nums[0]:
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"

        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"

        else:
            return "scalene"'''

'''nums = [5,4,-1,7,8]
maxi = nums[0]
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        maxi = max(maxi, total)
print(maxi)'''

'''class Solution(object):
    def canAliceWin(self, nums):
        single = 0
        double = 0
        for num in nums:
            if num < 10:
                single += num
            else:
                double += num
        if single > double:
            return True
        elif double > single:
            return True
        else:
            return False
'''
'''class Solution(object):
    def scoreOfString(self, s):
        total = 0

        for i in range(len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1]))

        return total'''
'''class Solution(object):
    def reverseString(self, s):
       l=0
       r=len(s)-1
       while l<r:
        s[l],s[r] = s[r],s[l]
        l+=1
        r-=1'''
'''class Solution(object):
    def isPalindrome(self, s):
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch.lower()
        return new == new[::-1]'''
'''s = "abccbaacz"

for i in s:
    for j in range(1,len(s)):
            if i==j:
                print(i)'''
''''s = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
maxi=0
for i in s:
    c=0
    if i in s.split(','):
        c+=1
        maxi=max(maxi,c)
print( maxi)
            '''

     
'''day 11       
class Solution(object):
    def scoreOfString(self, s):
        total = 0
        for i in range(len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1]))
        return total'''
'''
class Solution(object):
    def isPalindrome(self, s):
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch.lower()
        return new == new[::-1]'''
'''class Solution(object):
    def isAnagram(self, s, t):
        if sorted(s)==sorted(t):
            return True
        else:
            return False
   '''
'''class Solution(object):
    def firstUniqChar(self, s):
        d={}
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
            
        return -1
        '''
'''class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix'''
'''class Solution(object):
    def strStr(self, h, n):
        for i in range(len(h) - len(n) + 1):
            if h[i:i+len(n)] == n:
                return i
        return -1'''
'''def nat (n):
    if n==0:
        return 0
    return n+nat(n-1)
print(nat(5))  recursive'''
'''def num(n):
    if n==0:
        return 0
    return n%10 +num(n//10)
print(num(123))'''
'''def num(n):
    if n==0:
        return 0
    return 1+ num(n//10) 
print(num(123))'''
'''def num(n):
    if n==0:
        return 1
    return n%10*num(n//10)
print(num(123))'''
'''def num(n):
    if n=="":
        return ""
    return n[::-1]
print(num("hello"))'''
'''def num(n):
    if n=="":
        return ""
    return n==n[::-1]
print(num("hello"))'''
'''def num(n,rev):
    if n==0:
        return rev
    return num(n//10,rev*10+n%10)
def pal(n):
    return n==num(n,0)    
print(pal(123))'''
'''def fun(a):
    l=0
    r=len(a)-1
    while l<r:
      if a[l]!=a[r]:
          return False
      l+=1
      r-=1
    return True
print(fun("Hello"))'''
'''def fun(a):
    b=str(a)
    l=0
    r=len(b)-1
    while l<r:
      if b[l]!=b[r]:
          return False
      l+=1
      r-=1
    return True
print(fun(128))
pal in num'''
'''def num(a):
    if a==0:
        return 0
    if a==1:
        return 1
    while a>=2:
       return num(a-1)+num(a-2)
print(num(3))'''
'''def num(a,n):
    if n==0:
        return 0
    return a[n-1]+num(a,n-1)
a=[10,20,30]
print(num(a,len(a)))
    '''
'''def num(a):
    a=list(a)
    l=0
    r=len(a)-1
    while l<r:
         a[l],a[r]=a[r],a[l]
         l+=1
         r-=1
    return "".join(a)

print(num("Rahul"))
'''
'''def fun(a, n):
    if n == 1:
        return a[0]
    small = fun(a, n - 1)
    if a[n - 1] > small:
        return a[n - 1]
    else:
        return small
a = [10, 20, 30]
print(fun(a, len(a)))'''
'''def fun(s):
    if len(s)==1:
        return s[0]
    return max(s[0],fun(s[1:]))
a=[10,20,30]
print(fun(a))    '''
'''def fun(s):
    if len(s)==1:
        return s[0]
    return min(s[0],fun(s[1:]))
a=[10,20,30]
print(fun(a))'''
'''def fun(a):
    if len(a )== 0:
        return 0
    if a[0] in "aeiouAEIOU":
        return 1 + fun(a[1:])
    else:
        return fun(a[1:])
print(fun("Hello"))'''
'''def fun(a):
    if len(a)==0:
        return 0
    if a[0]==" ":
        return 1 + fun(a[1:])
    else:
        return fun(a[1:])
print(fun("hello i am har "))'''
'''def fun(a):
    if len(a)==0:
        return 0
    if a[0]==r:
        return 1 + fun(a[1:])
    else:
        return fun(a[1:])
r=input()
print(fun("banana"))'''
'''a=int(input())
b=int(input())
while (b!=0):
    a,b=b,a%b
print(a)gcd'''
'''def fun(a,b):
    if b==0:
        return a
    return fun(b,a%b)
a=18
b=24
print(fun(a,b))'''
''''class Solution(object):
    def subsets(self, nums):
        ans = []

        def fun(i, temp):
            if i == len(nums):
                ans.append(temp[:])
                return

            # Take
            temp.append(nums[i])
            fun(i + 1, temp)

            # Don't take
            temp.pop()
            fun(i + 1, temp)

        fun(0, [])
        return ans   subset impo'''
'''def fun(a):
    l=[]
    def bt(i,s):
        if len(i) == len(a):
            l.append(s[:])
            return
        for a in range(len(s)):
            i.append(s[i])
            bt(i,s[:a])

   
a=[1,2,3]
print(fun(a))'''


'''class Solution(object):
    def getConcatenation(self, nums):
        l=[]
        for i in range(len(nums)):
                l.append(nums[i])
        if l==nums:
            return l+nums'''
'''class Solution(object):
    def runningSum(self, nums):
        l=[]
        a=0
        for i in range(len(nums)):
            a+=nums[i]
            l.append(a)
        return l
'''
'''class Solution(object):
    def shuffle(self, nums, n):
        a=[]
        for i in range(n):
            a.append(nums[i])
            a.append(nums[i+n])
        return a'''
'''class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        i=0
        for j in range(1,len(nums)):
                if nums[i]!=nums[j]:
                    i+=1
                    nums[i]=nums[j]
        return i+1
'''
'''class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i'''
'''class Solution(object):
    def plusOne(self, d):
        for i in range(len(d)-1,-1,-1):
            if d[i]<9:
                d[i]+=1
                return d
            d[i]=0
        return [1]+d
'''
'''class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans'''
