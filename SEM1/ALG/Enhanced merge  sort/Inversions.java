package a3;
import java.util.Random;
import java.util.Scanner;
import test.EnhancedMerge;
public class Inversions 
{
	public static void main(String[] args)
	{
	Scanner s=new Scanner(System.in);
	System.out.println("enter the array size");
	int size=Integer.parseInt(s.nextLine());
	int Arr_numbers[]= new int[size];
	for(int i=0;i<size;i++)
    {  
		//Arr_numbers[i]=i+1;
 	    Random rand = new Random();
 	    Arr_numbers[i]=rand.nextInt(size);
		 //Arr_numbers[i]=size-i;
		System.out.println(Arr_numbers[i]+"");
    }
	System.out.println("1.O(n^2)\n2.O(nlogn)");
	System.out.println("Enter your choice");
	int choice=Integer.parseInt(s.nextLine());
	switch(choice)
	{
	 case 1:System.out.println("Time Complexity:O(n^2)\n");
	       int i,j,count=0;
	       for(i=0;i<size-1;i++)
	    	 for(j=i+1;j<size;j++)
	    		if(Arr_numbers[i]>Arr_numbers[j])
	    			count++;	
	       System.out.println("InversionsCount:"+count);
	        break;
	 case 2:System.out.println("Time Complexity:O(nlogn)\n");
	       //System.out.println("InversionsCount:"+count);
	       EnhancedMerge ob=new EnhancedMerge();
	       System.out.println("InversionsCount:"+ob.enmerge(Arr_numbers,size));
	       break;
	}
	s.close();
	}
}
