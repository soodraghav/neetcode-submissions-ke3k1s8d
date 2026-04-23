class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        l = 0
        maxr = 0
        ans = []

        for i,n in enumerate(s):

            d[n] = i

        for i,n in enumerate(s):

            if d[n] == i and maxr == i:
                ans.append(i-l+1)
                l = i+1
                if l<len(s): maxr = d[s[l]]

            elif d[n] > maxr:
                maxr = d[n]

        
        return ans



        

        
        