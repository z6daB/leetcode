# 338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        matrix = [0] * (n + 1)
        for i in range(1, n + 1):
            matrix[i] = 1 + matrix[i - (1 << (i.bit_length() - 1))]
        return matrix



# Когда я писал этот код, только Бог и я понимали, что он означает. Теперь понимает только Бог.
