k=1
d=1
tot=0

while (k<=4000000):
    if((k%2)==0):
        tot=tot+k
    k, d=d, k+d
print(tot)
