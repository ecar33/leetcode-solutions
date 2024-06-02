import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # Step 1: Prepare workers list by pairing each worker's minimum required ratio of wage to quality
        # with their quality, and then sorting this list by the ratio.
        workers = sorted(
            (float(w) / q, q) for w, q in zip(wage, quality)
        )  # [(ratio, quality), ...] sorted by ratio

        # Step 2: Initialize variables for result, the running total of qualities, and the heap.
        res = float("inf")  # to keep track of the minimum cost found
        quality_sum = 0  # sum of qualities of workers in the current heap
        heap = []  # this heap will keep the largest k qualities to calculate minimum cost

        # Step 3: Iterate over the sorted list of workers.
        for cur_ratio, q in workers:
            # Step 4: Add the current worker's quality to the heap and quality sum
            heapq.heappush(heap, -q)  # use negative for max-heap simulation
            quality_sum += q

            # Step 5: Ensure the heap does not exceed size k. If it does, remove the worker with the largest quality.
            if len(heap) > k:
                # Pop from heap (remember it's negative because of max-heap simulation)
                quality_sum += heapq.heappop(heap)  # this should subtract the largest quality

            # Step 6: If the heap size is exactly k, compute the potential cost of hiring these k workers.
            if len(heap) == k:
                # Calculate the total cost for these k workers based on the current ratio
                # and update the result if it's the lowest cost found so far.
                res = min(res, quality_sum * cur_ratio)

        # Step 7: Return the minimum cost found to hire exactly k workers.
        return res

# Example usage
quality = [10, 20, 5] 
wage = [70, 50, 30] 
k = 2

# Instantiate Solution class and use the function
solution = Solution()
print(solution.mincostToHireWorkers(quality, wage, k))  # Outputs the minimum cost to hire k workers
