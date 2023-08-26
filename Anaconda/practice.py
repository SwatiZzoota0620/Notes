'''rows=int(input("enter rows"))
col=int(input("enter column"))
m=[]
print("enter matrix")
for i in range(rows):
    m1=[]
    for j in range(col):
        if j==0:
            m1.append(int(input()))
        if j==1:
            m1.append(str(input()))
        if j==2:
            m1.append(float(input())) 
    m.append(m1)
print(m)'''
        
      
            
rows=int(input("rows:"))
col=int(input("col"))
m=[]
sum=0
for i in range(rows):
    m1=[]
    for j in range(col):
        n=int(input())
        m1.append(n)
        sum=sum+n
    m.append(m1)
print(m)
print("print row sum",sum)










    
