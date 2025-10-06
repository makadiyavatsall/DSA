public class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        // Initialize max, min, and result with the first element
        int maxProd = nums[0];
        int minProd = nums[0];
        int result = nums[0];

        // Traverse from the second element
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            // If number is negative, swap maxProd and minProd
            if (num < 0) {
                int temp = maxProd;
                maxProd = minProd;
                minProd = temp;
            }

            // Update maxProd and minProd for current number
            maxProd = Math.max(num, maxProd * num);
            minProd = Math.min(num, minProd * num);

            // Update result
            result = Math.max(result, maxProd);
        }

        return result;
    }
}
