#include<stdio.h>
int fun(int n)
{
	if(n<=1)
	return 1;
	if(n%2==0)
	return f(n/2);
	else
	return f(n/2)+f(n/2+1);
}
int main()
{
	printf("%d",f(11));
	return 0;
}
