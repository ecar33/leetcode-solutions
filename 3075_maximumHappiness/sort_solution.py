def maximumHappinessSum(happiness, k):
    happiness.sort()
    res,n = 0, len(happiness)-1
    for i in range(k):
        if happiness[n-i] - i < 0: break
        res += happiness[n-i] - i
    return res