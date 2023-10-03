//Check the whether given number is power of 2
#include<stdio.h>
main()
{
	int num,count=0;
	printf("Enter the n value");
	scanf("%d",&num);
	while(num)
	{
		count++;
		num=num&(num-1);
	}
	if(count==1)
	{
		printf("True");	
	}
	else
	{
		printf("False");
	}
}
