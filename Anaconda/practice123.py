'''list=[1,2,3,4,2,5,7,3,3,4,2,5,3,2,2]
n=int(input("enter the no"))
count=0
for i in list:
    if n==i:
        count=count+1
print("occure",i)
print(count)'''

'''Eneter a num : 3'''
'''Count which num occur more times'''
'''count each num occurence'''
'''List=[1,8,3,4,5,6,7,8,1,2,2,8,7,3,8,4,6,7,8,6,1,1]

listFreq=[]
size=len(List)
for i in range(size):               # GENERATE SAME SIZE LIST WITH ALL -1
    listFreq.append(int(-1))

for i in range(len(List)):          # COUNT FREQ OF EACH NUM
    count=1
    for j in range(i+1,len(List)):
        if List[i]==List[j]:
            count+=1
            listFreq[j]=0           # SET FREQ=0 WHERE NUM IS REPEATED
    if listFreq[i]!=0:
        listFreq[i]=count

print('OCCURENCE OF EACH NUMBERS : ')
for i in range(size):               # PRINT ALL NUM WITH FREQ
    if listFreq[i]!=0:
        print(List[i],' ----> ',listFreq[i])
max=listFreq[0]
for i in range(size):               # CHECK WHICH NUM OCCUR MORE TIMES
    if listFreq[i]>max:
        max=listFreq[i]
        print("MORE OCCURENCE OF NUMBER IS BELOW : ")
        print(List[i], ' -----> ',max)
        
n=int(input('number'))
for i in range(n):
    for j in range(0,i+1):
        print('*',end=" ")
    print('\r')
n=int(input('number'))
for i in range(1,n):
    for j in range(1,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print('*',end="")
    print()   '''
list1=[] 
list3=[] 
list4=[]
r=int(input('rows:'))
c=int(input('col:'))
for i in range(r):
    list=[]  
    for j in range(c):
        r1= int(input('enter element'))
        list.append(r1)
    list1.append(list)
print(list1)
for i in range(r):
    list2=[]  
    for j in range(c):
        r2= int(input('enter element'))
        list2.append(r2)
    list3.append(list2)
print(list3)
for i in range(r):
    for j in range(c):
        list4[i][j]=list1[i][j]+list3[i][j]
print(list4)        



    
    

