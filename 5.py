a = [1,2,34,656,4,4,456,2,23,78]
l = len(a)
b = [0]*l

for i in range (0,l):
    b[i]=a[l-i-1]
b.pop()
b.append(10)
for j in (b):
    print(j)

t = tuple(b)
s = set(t)
s.add(10)
print(s)            

s = {"Ken":70,"Mila":60,"Harry":30,"Kane":55,"Nena":12}
for a,b in s.items():
    if b>50:
        print(f"{a}:{b}")