#include<stdio.h>
#include<stdlib.h>
char static *foo()
{
	char ch = 'x';
	return (char *)ch;
}
int main()
{
char *p;
int x;
char s;
printf("Pl e a s e e n t e r the v al u e o f x \n ");
(void)scanf("%d",&x);
if(x==0)
p=0;
else
p=foo();
if(x!=0)
if(p!=NULL)
s=*p;
else
printf(" The v al u e o f x e n t e r e d i s %d\n ",x);
free(p);
return 0;
}

