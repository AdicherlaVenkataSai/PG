#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

void freq(int index,char *c)
{   
	int k=abs(index-18);
	printf("key is:%d",k);
	char store[1000]={'\0'};
	int i;
	for(i=0;i< strlen(c);i++)
	{
	    if(islower(c[i]))
		store[i]=((c[i]-k-122)%26)+122;
		else if(isupper(c[i]))
		store[i]=((c[i]-k-90)%26)+90;
		else
		store[i]=c[i];	 
	}
	printf("\n %s \n",store);
}
int main()
{
	char c[1000];
	FILE *ptr;
	ptr=fopen("encrypttext.txt","r");
	if(ptr==NULL)
	{
		printf("OOPs!file not found..");
	}
	else
	{
	int f[26]={0},i,l;
	fgets(c,1000,ptr);
	printf("%s",c);
	l=strlen(c);
	for(i=0;i<l;i++)
	{
	    if(islower(c[i]))
		++f[(c[i])% 97];
		if(isupper(c[i]))
		++f[(c[i])% 65];
	}
	printf("\n");
	for(i=0;i<26;i++)
	{
		printf("%d:",f[i]);
	}
    printf("\n");
    while(1)
    {
    	int max=0,index=0,var=1,i;
    	for(i=0;i<26;i++)
    	{
    		if(max<f[i])
    		{
    			max=f[i];
    			index=i;
			}
		}
	printf("max %d ,index %d \n",max,index);
	freq(index,c);
	f[index]=0;
	scanf("%d",&var);
	if(var)
	{
		exit(1);
	}
	}
	}
	return 0;
}


