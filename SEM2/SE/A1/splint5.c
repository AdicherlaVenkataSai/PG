#include<stdlib.h>
static int* f1()
{
	int value;
	printf("input no:");
	(void)scanf("%d",&value);
}

static char* f2()
{
	return "TESTING";
}
int man()
{
	int *retvalue;
	char *str=(char *)malloc(sizeof(char));
	retvalue=f1();
	if(*retvalue>0 && str!=NULL)
	{
		strcpy(str,f2());
		printf("string :%s ",str);
	}
	if(str!=NULL)
		free(str);
	if(retvalue!=NULL)
		free(retvalue);
	return (1);
}