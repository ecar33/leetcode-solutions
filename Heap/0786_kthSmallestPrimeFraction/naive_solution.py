
# Time complexity: O(n^2logn)
def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    result = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            result.append((arr[i]/arr[j]))
    result.sort()
    return result[k - 1]



