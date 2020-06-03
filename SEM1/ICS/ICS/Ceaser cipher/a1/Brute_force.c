#include<stdio.h>
#include<string.h>
void main()//In the brute force attack, we check the given cipher text by shifting it (either to left or Right)
//all possiblites are verified from 1 to 25(for the last time we end up with the same input)
//From the possiblities we choose the text which seems meaningful,plaintext.
{
	FILE *fp;
	char ch,cipher[1000],plain[1000];
	int l,i,j;	
//	printf("\nEnter file name to be Decrypted : ");
	fp=fopen("Cipher_Text.txt","r");
	if(fp==NULL)
		printf("OOPs!File not Found");
	else
	{
		fgets(cipher,1000,fp);
		l=strlen(cipher);
		printf("\n\n\nChoose the meaningful text from below...\n");
		for(i=1;i<=26;i++)
		{
			for(j=0;j<l;j++)
			{
				ch=cipher[j];
				if(ch>='A' && ch<='Z')
				{
					ch=ch-i;
					if(ch<'A')
						ch=ch+26;//ch=ch-('Z'+'A'-1);

					printf("%c",ch);
				}
				else if(ch>='a' && ch<='z')
				{
					ch=ch-i;
					if(ch<'a')
						ch=ch+26;//ch=ch-('z'+'a'-1);

					printf("%c",ch);
				}
				else if(ch==' ')
					printf("%c",ch);
				else
					printf("%c",ch);
			}
			printf("\n");
		}
	}
}
