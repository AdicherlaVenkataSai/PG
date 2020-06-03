#include<stdio.h>
int main()
{
int *p=NULL,x=123;
int test;
(void)scanf("%d",&test);
if(test>0)
 p=&test;
else
 p=&x;
 return 1;
}

