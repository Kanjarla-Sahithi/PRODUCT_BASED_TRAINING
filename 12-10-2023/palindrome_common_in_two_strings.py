s1="ababcc"
s2="abccf"

substring1=[]
substring2=[]

for i in range(0,len(s1)):
    for j in range(0,len(s1)):
        substring1.append(s1[j:j+i+1])
for i in range(0,len(s2)):
    for j in range(0,len(s2)):
        substring2.append(s2[j:j+i+1])
        
a1=set(substring1)
b=set(substring2)
a=[]

for i in a1:
    if i in b:
        a.append(i)
print(max(a, key=len))
