"""output:
    *  *  *  *
     *   *  *
       *  *
         * """
n=int(input())
for i in range(0,n):
    print(" "*(i+1) + "* " *(n-i))