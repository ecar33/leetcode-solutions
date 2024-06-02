from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        prefix_xor = [0] * n
        prefix_xor[0] = arr[0]
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i]
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    xor_ij = prefix_xor[j-1] ^ (prefix_xor[i-1] if i > 0 else 0)
                    xor_jk = prefix_xor[k] ^ prefix_xor[j-1]
                    if xor_jk == xor_ij:
                        count += 1
        return count
        
        


s = Solution()
arr = [2, 3, 1, 6, 7]

print(s.countTriplets(arr))