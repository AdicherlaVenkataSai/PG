#include<stdio.h>
#include<string.h>	
void main()//Encryption using Ceasar cipher
{
	FILE *f1,*f2;//pointers used to hold the file(read,write)								
	char ch,plain[1000],cipher[1000];//plain and cipher text content
	int key,l,i;//l=holds the length of the text
						
	f1=fopen("Plain_Text.txt","r");
	printf("\n -----Encryption based on Ceasar Cipher(shift cipher)---- \n");
	if(f1==NULL)//checks whether the file is present or not	
	{
	 printf("OOPs! File not Found");
    }
	else
	{
		printf("\nEnter the shift value(key):");
		scanf("%d",&key);
		fgets(plain,1000,f1);//char *fgets(char *str, int n, FILE *stream) 
	//	printf("Plain Text : %s \n",plain);
        l=strlen(plain);
		for(i=0;i<l;i++)
		{
			ch=plain[i];

			if(ch>='A' && ch<='Z')
			{
				ch=ch+key;
				if(ch>'Z')
				ch=ch-26;//ch=ch-('Z'+'A'-1);
				cipher[i]=ch;
			}
			else if(ch>='a' && ch<='z')
			{
				ch=ch+key;
				if(ch>'z')
					ch=ch-26;//ch=ch-('z'+'a'-1);
				cipher[i]=ch;
			}
			else if(ch==' ')
				cipher[i]=' ';
			else
			  cipher[i]=ch;
		}
		//printf("Cipher Text : %s",cipher);
		f2=fopen("Cipher_Text.txt","w+");
		fprintf(f2,cipher);
		printf("Successfully Encrypted");
	}
}
