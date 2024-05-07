class Solution:
    def numRescueBoats(people, limit) -> int:
        people.sort()
        boat_count = 0
        
        start = 0
        end = len(people) - 1
        
        while start <= end:
            boat_count += 1
            if people[start] + people[end] <= limit:
               start += 1
            end -= 1 
        return boat_count
        
        
        
        

sol = Solution
people = [3,5,3,4]
limit = 5
print(sol.numRescueBoats(people, limit))