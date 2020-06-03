#include<stdio.h>
#include<string.h>
void main()
{
	FILE *fp;
	char cipher[100];
	char plain[100];
	int i,len=0,j;
	char ch;

	fp=fopen("Cipher_Text.txt","r");

	if(fp==NULL)
	{
		printf("File not Found");
	}
	else
	{
		fgets(cipher,100,fp);

		len=strlen(cipher);

		for(i=1;i<=26;i++)
		{
			for(j=0;j<len;j++)
			{
				ch=cipher[j];

				if(ch>='A' && ch<='Z')
				{
					ch=ch-i;

					if(ch<'A')
					{
						ch=ch+26;
					}
					printf("%c",ch);
					//plain[j]=ch;
				}
				else if(ch>='a' && ch<='z')
				{
					ch=ch-i;

					if(ch<'a')
					{
						ch=ch+26;
					}
					printf("%c",ch);
					//plain[i]=ch;
				}
				else if(ch==' ')
				{
					printf("%c",ch);
					//plain[i]=' ';
				}
				else
				{
					printf("%c",ch);
					//plain[i]=ch;
				}
			}
			printf("\n");
		}
	}
}