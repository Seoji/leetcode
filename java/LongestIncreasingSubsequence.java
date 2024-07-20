// Runtime: 49ms
// Memory Usage: 44.7MB

class Solution{
    public int lengthOfLIS(int[] nums) {
        int[] dpArr = new int[nums.length];
        Arrays.fill(dpArr, 1);

        for(int i = 1; i < nums.length; i++) {

            for(int j = 0; j < i; j++) {

                if(nums[j] < nums[i]) {

                    dpArr[i] = Math.max(
                        dpArr[i], 
                        dpArr[j] + 1
                    );
                }
            }
        }
        return Arrays.stream(dpArr).max().getAsInt();
}
    
}
