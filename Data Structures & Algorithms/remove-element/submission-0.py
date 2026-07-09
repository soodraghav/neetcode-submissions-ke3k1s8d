class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l = 0 
        r = len(nums)-1

        count = 0


        while r > l:


            while r> l and nums[r] == val:
                r-=1
            
            while r > l and nums[l] != val:
                l+=1

            
            nums[l], nums[r] = nums[r], nums[l]
            

            l+=1
            r-=1
        
        for i in range(len(nums)):
            if nums[i] == val:
                break
            count+=1

        return count