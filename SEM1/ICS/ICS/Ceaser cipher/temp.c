#include<stdio.h>
#include<string.h>
void main()
{
	FILE *fp,*fp1;
	char plain_text[100];
	char cipher_text[100];
	int key,len,i;
	char ch;

	fp=fopen("Plain_Text.txt","r");

	printf("Enter the amount of shift: ");
	scanf("%d",&key);

	if(fp==NULL)
	{
		printf("File not Found");
	}
	else
	{
		fgets(plain_text,100,fp);
		printf("%s\n",plain_text);

		len=strlen(plain_text);

		//printf("%d",len);

		for(i=0;i<len;i++)
		{
			ch=plain_text[i];

			if(ch>='A' && ch<='Z')
			{
				ch=ch+key;

				if(ch>'Z')
				{
					ch=ch-26;
				}
				cipher_text[i]=ch;
				//printf("%c",ch);
			}
			else if(ch>='a' && ch<='z')
			{
				ch=ch+key;

				if(ch>'z')
				{
					ch=ch-26;
				}
				cipher_text[i]=ch;
				//printf("%c",ch);
			}
			else if(ch==' ')
			{
				cipher_text[i]=' ';
				//printf("%c",ch);
			}
		}
		fp1=fopen("Cipher_Text.txt","w+");
		fprintf(fp1,cipher_text);
	}
}
