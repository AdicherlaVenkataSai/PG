//Railfence Cipher
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAXSIZE 128
char PT[MAXSIZE],CT[MAXSIZE],temp_CT[MAXSIZE][MAXSIZE];
int KEY,SIZE;
void frameMsg()
{
	int i,len;
	FILE *fp;
	//printf("Message?  ");
	//scanf("%s",PT);
	//gets(PT);
	//get Message from file only
	fp = fopen("file.txt","r");
	if(fp == NULL)
	{
		printf("ERROR!! ");
		exit(0);
	}
	printf("\nReading the file file.txt" ) ;
	while( fgets (PT,MAXSIZE, fp ) != NULL )
         
	printf("Key?  ");
	scanf("%d",&KEY);
	//Mak PT in proper format
	len = strlen(PT);
	if((len%KEY) != 0)
	{
		for(i=0;i<KEY-(len%KEY);i++)
			PT[len+i] = '_';
	}
	PT[len+i] = '\0';
	len = strlen(PT);
	for(i=0;i<len;i++)
	{
		if(PT[i] == ' ')
			PT[i] = '_';
	}
	SIZE = len;
//	printf("Plain Text : %s",PT);
}
void decrpytion()
{
	int k=0,i,j;
	char PT_dec[MAXSIZE];
	for(i=0;i<KEY;i++)
	{
		for(j=0;j<(SIZE/KEY);j++)
			temp_CT[i][j] = CT[k++];
	}
	
	k=0;
	for(i=0;i<(SIZE/KEY);i++)
	{
		for(j=0;j<KEY;j++)
			PT_dec[k++] = temp_CT[j][i];
	}
	printf("\nDecrypted : %s\n",PT_dec);
}
void encryption()
{
	int i,j,k=0;
	for(i=0;i<(SIZE/KEY);i++)
	{
		for(j=0;j<KEY;j++)
			temp_CT[i][j] = PT[k++];
	}
	k=0;
	for(i=0;i<KEY;i++)
	{
		for(j=0;j<(SIZE/KEY);j++)
			CT[k++] = temp_CT[j][i];
	}
	printf("\nCipher Text : %s",CT);
}
int main()
{
	int choice;
	do
	{
		printf("\n\t\t $$ M E N U $$\n 1) Encryption\n 2) Decryption \n 0) Exit\n   Enter Your Choice    ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1: frameMsg();  
					encryption(); 
					break;
			case 2: frameMsg();  
					decrpytion(); 
					break;
			case 0: break;
			default: printf("\nBad Choice\n");
		}
	}while(choice !=0);
	return 0;
}

