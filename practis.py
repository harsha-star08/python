'''n=int(input())
if n>0:
    print("P")
else:
    print("n")'''
'''n=9474
o=n
dig=len(str(n))
t=0
while(n>0):
    d=n%10
    t+=d**dig
    n=n//10
if o==t:
    print("s")
else:
    print("no") arm'''
'''n=15
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
fact'''
'''n=12
o=n
s=0
while n>0:
    s+=n%10
    n=n//10
if o%s==0:
    print("h")
else:
    print("n")'''
'''n=15
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s>n:
    print("tr")
else:
    print("fa")
abun'''
'''a=76
o=a
b=a*a
if a>0:
    d=a%10
    if d==b:
       print("a") 
    else:
        print("n")'''

'''def fun(a):
    if a==0:
        return 
    fun(a-1)
    print(a)
    
fun(10)   1 to n'''
'''def fun(a):
    if a==0:
        return 
    print(a)
    fun(a-1)
fun(10)  '''
'''def fun(a):
    if a==0:
        return 0
    return a + fun(a-1)
print(fun(5))'''


'''class Attendence(Exception):
    pass
try:
    a=int(input())
    if a>75:
        print("crt ")
    else:
        raise Attendence("shortage")
except Attendence as e:
    print(e)'''
'''class Temperature(Exception):
    pass
try:
    a=int(input())
    if a>0:
        print("crt ")
    else:
        raise Temperature("enter crctly")
except Temperature as e:
    print(e)'''
'''class Atmpin(Exception):
    pass
try:
    a=int(input())
    if len(str(a))==4:
        print("crt atm  ")
    else:
        raise Atmpin("4 dig is needed")
except Atmpin as e:
    print(e)'''
'''class person:
    def dis_name(self,a):
        print(a)
class stu(person):
    def dis_roll(self,b):
        print(b)
s=stu()
s.dis_roll("123")
s.dis_name(input())
'''
'''class Father:
    def fa_pro(self):
        print("my land")
class Mother(Father):
    def mo_pro(self):
        print("my jewel")
class Child(Mother):
    def chil_pro(self):
        pass
c=Child()
c.chil_pro()
c.mo_pro()
c.fa_pro()'''
'''class Animal:
    def eat(self):
        print("animal eats")
class dog(Animal):
    def bark(self):
        print("bow bow")
class puppy(Animal):
        pass
a=puppy()
b=dog()
a.eat()
b.eat()'''
'''class Animal:
    def eat(self):
        print("animal eats")
class dog:
    def bark(self):
        print("bow bow")
class puppy(Animal,dog):
        pass
a=puppy()
a.eat()
a.bark()'''
'''f=open("file1.txt","r")
print(f.read())
f=open("file1.txt","a")
f.write("python")
f=open("file1.txt","r")
c=0
for i in f:
    c+=1
print(c)
f.close()
'''
'''import csv
f=open("data.csv","w")
w=csv.writer(f)
w.writerow(["afu",16,"male"])
f=open("data.csv","r")
r=csv.reader(f)
for i in r:
    print(i)'''
'''import json
data = {
    "name": "Harsha",
    "age": 20,
    "course": "CSE"
}
f = open("student.json", "w")
json.dump(data, f)
f.close()
'''
'''def add(a,b):
    return a+b
def dif(a,b):
    return a-b
a=10
b=2
print(add(a,b))'''
'''a=int(input())
if a&1:
    print("o")
else:
    print("e")
without % e or o'''
'''c=121
o=c
rev=0
while c>0:
    d=c%10
    rev=rev*10+d
    c//=10
if o==rev:
    print("pa")
else:
    print("no")'''
'''n=5
for i in range(0,n):
    for j in range(0,n):
      if i==0 or i==n-1 or j==0 or j==n-1:
        print("*",end="")
      else:
        print(" ",end="")
    print()'''
