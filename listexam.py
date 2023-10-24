l1=[500,800,600,200,900]
start=1
sum=0
for c in range(start,4):
    sum=sum+l1[c]
    print(c,":",sum)
    sum=sum+l1[0]*10
    print(sum)