def findMaxK(nums) -> int:
    nums.sort(reverse=True)
    map = {}
    
    for index, num in enumerate(nums):
        map[num] = index
    
    for num in nums:
        if -num in map:
            return num
    return -1



nums = [-1, 2, -3, 3]

print(findMaxK(nums))