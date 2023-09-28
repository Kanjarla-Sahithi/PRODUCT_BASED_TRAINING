#include<stdio.h>
void main()
{
	short n;
	printf("Enter no of lemons:");
	scanf("%hi",&n);
	int m=(n>=0)?sizeof(n)==2?n<=21?printf("%hi are needed to buy",21-n):printf("%hi are extra",n-21):-1:-1;
	m!=-1?:(printf("Invalid Input"));
		
}
