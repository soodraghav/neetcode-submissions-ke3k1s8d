class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = r = 0

        ans = []
        q = collections.deque()

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            
            if r < k-1: 
                r+=1
                continue


            while q[0] <= r-k:
                q.popleft()

            ans.append(nums[q[0]])
            r+=1

        return ans



            
        