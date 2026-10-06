class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        d = defaultdict(int)
        d[0] = 1
        count = 0
        summ = 0
 

        for n in nums:

            summ+=n

            if summ - k in d:
                count+= d[summ-k]
            
            d[summ]+=1

        
        return count

        
        


        