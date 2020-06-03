package assignmet1;
import java.util.*;
import test.*;
public class TimingAnalysis
{ 
public static void main(String args[])throws Exception
{ 
	Scanner s=new Scanner(System.in);
	System.out.println("Enter the value for n(Numbers to be Generated): ");
	int n=Integer.parseInt(s.nextLine());
	System.out.println("----------");
	  System.out.println("1.Sorted\n2.Random\n3.Reverse Sorted");
	  System.out.println("----------");
	  System.out.println("Enter your choice:");
	  System.out.println("----------");
	  int choice=Integer.parseInt(s.nextLine());
	  int Arr_numbers[]= new int[100000];
	  int i,lb=0;
	  switch(choice)
	   {
	  case 1:  System.out.println("Sorted Order");
	           System.out.println("----------");
	           for(i=0;i<n;i++)
	           {
	        	   Arr_numbers[i]=i+1;
	        	   System.out.println(Arr_numbers[i]+"");
	           } break;
	  case 2:  System.out.println("Random");
	           System.out.println("----------");
	           for(i=0;i<n;i++)
	           {
	        	   Random rand = new Random();
	        	   Arr_numbers[i]=rand.nextInt(n);
	        	   //Arr_numbers[i]=(int)Math.random();
	        	   System.out.println(Arr_numbers[i]+"");
	           }break;
	  case 3:  System.out.println("Reverse Sorted");
	           System.out.println("----------");
	           for(i=0;i<n;i++)
	           {
	        	   Arr_numbers[i]=n-i;
	        	   System.out.println(Arr_numbers[i]+"");  
	           }break;
	  default:
	        System.out.println("Invalid Choice...");
	 }
	System.out.println("----------");
  	System.out.println("choose the sorting algorithm:");
  	System.out.println("----------");
	System.out.println("1.BubbleSort\n2.MergeSort\n3.QuickSort\n4.HeapSort\n5.InsertionSort");
	System.out.println("----------");
	System.out.println("Enter your choice:");
	int choice1=Integer.parseInt(s.nextLine());
	long start_time,end_time,microseconds;
	switch(choice1)
	   {
	        case 1: 
	        	//Best case : When array is already sorted.
	        	//Worst case: when the array is reverse sorted.
	        	start_time = System.currentTimeMillis();//System.nanoTime();
	        	System.out.println("-----BubbleSort-----");
	        	Bubble_Sort bs = new Bubble_Sort();
	        	System.out.println("Swaps:"+bs.Sort(Arr_numbers,n));
	        	end_time = System.currentTimeMillis();//System.nanoTime();
	        	microseconds = (end_time - start_time) *1000;
	        	System.out.println("time taken is:"+microseconds+" microseconds");
		        break;
	        case 2:
	        	start_time = System.currentTimeMillis();//System.nanoTime();
	        	System.out.println("-----MergeSort-----");
	        	Merge_Sort ms=new Merge_Sort();
	        	System.out.println("Swaps:"+ms.Sort(Arr_numbers,lb,n));
	        	end_time = System.currentTimeMillis();//System.nanoTime();
	        	microseconds = (end_time - start_time) *1000;
	        	System.out.println("time taken is:"+microseconds+" microseconds");
		        break;
     	    case 3:
     	    	//The performance of the quick sort depends the pivot choosen 
     	    	start_time =System.currentTimeMillis();// System.nanoTime();//
	        	System.out.println("-----QuickSort-----");
	        	Quick_Sort qs=new Quick_Sort();
	        	System.out.println("Swaps:"+qs.Sort(Arr_numbers,lb,n));
	        	end_time = System.currentTimeMillis();//System.nanoTime();
	        	microseconds = (end_time - start_time) *1000;
	        	System.out.println("time taken is:"+microseconds+" microseconds");
		        break;
	        case 4:
	        	start_time =System.currentTimeMillis();// System.nanoTime();
	        	System.out.println("-----HeapSort-----");
	        	Heap_Sort hs=new Heap_Sort();
	        	System.out.println("Swaps:"+hs.Sort(Arr_numbers,n));
	        	end_time = System.currentTimeMillis();//System.nanoTime();
	        	microseconds = (end_time - start_time) *1000;
	        	System.out.println("time taken is:"+microseconds+" microseconds");
		        break;
	        case 5:
	        	//Best case : when array is already sorted.
	        	//Worst case: when the array is reverse sorted.
	        	start_time = System.currentTimeMillis();//System.nanoTime();
	        	System.out.println("-----InsertionSort-----");
	        	Insertion_Sort is=new Insertion_Sort();
	        	System.out.println("Swaps:"+is.Sort(Arr_numbers,n));
	        	end_time = System.currentTimeMillis();//System.nanoTime();
	        	microseconds = (end_time - start_time) *1000;
	        	System.out.println("time taken is:"+microseconds+" microseconds");
		        break;
	         default:System.out.println("Invalid Choice...");
	   }
	 s.close();
    }
   
}



