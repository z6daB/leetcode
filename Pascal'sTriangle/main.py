class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triange = [[1]]
        for i in range(1, numRows):
            temp_row = []
            for j in range(i + 1):
                if j - 1 >= 0 and j + 1 <= len(triange[-1]) and i - 1 >= 0:
                    temp_row.append(triange[i-1][j-1] + triange[i-1][j])
                else:
                    temp_row.append(1)
            triange.append(temp_row)
        return triange
