#include<stdio.h>
int fun(int x, int y)
{
	if(x==0)
	return y;
	else
	return fun(x-1, x+y);
}
main()
{
	int f;
	f=fun(4,3);
	printf("%d",f);
}
