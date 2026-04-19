class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) < groupSize or len(hand)%groupSize!=0: return False

        d = dict(Counter(hand))
        total = int(len(hand) // groupSize)

        while total > 0:

            minn = min(d.keys())

            for i in range(groupSize):
                if minn+i not in d: return False
                d[minn+i]-= 1
                if d[minn+i] == 0: d.pop(minn+i)

            total-=1
        return True


