print("Data types ,condition,loops and function")
x='boring'
def myfunc():
  print("Python is " + x)

myfunc()

a=10            #int
b=3.14          #float
c='Your_Name'   #str
d=True          #bool
e=[1,2,3]       #list
f=(4,5)         #tuple
g={"x":1}       #dict
h={1,2,3}       #set

print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)
print(type(g),g)
print(type(h),h)

if a<16:
    print("smaller")
else :
    print("larger")
x, y, z = "Orange", "Banana", "Cherry"
f = ["apple", "banana", "cherry"]
x, y, z = f
print(x)
print(y)
print(z)

i=6
while i>0:
    print(i)
    i-=1