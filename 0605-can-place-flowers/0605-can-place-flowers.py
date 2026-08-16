class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        f = [0] + flowerbed + [0]
        length = len(f)
        for i in range(1,length-1):
            if f[i - 1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i]= 1
                n -= 1 
            
        return n <= 0   