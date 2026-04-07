

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        gmax = nums[0] 
        
        lmax =nums[0]
        lmin = nums[0]

        for i in range(1,len(nums)):

            temp = lmax
            lmax = max(nums[i], lmax*nums[i],lmin * nums[i]) 
            lmin = min(nums[i], lmin*nums[i],temp*nums[i]) 

            gmax = max(gmax,lmax) 
        
        return gmax 







        