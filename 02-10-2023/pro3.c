#include<stdio.h>
int fun(int x, int y)
{
	if(y==0)
	return 0;
	else
	return (x+fun(x,y-1));	
}
int fun2(int a, int b)
{
	if(b==0)
	return 1;
	else
	return fun(a,fun2(a,b-1));
}
main()
{
	int f;
	f=fun2(2,4);
	printf("%d",f);
	
}
