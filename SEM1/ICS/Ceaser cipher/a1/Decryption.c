#include<stdio.h>
#include<string.h>
void main()//Decryption using Ceasar cipher
{
	FILE *f1,*f2;
	char ch,cipher[1000],plain[1000];
	int key,l,i;
	f1=fopen("Cipher_Text.txt","r");
	printf("\n -----Decryption based on Ceasar Cipher(shift cipher)---- \n");
	printf("\nEnter the shift value(key):");
	scanf("%d",&key);
	if(f1==NULL)
	{
		printf("OOPs!File not Found");
	}
	else
	{
		fgets(cipher,100,f1);
	//	printf("%s\n",cipher);
		l=strlen(cipher);
        for(i=0;i<l;i++)
		{
			ch=cipher[i];

			if(ch>='A' && ch<='Z')
			{
				ch=ch-key;

				if(ch<'A')
				{
					ch=ch+26;//ch=ch+('Z'+'A'-1);
				}
				plain[i]=ch;
			}
			else if(ch>='a' && ch<='z')
			{
				ch=ch-key;

				if(ch<'a')
				{
					ch=ch+26;//ch=ch+('z'+'a'-1);
				}
				plain[i]=ch;
			}
			else if(ch==' ')
				plain[i]=' ';
			else
			plain[i]=ch;
		}
	//	printf("%s",plain);
		f2=fopen("Plain_Text1.txt","w+");
		fprintf(f2,plain);
		printf("Successfully Decrypted");
		
	}
}
