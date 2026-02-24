class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0
        n = len(gas)

        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start
