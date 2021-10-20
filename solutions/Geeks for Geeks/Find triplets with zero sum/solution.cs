class Solution
{
    public bool findTriplets(int[] array, int n)
    {
        Array.Sort(array);
        for(int i = 0 ; i < n ; ++i){
            int left = i + 1, right = n - 1;
            while(left < right){
                int sum = array[ i ] + array[ left ] + array[ right ];
                if(sum == 0)
                    return true;
                else if(sum < 0)
                    ++left;
                else
                    --right;
            }
        }
        return false;
    }
}