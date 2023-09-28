/*Question
   1 0 0 1
   0 1 0 1
   0 0 1 1
   0 0 0 1
 
OUTPUT:
    1's vertical count=1
	1's horizontal count =0
	1's left diagonal count=1
	1's right diagonal count=0
	0's vertical count=0
	0's horizontal count =0
	0's left diagonal count=0
	0's right diagonal count=0
*/
#include<stdio.h>
void main()
{
	int arr[20][20],i,j,n,flag1,flag2,flag3,flag4;
	int onesVertical = 0;
    int onesHorizontal = 0;
    int onesLeftDiagonal = 0;
    int onesRightDiagonal = 0;

    int zerosVertical = 0;
    int zerosHorizontal = 0;
    int zerosLeftDiagonal = 0;
    int zerosRightDiagonal = 0;
    
	printf("Enter n value :");
	scanf("%d",&n);
	
	
	for(i=1; i<=n; i++)
	{
		for(j=1; j<=n; j++)
		{
			scanf("%d",&arr[i][j]);
		}
	}
	
	printf("The matrix is :\n");
	for(i=1; i<=n; i++)
	{
		for(j=1; j<=n; j++)
		{
			printf("%d  ",arr[i][j]);
		}
		printf("\n");
	}
	
	for(j=1; j<=n; j++)
	{
		flag1=arr[1][j];
		for(i=1; i<=n; i++)
		{
			if(arr[i][j]!=flag1)
			{
			flag1=100;
			break;
		    }
		}
	if(flag1!=100)
	{
		if(flag1==1)
		{
			onesVertical++;			
		}
		else
		{
			zerosVertical++;
		}
	}
    }
	printf("The Ones Vertical:%d\n",onesVertical);
	printf("The Zeros Vertical:%d\n",zerosVertical);
	
		for(i=1; i<=n; i++)
	{
		flag2=arr[i][1];
		for(j=1; j<=n; j++)
		{
			if(arr[i][j]!=flag2)
			{
			flag2=100;
			break;
		    }
		}
	if(flag2!=100)
	{
		if(flag2==1)
		{
			onesHorizontal++;			
		}
		else
		{
			zerosHorizontal++;
		}
	}
    }
	printf("The Ones Horizontal:%d\n",onesHorizontal);
	printf("The Zeros Horizontal:%d\n",zerosHorizontal);
	
		flag3=arr[1][1];
		for(i=1; i<=n; i++)
		{
			if(arr[i][i]!=flag3)
			{
			flag3=100;
			break;
		    }
		}
		
	if(flag3!=100)
	{
		if(flag3==1)
		{
			onesLeftDiagonal++;			
		}
		else
		{
			zerosLeftDiagonal++;
		}
	}
	printf("The Ones Left Diagonal:%d\n",onesLeftDiagonal);
	printf("The Zeros Left Diagonal:%d\n",zerosLeftDiagonal);
	
	flag4=arr[1][4];
	for(i=1; i>=n; i++)
	{
		for(j=1; j>=n; j++)
		{
			if(arr[i+1][j-1]!=flag4)
			{
			flag4=100;
			break;	
			}
		}
		if(flag4!=100)
		{
			if(flag4==1)
			{
				onesRightDiagonal++;			
			}
			else
			{
				zerosRightDiagonal++;
			}
		}
	}
	
	printf("The Ones Right Diagonal:%d\n",onesRightDiagonal);
	printf("The Zeros Right Diagonal:%d\n",zerosRightDiagonal);
}
