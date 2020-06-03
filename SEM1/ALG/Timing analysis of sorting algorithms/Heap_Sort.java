package test;

public class Heap_Sort 
{
	long swaps=0;
	void maxheapify(int a[], int n, int i)
	{
	    int largest = i,l = (2*i),r = (2*i)+1; 
	    if (l < n && a[l] > a[largest])
	    { largest = l;}
	    if (r < n && a[r] > a[largest])
	    { largest = r;}
	    if (largest != i){
	    	int temp=a[i];
	    	a[i]=a[largest];
	    	a[largest]=temp;
	    	swaps++;
	        maxheapify(a,n,largest);}
	}
	public long Sort(int arr[],int n)
    {
		    for (int i=(n/2);i >= 1; i--)
		        { maxheapify(arr, n, i);}
		     for (int i=n; i>=1; i--)
		     {
		    	 int temp=arr[1];
		    	   arr[1]=arr[i];
		    	   arr[i]=temp;
		    	   swaps++;
		        maxheapify(arr, i, 1);
		     }
		//System.out.println("Swaps:"+swaps);
		     return swaps;
	}
	
}