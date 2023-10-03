#include<stdio.h>
int fun(int n)
{
	if(n==0)
	return;
	
	printf("%d",n%2);
	fun(n/2);
}
main()
{
	int f;
	f=fun(25);
	printf("%d",f);
	
}
