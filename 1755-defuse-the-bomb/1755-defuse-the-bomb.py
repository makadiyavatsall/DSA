class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        if k == 0:
            return [0] * n

        extended = code + code
        res = []

        if k > 0:
            for i in range(n):
                s = 0
                for j in range(1, k+1):
                    s += extended[i+j]
                res.append(s)

        if k < 0:
            for i in range(n):
                s = 0
                for j in range(1, -k+1):
                    s += extended[i-j+n]
                res.append(s)

        return res