'''n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()'''
'''f=open("file1.txt","r")
data=f.read()
c=0
for i in data:
    if i in "aeiouAEIOU":
        c+=1
print(c)

'''
'''f = open("file1.txt", "r")

data = f.read()

lines = data.split("\n")
words = data.split()

print("Lines =", len(lines))
print("Words =", len(words))
print("Characters =", len(data))
f.close()
'''
''''a=[0,1,0,2,3]
i=0
for j in range(len(a)):
   if a[j]!=0:
        a[i],a[j]=a[j],a[i]
        i+=1
print(a)
        '''
'''n = 5

for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)'''
'''s="hello"
a=list(s)
l=0
r=len(a)-1
while l<r:
    if a[l]  not in "aeiouAEIOU":
        l+=1
    elif a[r] not in "aeiouAEIOU":
        r-=1
    else:
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
print("".join(a))
'''
'''s = "A man, a plan, a canal: Panama"

l = 0
r = len(s) - 1

while l < r:

    # Skip non-alphanumeric characters
    while l < r and not s[l].isalnum():
        l += 1

    while l < r and not s[r].isalnum():
        r -= 1

    # Compare characters (ignore case)
    if s[l].lower() == s[r].lower():
        print(True)
        break

    l += 1
    r -= 1
else:
    print(False)'''
'''a = [1,1,2,2,3,3,4]

i = 0

for j in range(1, len(a)):
    if a[i] != a[j]:
        i += 1
        a[i] = a[j]

print(a[:i+1])'''
'''n=5
for i  in range(1,n+1):
    print("*"*(i)+" "*(2*(n-i))+"*"*i)
for j in range(n-1,0,-1):
    print("*"*j+" "*(2*(n-j))+"*"*j)'''
'''n = 5

for i in range(1, n + 1):

    # Spaces
    print(" " * (n - i), end="")

    # Stars and inner spaces
    if i == 1:
        print("*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        print("*" + " " * (2 * i - 3) + "*")'''
'''n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
    
        print(chr(65+j),end="")
    for k in range(i-2,-1,-1):
        print(chr(65+k),end="")
    print()'''
'''a=[1,2,3,4,5]
k=2
w=sum(a[:k])
print(w/k)
for i in range(k,len(a)):
    w=w+a[i]-a[i-k]
    print(w/k)'''
'''from itertools import permutations

a = [1,2,3]

print(list(permutations(a)))'''

'''n=5
for i in range(1,n+1):
    if i==1 :
        print(" "*(n-i)+"*"*i)
    elif i==n:
        print("*"*(2*n-1))
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")
'''
'''n=5
for i in range(1,n+1):
    print("*"*i+" "*((2*n)-(2*i))+"*"*(i))
for i in range(n-1,0,-1):
     print("*"*i+" "*(2*(n-i))+"*"*i)
'''
'''n=4
for i in range(1,n):
    if i==1:
        print(" "*(n)+"*")
    print(" "*(n-i)+"*"+" "*((2*i)-1)+"*")
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"+" "*((2*i)-1)+"*")
    if i==1:
        print(" "*(n)+"*")'''

'''a=4
for i in range(1,a):
    if i==1:
        print(" "*(a)+"*")
    else:
        print(" "*(a-i)+"*"+" "*((2*i)-1)+"*")
for i in range(a,0,-1):
    if i==1:
        print(" "*(a)+"*")
    else:
        print(" "*(a-i)+"*"+" "*((2*i)-1)+"*")'''

'''a=5
b=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*((2*(a-i))),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(a-1,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*((2*(a-i))),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()'''

'''a=[1,2,3,2,4,1,5,3]
n=8
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    print(k,end=" ")
'''
'''a=[2,7,11,15,3]
tar=10
for j in range(len(a)):
  for i in range(j+1,len(a)):
    if a[j]+a[i]==tar:
        print(j,i)
    '''
'''a=[1,2,3,4,5]
b=[]

for j in range(len(a)):
  p=1
  for i in range(len(a)):
    if a[j]!=a[i]:
      p=p*a[i]
  b.append(p)
    
print(b)
'''
    

    