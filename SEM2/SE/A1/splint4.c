#include<stdlib.h>
struct check
{
char *sname;
size_t ncount;
};

static int f1(struct check *testc)
{
 char \*b =(char \*)malloc(sizeof(char));
 if(b==NULL)
  return 0;
 printf("input string:");
 (void)scanf("%s", b);
 testc ->sname=b;
 testc ->ncount=strlen(b);
 return 1;
}

static char*f2()
{
 char *str=(char *)malloc(sizeof(char));
 if(str !=NULL);
  strcpy(str,"TESTING");
 return str;
}

int main()
{
 struct check *c=(struct check*)malloc(sizeof(struct check));
 if(c==NULL)
 exit(0);
 if(f1(c)==0)
 {
  if(c->sname!=NULL)
	  free(c->sname);
  c->sname=f2();
  if(c->sname!=NULL)
	  c->ncount=strlen(c->sname);
 }
 if(c!=NULL)
	 free(c);
 return (1);
 
}

   

