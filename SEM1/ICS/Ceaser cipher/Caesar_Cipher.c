#include<stdio.h>
#include<string.h>
void main()
{
	char str[100],ch;
	int len,i,key;

	printf("Enter the string to be encrypted: ");
	scanf("%s",&str);

	len=strlen(str);

	printf("Enter the amount of shift: ");
	scanf("%d",&key);

	for(i=0;i<len;i++)
	{
		ch=str[i];

		if(ch>='A' && ch<='Z')
		{
			ch=ch+key;

			if(ch>'Z')
			{
				ch=ch-'Z'+'A'-1;
			}
			str[i]=ch;
		}

		else if(ch>='a' && ch<='z')
		{
			ch=ch+key;

			if(ch>'z')
			{
				ch=ch-'z'+'a'-1;
			}
			str[i]=ch;
		}
	}

	printf("The encrypted text is: %s",str);
}