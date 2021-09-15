class Solution {
    findTriplets(array, n)
    {
        array.sort(function(a, b){ return a - b });
        for(let i = 0 ; i < n ; ++i){
            let left = i + 1, right = n - 1;
            while(left < right){
                let sum = array[ i ] + array[ left ] + array[ right ];
                if(sum === 0)
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