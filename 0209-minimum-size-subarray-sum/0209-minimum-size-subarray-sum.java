class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int minLength = Integer.MAX_VALUE;
        int currentSum = 0;
        int left = 0;

        for(int right = 0; right < n; right++)
        {
            currentSum = currentSum + nums[right];
            while (currentSum >= target){
                minLength = Math.min(minLength, right-left +1);
                currentSum -= nums[left];
                left++;
            }
        }
        return minLength == Integer.MAX_VALUE ? 0 : minLength;
    }
}