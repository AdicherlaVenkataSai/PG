void static updateEnv(char *str, size_t size)
{
 char *tmp;
 tmp=getenv("HOME");
 if(tmp!=NULL)
  {
   strncpy(str,tmp,size-1);
   str[size -1]='\0';
  }
}

int main()
{
	char *str;
	size_t size;
	str="Hello World";
	size=strlen(str);
	updateEnv(str,(size -1));
	printf("\n Tne Enviroment variable copied\n");
	return 0;
}