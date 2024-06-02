def findRelativeRanks(score):
    score_index_map = {score: idx for idx, score in enumerate(score)}
    
    # Sorting the scores in descending order to determine ranks
    sorted_scores = sorted(score, reverse=True)
    
    # Initialize the result list with empty strings based on the number of scores
    result = [""] * len(score)
    
    # Assign medals or numerical ranks
    for rank, score in enumerate(sorted_scores):
        if rank == 0:
            result[score_index_map[score]] = "Gold Medal"
        elif rank == 1:
            result[score_index_map[score]] = "Silver Medal"
        elif rank == 2:
            result[score_index_map[score]] = "Bronze Medal"
        else:
            result[score_index_map[score]] = str(rank + 1)
    
    return result

score = [10,3,8,9,4]
score = findRelativeRanks(score)
print(score)