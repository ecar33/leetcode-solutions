import heapq

# Time complexity: O(klogn)
def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    heap = []
    
    # Initial heap setup: each numerator paired with the largest denominator
    for i in range(n - 1):
        print(f'{arr[i]}/{arr[n-1]}')
        heapq.heappush(heap, (arr[i] / arr[n-1], i, n-1))
    
    # Extract the smallest fraction k times
    for _ in range(k - 1):
        # Pop current min
        _, i, j = heapq.heappop(heap)
        if j - 1 > i:
            # Check the next largest denominator by decrementing j
            heapq.heappush(heap, (arr[i] / arr[j-1], i, j-1))
    
    # The k-th smallest fraction
    fraction_value, i, j = heapq.heappop(heap)
    return [arr[i], arr[j]]


arr = [1,2,3,5]
k = 3
print(kthSmallestPrimeFraction(arr, 3))

