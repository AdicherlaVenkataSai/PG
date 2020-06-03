package a2;
import java.util.Scanner;
public class Pow {
   public static void main(String[] args) 
	{
		Scanner s=new Scanner(System.in);
		System.out.println("Enter the x value:");
		int x=Integer.parseInt(s.nextLine());
		System.out.println("Enter the  y value:");
		int y=Integer.parseInt(s.nextLine());
		System.out.println("1.Normal Method:\n2.Bin Exponent:");
		System.out.println("Enter the choice:");
		int choice=Integer.parseInt(s.nextLine());
		long start_time,end_time,microseconds;
		switch(choice)
		{
		case 1:System.out.println("Normal Method");
		       start_time = System.currentTimeMillis();
		       //int result=power(x,y);
		       double result=Math.pow(x,y);//Math class is available in java.lang package(default package)
		       System.out.println("x^y:"+result);
		       end_time = System.currentTimeMillis();
		       microseconds = (end_time - start_time) *1000;
	           System.out.println("time taken is:"+microseconds+" microseconds");
		       break;
		case 2:System.out.println("Bin Exponent");
		       start_time = System.nanoTime();
		       int result1=binexponent(x,y);
		       System.out.println("x^y:"+result1);
		       end_time = System.nanoTime();
		       microseconds = (end_time - start_time) /1000;
	           System.out.println("time taken is:"+microseconds+" microseconds");
	       break;
		}
		
		s.close();
	 }
	  /*static int power(int x, int y) 
	    { 
	        if (y == 0) 
	            return 1; 
	        else if (y % 2 == 0) 
	            return power(x, y / 2) * power(x, y / 2); 
	        else
	            return x * power(x, y / 2) * power(x, y / 2); 
	    }*/
   static int binexponent(int x,int y)
	   {   
		  int ans=1;
		  int q=y/2;
		  int r=y%2;
		  if(r==1)
			  return ans*x;
		  else  if(q==0)
			  return ans;
			  y=q;
		      x=x*x;
		 return  binexponent(x,y);    
	  }
	  
}