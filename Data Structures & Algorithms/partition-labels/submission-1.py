class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        l = 0
        maxr = 0
        ans = []

        for i,n in enumerate(s):

            d[n] = i

        for i,n in enumerate(s):

            maxr = max(maxr,d[n])

            if maxr == i:
                ans.append(i-l+1)
                l = i+1
        
        return ans



        

        
        