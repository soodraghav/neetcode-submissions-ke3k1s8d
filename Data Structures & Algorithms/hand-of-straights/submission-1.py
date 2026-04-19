class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) < groupSize or len(hand)%groupSize!=0: return False

        d = Counter(hand)
        
        keyz = sorted(d.keys())


        for minn in keyz:

            while minn in d:

                for i in range(groupSize):
                    if minn+i not in d: return False
                    d[minn+i]-= 1
                    if d[minn+i] == 0: d.pop(minn+i)


        return True