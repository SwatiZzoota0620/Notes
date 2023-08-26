n=int(input("number:"))
sum=0
list1=[]
list2=[]
for x in range(1,n):
    if(n%x==0):
        sum=sum+x
        if(x%2==0):
            list1.append(x)
        else:
            list2.append(x)
print(list1)
print(list2)
if(sum==n):
    print('perfect no')
else:
    print('not perfect no')