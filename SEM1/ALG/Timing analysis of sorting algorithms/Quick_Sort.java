package test;

public class Quick_Sort 
{
	long  swaps;
	/*int partition(int a[], int lb, int ub) 
	    { 
	        int pivot = a[lb];  
	        int i = lb,j=ub; 
	        while(i<j)
			{
	    		do
	    		{
	    			i++;
	    		}while(a[i]<=pivot);
	    		do
	    		{
	    			j--;
	    		}while(a[j]>pivot);
	    		if(i<j)
	    		{
	    			int temp=a[i];
	    			a[i]=a[j];
	    			a[j]=temp;
	    			swaps++;
	    		}
	    		}
	  
	        int temp=a[lb];
			a[lb]=a[j];
			a[j]=temp;
			swaps++;
			return j;
	    } 
	    public void Sort(int arr[], int lb, int ub) 
	    { 
	        if (lb < ub) 
	        { 
	            int j= partition(arr,lb,ub);  
	            Sort(arr, lb, j); 
	            Sort(arr, j+1, ub); 
	        } 
	        System.out.println("Swaps:"+swaps);
	    }*/	  
	int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];  
        int i = (low-1); // index of smaller element 
        for (int j=low; j<high; j++) 
        { 
            // If current element is smaller than or 
            // equal to pivot 
            if (arr[j] <= pivot) 
            { 
                i++; 
  
                // swap arr[i] and arr[j] 
                int temp = arr[i]; 
                arr[i] = arr[j]; 
                arr[j] = temp; 
                swaps++;
            } 
        } 
  
        // swap arr[i+1] and arr[high] (or pivot) 
        int temp = arr[i+1]; 
        arr[i+1] = arr[high]; 
        arr[high] = temp; 
        swaps++;
        return i+1; 
    } 
	public long Sort(int arr[], int low, int high) 
    { 
        if (low < high) 
        { 
            /* pi is partitioning index, arr[pi] is  
              now at right place */
           int pi = partition(arr, low, high); 
  
            // Recursively sort elements before 
            // partition and after partition 
            Sort(arr, low, pi-1); 
            Sort(arr, pi+1, high); 
        } 
      //  System.out.println("Swaps:"+swaps);
        return swaps;
    } 
  
}