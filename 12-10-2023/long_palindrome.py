s="aacabdkacaa"
lis=[]
st=""
for i in range(len(s)):
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            st=s[i:j+1]
            if st==st[::-1]:
                lis.append(st)
        st=""
        j-=1
if len(s)==1:
    print(s)
elif not lis:
    print(s[0])
else:
    print(max(lis, key=len))

        
