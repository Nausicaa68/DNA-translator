import random

def genereDNA(n):
    i=0;
    l=[]
    while i < n :
        l.append(random.choice(['A','G','C','T']))
        i+=1

    return l

ll=genereDNA(100)
#print("".join(ll))
