package test;
public class Merge_Sort
{    long swaps=0;
	void merge(int arr[], int lb, int mid, int ub)    	  
		{
		    int n1 = (mid -lb)+ 1; 
	        int n2 = (ub-mid); 
	        //Creating  temporary arrays
	        int L[] = new int [n1]; 
	        int R[] = new int [n2]; 
	        //Copying data to temporary arrays
	        for (int i=0; i<n1; ++i) 
	            L[i] = arr[lb+ i]; 
	        for (int j=0; j<n2; ++j) 
	            R[j] = arr[mid +1+ j]; 
	        int i = 0, j = 0;
	        		int k = lb;  
	        while (i < n1 && j < n2) 
	        { 
	            if (L[i] <= R[j]) 
	            { 
	                arr[k] = L[i]; 
	                i++;  
	            } 
	            else
	            { 
	                arr[k] = R[j]; 
	                j++;
	            } 
	            k++; 
	            swaps++;
	        } 
	       while (i < n1) 
	        { 
	            arr[k] = L[i]; 
	            i++; k++;
	        } 
	         while (j < n2) 
	        { 
	            arr[k] = R[j]; 
	            j++;k++; 
	        }
	    } 
	public long Sort(int arr[], int lb, int ub) 
    {   
        if (lb<ub) 
        { 
            int mid = (lb+ub)/2; 
            Sort(arr,lb,mid); 
            Sort(arr,mid+1,lb);  
            merge(arr,lb,mid,ub); 
        } 
        return swaps;
    }
}
