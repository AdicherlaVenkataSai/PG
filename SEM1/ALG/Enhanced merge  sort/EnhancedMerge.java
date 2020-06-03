package test;

public class EnhancedMerge 
{   
	int count=0;
	public int enmerge(int arr[],int n)
	{   
		
		System.out.println("-------------");
		 int temp[] = new int[n]; 
		return mergeSort(arr,temp,0,n- 1);  
	}
	 public  int mergeSort(int arr[], int temp[], int left, int right) 
	    { 
	        if (right > left) 
	        { 
	           int  mid = (right + left) / 2; 
	            mergeSort(arr, temp, left, mid); 
	            mergeSort(arr, temp, mid + 1, right); 
	            merge(arr, temp, left, mid + 1, right); 
	        } 
	        //count++;
	        return count; 
	    }
	 public int merge(int arr[], int temp[], int left, int mid, int right) 
	    { 
	        int i=left,j=mid,k=left;        
     while ((i <= mid - 1) && (j <= right)) { 
         if (arr[i] <= arr[j]) { 
             temp[k++] = arr[i++]; 
         } 
         else { 
             temp[k++] = arr[j++]; 
             count+=(mid-i); 
         } 
     } 
     while (i <= mid - 1)
         temp[k++] = arr[i++];
     while (j <= right) 
         temp[k++] = arr[j++]; 
     for (i = left; i <= right; i++) 
         arr[i] = temp[i];
     return count; 
 }
	/*void merge(int arr[], int lb, int mid, int ub)    	  
	{
	int n1 = mid - lb + 1; 
        int n2 = ub - mid; 
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
            count+=(mid - i); 
            
        } 
       while (i < n1) 
        { 
            arr[k] = L[i]; 
            i++; 
            k++; 
         
        } 
         while (j < n2) 
        { 
            arr[k] = R[j]; 
            j++; 
            k++; 
           
        } 
         
    } 
public int enmerge(int arr[], int lb, int ub) 
{   
    if (lb<ub) 
    { 
        int mid = (lb+ub)/2; 
       count= enmerge(arr,lb,mid); 
       count+= enmerge(arr,mid+1,lb);  
       merge(arr,lb,mid,ub); 
    } 
    return count;*/
}

