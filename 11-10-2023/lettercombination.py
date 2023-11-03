def letterCombinations(digits):
    n=len(digits)
    if n==0:
        return []
    d={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
    res=[]
    def backtrack(r,curstr):
        if len(digits)==len(curstr):
            res.append(curstr)
            return
        for i in d[digits[r]]:
            backtrack(r+1,curstr+i)
    backtrack(0,"")
    return res
digits="23"
result=letterCombinations(digits)
print(result)


       




     
        
