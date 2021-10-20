int comparer(const void* a, const void* b)
{
    int int_a = *((int*)a);
    int int_b = *((int*)b);
    if(int_a == int_b) return 0;
    return int_a < int_b ? -1 : 1;
}

int findTriplets(int array[], int n)
{
    qsort(array, n, sizeof(int), comparer);
    for(int i = 0 ; i < n ; ++i){
        int left = i + 1, right = n - 1;
        while(left < right){
            int sum = array[ i ] + array[ left ] + array[ right ];
            if(sum == 0)
                return 1;
            else if(sum < 0)
                ++left;
            else
                --right;
        }
    }
    return 0;
}