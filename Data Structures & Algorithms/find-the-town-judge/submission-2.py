class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        trusted = defaultdict(int)
        trustee = defaultdict(int)

        candidates = set()


        for a,b in trust:

            trusted[b]+=1
            trustee[a]+=1

            if trusted[b] == n-1: candidates.add(b)

        for candidate in candidates:

            if trusted[candidate] == n-1 and trustee[candidate] == 0:

                return candidate

        
        return -1


