
'''words = []
file = open("demo_file.py","r")
data = file.readlines()
for line in data:
 for word in line.split():
     words.append(word)
count = {}
for i in words:
   if i in count :
      count[i] += 1
   else:
      count[i] = 1
f1=open("inputfile.txt","w")
for i in list(sorted(count.keys())):
    p=(i+ " : "+str(count[i]))
    f1.write(str(p))
    print('\n')

fname = input("Enter file name: ")
word=input("Enter word to be searched:")
words=[]
k=0
file=open(fname, 'r')
data = file.readlines()
for line in data:
 for word in line.split():
     words.append(word)  
print(word)
for i in words:
   if(i==word):
       k=k+1
print("Occurrences of the word:")
print(k)

'''

def char_count(strr,c):
    count=0
    
    strr=strr.lower()
    c=c.lower()
    for word in strr:
        if word==c:
            count+=1
    return count
name=input('enter file name:')
c=input('enter character to be count:')
cc=0
f=open(name)
content=f.read()
output=char_count(content,c)
print('File has',output,'no. of ',c,'character') 

'''def word_count(str):
    words=str.lower().split()
    counts=dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
f = open("demo_file.py","r")
content = f.read()
output=word_count(content)
f1=open('output.txt','w')
for key in list(sorted(output.keys())):
    f1.write(str(key+':'+str((output[key]))))
    f1.write('\n')
f1.close()
f.close()'''
              
    
        
        
