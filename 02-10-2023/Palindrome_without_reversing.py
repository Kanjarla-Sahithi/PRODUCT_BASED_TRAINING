#palindrome without reversing the string
"""s=input()
i=0
j=len(s)-1
while i<=j:
    if(s[i]!=s[j]):
        print("It is not palindrome")
        break
    else:
        i=i+1
        j=j-1
else:
    print("Palindrome")"""

#using function
"""def palindrome(s):
    i=0
    j=len(s)-1
    while i<=j:
        if(s[i]!=s[j]):
            return "Not a palindrome"
        else:
            i=i+1
            j=j-1
        return "Palindrome"
s=input()
print(palindrome(s))"""
#using recursion
def palindrome(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return palindrome(s,i+1,j-1)
s=input()
print(palindrome(s,0,len(s)-1))

    
        
    
            
                
                
            
            
            
