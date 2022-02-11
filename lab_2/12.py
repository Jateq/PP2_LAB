x=input()
x = x.split()
x=set(x)
a = list()
t = ""
for i in x:
    for j in i:
        if j.isalpha():
            t+=j
    a.append(t)
    t =""
a.sort()
print(len(a))
for i in a:
    print(i)