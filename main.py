print("veeraswamy\n"*3)
print(r"\tcurrent\new\folder")
def function(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
n= int(input("Enter a number: "))
function(n)
d={"name":"veeraswamy","age":20,"Town":"Vijayawada"}
d.update({"name":"Sai"})
# print(d)
dict={
    "name":"veeraswamy",
    "gender":"male",
    "age":"20",
    "courses":["Python","Java","Data Science"]
}
dict.update({"name":"Hari"})
dict.update({"courses":["Machine Learning","Deep Learning","C++","C"]})
print(dict)
def count(*args):
    print(type(args))
# count(1,2,3,4,5,6,7,8,9)
def dicts(**kwargs):
    print(type(kwargs))
dicts(name="veeraswamy",age=21,Gender="Male")
oops
l=[1,2,3]
s="String"
len(l)
len(s)
print(len(l))
print(len(s))
x="veeraswamy"
x=x[1:5]
x=x[::-1]
print(x)
while True:
    print("Hi")
n=30
sum=0
while n>0:
    sum+=n
    n-=1
print(sum)
n=30
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of first",n,"numbers is:",sum)
