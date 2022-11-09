#swap two tuples
print("Enter elements for first tuple separated by comma:")
t1=tuple([eval(e) for e in (input().split(','))])
print("Enter elements for second tuple separated by comma:")
t2=tuple([eval(e) for e in (input().split(','))])
print("Before swapping")
print(t1)
print(t2)
t3,t4=t1,t2
t1,t2=list(t1),list(t2)
for i in range(len(t1)):
    t1[i],t2[i]=t2[i],t1[i]
print("After swapping")
print("first tuple is",tuple(t1))
print("ssecond tuple is",tuple(t2))