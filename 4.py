def fun(n=4):
    print(f"the number is {n}")
fun()
fun(329349)
def avg(**kwargs):
    t = sum(kwargs.values())
    c = len(kwargs)
    a = t/c
    print(a)
avg(m=90,v=33,c=11)

add_ten = lambda x:x+10
print(add_ten(13))

arr = [1,2,3,4,5,6,7,8,9]
sqc = list(map(lambda x:(x**2)+2,arr))
fa  = list(filter(lambda y:y>=40,sqc))
print(sqc)
print(fa)