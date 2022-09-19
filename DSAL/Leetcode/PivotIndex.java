package DSAL.Leetcode;

class Solution {
    int sumLeft, sumRight;
    public int pivotIndex(int[] nums) {
        for(int i =0; i < nums.length / 2; i++){
            sumLeft += nums[i];
        }
        for(int j = 0; j > nums.length / 2; j--){
            sumRight +=nums[j];
        }
        return sumLeft;
    }
    


public static void main(String[] args) {
    int[] nums = {1, 7, 3, 6, 5, 6};
    Solution s = new Solution();
    System.out.println(s.pivotIndex(nums));
    }
}    
