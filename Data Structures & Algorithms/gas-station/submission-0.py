class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # candidates = []

        def canTravel(idx):
            i = idx
            length = len(cost)
            tot_gas = 0

            while length > 0:

                tot_gas+= gas[i]
                tot_gas-= cost[i]

                if tot_gas < 0: return False

                i+=1
                if i == len(gas): i =0
                length -=1

            return True







        for i in range(len(cost)):

            if gas[i] >= cost[i] and canTravel(i): return i

        return -1

        