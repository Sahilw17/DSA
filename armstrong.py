# 153=1^3 + 5^3 + 3^3

a=153
d=0
c=a # the value of a gets hange in loop so the value of a is tored in c for comparison
while a > 0:
   b= a % 10 #3 
   d +=b**3 #9
   a = a//10 #15

if(d==c):
    print("num is arm strong")
else:
      print(f"num is not armstrong")
