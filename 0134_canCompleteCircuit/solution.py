from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        n = len(gas) # Both gas and cost are same length
        
        if total_gas - total_cost < 0:
            return -1
        
        start = 0
        current_gas = 0
        for i in range(n):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        
        return start


s = Solution()
gas = [3,1,1]
cost = [1,2,2]

print(s.canCompleteCircuit(gas, cost))