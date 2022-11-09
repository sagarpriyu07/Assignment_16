#change the first item (22)os a list within the following tuple to 222
tuple1=(11,[22,33],44,55)
print(tuple1)
list1=list(tuple1)
list1[1][0]=222
tuple1=tuple(list1)
print(tuple1)

