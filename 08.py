#sort a tuple of tuples by second item
t1=(('a',21),('b',37),('c',11),('d',29))
'''l1=list(t1)
j=1
for e in range(0,len(l1)-1):
    for i in range(0,len(l1)-1):
        if l1[i][j]>l1[i+1][j]:
            l1[i],l1[i+1]=l1[i+1],l1[i]
t1=tuple(l1)
print(t1)'''
'''l1=tuple(sorted(t1,key=lambda y:y[1]))
print(l1)'''
l1=list(t1)
l1.sort(key=lambda y:y[1])
print(tuple(l1))