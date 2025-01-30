# 121. Best Time to Buy and Sell Stock
class Solution:
    def countBits(self, n: int) -> List[int]:
        matrix = [0] * (n + 1)
        for i in range(1, n + 1):
            matrix[i] = 1 + matrix[i - (1 << (i.bit_length() - 1))]
        return matrix
