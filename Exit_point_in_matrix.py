#User function Template for python3

class Solution:
    def FindExitPoint(self, n, m, matrix):
        i, j = 0, 0
        d1, d2 = 0, 1
        while 0<=i<n and 0<=j<m:
            if matrix[i][j]:
                matrix[i][j] = 0
                if d1 == 1:
                    d1, d2 = 0, -1
                elif d1 == -1:
                    d1, d2 = 0, 1
                elif d2 == 1:
                    d1, d2 = 1, 0
                else:
                    d1, d2 = -1, 0
            i += d1
            j += d2
        
        return i-d1,j-d2    # Code here
