package test;
public class Bubble_Sort
{
    public long Sort(int arr[],int n)
    {
        long swaps=0;
    	for(int i=0;i<n;i++)
    	{
    		for(int j=1;j<n-i;j++)
    		{
    		 if(arr[j-1]>arr[j])
    		 {
    			 int temp=arr[j-1];
    			 arr[j-1]=arr[j];
    			 arr[j]=temp;
    			 swaps++;
    		 }
    		}
    	}
    	//System.out.println("Swaps:"+swaps);
    	return swaps;
    }
}