l=[1,1,1,2,3,2,4,4,4,1]
h={}
b=[]
for i in l:
    h[i]=l[i]
l.clear()
for key,value in h.items():
    l.append(key)
print(l)
