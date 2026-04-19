class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) > sum(gas): return -1

        total_gas = 0
        idx = 0 

        for i in range(len(cost)):

            total_gas+= gas[i]- cost[i]
            if total_gas < 0:
                total_gas = 0
                idx=i+1

        return idx

        