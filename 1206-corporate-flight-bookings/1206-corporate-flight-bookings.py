class Solution(object):
    def corpFlightBookings(self, bookings, n): 
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats      
            if last < n:                   
                diff[last] -= seats
        answer = [0] * n
        total = 0
        for i in range(n):
            total += diff[i]
            answer[i] = total
        
        return answer
