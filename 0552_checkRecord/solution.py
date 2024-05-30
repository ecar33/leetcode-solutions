class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        # Initialize the cache to store sub-problem results.
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        def eligible_combination(n: int, total_absences, consecutive_lates) -> List[str]:
            # Base case.
            if total_absences >= 2 or consecutive_lates >= 3: return 0 # Invalid combination, count is not incremented
            if n == 0: return 1  # Valid combination
            # If we have already seen this sub-problem earlier, 
            # we return the stored result.
            if memo[n][total_absences][consecutive_lates] != -1:
                return memo[n][total_absences][consecutive_lates]


            count = eligible_combination(n-1, total_absences, 0) # Choose P
            count = (count + eligible_combination(n-1, total_absences + 1, 0)) % MOD # Choose A
            count = (count + eligible_combination(n-1, total_absences, consecutive_lates + 1)) % MOD # Choose L
            
            # Return and store the current sub-problem result in the cache.
            memo[n][total_absences][consecutive_lates] = count
            return count
        
        return eligible_combination(n, 0, 0)
            

s = Solution()
n = 2
print(s.checkRecord(n))