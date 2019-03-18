## Questions link : https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1

Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/*Complete the function below*/
int findExtra(int a[],int b[],int n)
{
 //add code here.
 int index = 0;
 for (int i = 0;i<n;i++)
 {
     if( a[i] != b[i])
    {
        index = i;
        break;
    }
 }
     return index;
}

## Solutions link : https://practice.geeksforgeeks.org/viewSol.php?subId=4411173&pid=700517&user=VikasViki
