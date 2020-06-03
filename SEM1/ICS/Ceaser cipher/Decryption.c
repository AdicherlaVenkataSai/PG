#include<stdio.h>
#include<string.h>
void main()
{
	FILE *fp,*fp1;
	char cipher_text[100];
	char plain_text[100];
	int key,len,i;
	char ch;

	fp=fopen("Cipher_Text.txt","r");

	printf("Enter the amount of shift: ");
	scanf("%d",&key);

	if(fp==NULL)
	{
		printf("File not Found");
	}
	else
	{
		fgets(cipher_text,100,fp);
		printf("%s\n",cipher_text);

		len=strlen(cipher_text);

		for(i=0;i<len;i++)
		{
			ch=cipher_text[i];

			if(ch>='A' && ch<='Z')
			{
				ch=ch-key;

				if(ch<'A')
				{
					ch=ch+26;
				}
				plain_text[i]=ch;
			}
			else if(ch>='a' && ch<='z')
			{
				ch=ch-key;

				if(ch<'a')
				{
					ch=ch+26;
				}
				plain_text[i]=ch;
			}
			else if(ch==' ')
			{
				plain_text[i]=' ';
			}
		}
		fp1=fopen("Plain_Text.txt","w+");
		fprintf(fp1,plain_text);
	}
}
