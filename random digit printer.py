import random as r
a=int(input("enter how mant times to loop random"))
b= input("enter range like a,b")
c=list(map(int,b.split(',')))
print(type(c))
for i in range(
    a   
    ):
    c=r.randint (c[0],c[1])
    print(c)
