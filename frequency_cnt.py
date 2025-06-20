#1,1,2,3,4,5,5 hashmap will store 1,2,3,4,5
l=[1,1,2,3,4,5,5,5]
h={}
cnt=0
for i in l:
        if i in h:
            h[i]+=1
        else:
              h[i]=1
for key,value in h.items():
      print(f"{key} is for {value} times")
