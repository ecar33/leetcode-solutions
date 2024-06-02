import heapq

def mincostToHireWorkers(quality, wage, k: int) -> float:
    c_ratios = []
    n = len(quality)
    for q, w in zip(quality, wage):
        c_ratios.append(w/q)
    
    heaps = [[] for _ in range(n)]
    heap_index = 0
    
    for ratio in c_ratios:
        for i in range(n):
            if ratio * quality[i] >= wage[i]:
                heaps[heap_index].append(ratio * quality[i])
        heapq.heapify(heaps[heap_index])
        heap_index += 1

    paid_groups = [[] for _ in range(n)]
    smallest_paid_group = float('inf')
    for index, heap in enumerate(heaps):
        if len(heap) >= k:
            paid_groups[index] = heapq.nsmallest(k, heap)
            sum_paid_group = sum(paid_groups[index])
            if sum_paid_group < smallest_paid_group:
                smallest_paid_group = sum_paid_group
        
    
    return smallest_paid_group


    
quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
k = 3

print(mincostToHireWorkers(quality, wage, k))
