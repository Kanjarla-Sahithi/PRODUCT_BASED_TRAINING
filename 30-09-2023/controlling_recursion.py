#controlling recursion by 'return condition'
def cse(x):
    if(x==0):
        return 0
    print("Hi:)",x)
    print(cse(x-1))
    print(x)   #backtracking 
cse(4)