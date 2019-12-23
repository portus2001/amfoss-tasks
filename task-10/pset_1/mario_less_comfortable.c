#include<stdlib.h>
#include<stdio.h>
#include<cs50.h>

int main()
{
    int i, j, height;


    do
    {
        printf("Specify the height of the pyramid: ");
        scanf("%d",&height);
    }
    while (height < 0 || height > 23);


    for(i=2; i<=height+1; i++)
    {

        for(j=i; j<height+1; j++)
        {
            printf(" ");
        }

        for(j=1; j<=i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}