#include<stdio.h>
#include<stdlib.h>
#define MAXTMP 80
void static foo(void)
{
 char *tmp;
 tmp=(char *)malloc(MAXTMP);
 if(tmp!=NULL)
 *tmp='x';
 free(tmp);
}
int main()
{
foo();
return 0;
}

