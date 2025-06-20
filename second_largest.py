a=[1,2,3,4]
fir=sec=float('-inf') #the number can be -1212232321312

for i in a:
    if i> fir: # 1>-23131123, 2>1 3>2 4>3
        sec=fir # sec=-232313 1 2 3
        fir=i #fir=1 2 3 4
    elif fir >= i >sec: # 3>3>2  4>  4 > 3
        sec=i #3

print("sec:",sec)