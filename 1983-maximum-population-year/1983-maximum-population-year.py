class Solution(object):
    def maximumPopulation(self, logs):
        diff = [0] * 101

        for birth, death in logs:
            diff[birth - 1950] += 1
            diff[death - 1950] -= 1

        max_pop = 0
        year = 1950
        curr = 0

        for i in range(101):
            curr += diff[i]
            if curr > max_pop:
                max_pop = curr
                year = 1950 + i

        return year
