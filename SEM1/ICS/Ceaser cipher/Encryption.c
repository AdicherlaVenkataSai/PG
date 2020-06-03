#include<stdio.h>
#include<string.h>
#include<conio.h>
void main()
{
	FILE *file_read,*file_write;
	char plain_text[100];
	char cipher_text[100];
	int key,length,i;
	char ch;

   	file_read=fopen("plaintext.txt","r");
	printf("Enter the shift value (key):");
	scanf("%d",&key);

	if(file_read==NULL)
	{
		printf("File not Found");
	}
	else
	{
		fgets(plain_text,100,file_read);
		printf("%s\n",plain_text);

		length=strlen(plain_text);

		for(i=0;i<length;i++)
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
			}
			else if(ch>='a' && ch<='z')
			{
				ch=ch+key;

				if(ch>'z')
				{
					ch=ch-26;
				}
				cipher_text[i]=ch;
			}
			else if(ch==' ')
			{
				cipher_text[i]=' ';
			}
		}
		file_write=fopen("ciphertext.txt","w+");
		fprintf(file_write,cipher_text);
		printf("Succesfully encrpted");
    } 
}
