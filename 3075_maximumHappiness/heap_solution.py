import heapq

def maximumHappinessSum(happiness, k):
    if len(happiness) == 1:
        return happiness[0]
    
    # Find the k largest elements
    result = heapq.nlargest(k, happiness)
     # Decrement each element in the result by an increasing amount and return
    # The first element is not decremented, subsequent elements are decremented increasingly
    return result[0] + sum([max((x - index), 0) for index, x in enumerate(result) if index != 0])


happiness = [2,83,62]
k = 3
print(maximumHappinessSum(happiness, k))
    