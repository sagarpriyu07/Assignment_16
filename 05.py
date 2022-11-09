# to check if all the items in the tuple are same
t1=(5,5,5,5,5,5)
for i in range(len(t1)-1):
    if t1[i]==t1[i+1]:
        continue
    else:
        print("All elements in tuple are not same")
        break
else:
    print("All element in tuple are same")
        