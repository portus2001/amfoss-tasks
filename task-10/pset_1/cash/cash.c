#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void){
float count=0;
float change;
do
{
  change=get_float("Cash Owed: ");
}
while (change<0);

change*=100;
change=round(change);


while(change>0)
{
    if(change>=25)
    {
        change-=25;
        count+=1;
    }
    else if(change>=10)
    {
        change-=10;
        count+=1;
    }
    else if(change>=5)
    {
        change-=5;
        count+=1;
    }
    else
    {
        change-=1;
        count+=1;
    }
}

printf("Total coins: %f\n", count);
}
