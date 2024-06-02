class Solution:
    def numRescueBoats(people, limit) -> int:
        people.sort()  # Sort the people by weight
        boat_count = 0
        
        start = 0  # Pointer to the lightest person
        end = len(people) - 1  # Pointer to the heaviest person
        
        while start <= end:
            boat_count += 1  # A new boat is used
            if people[start] + people[end] <= limit:
                start += 1  # Lightest person can share the boat
            end -= 1  # Heaviest person is placed on the boat
        return boat_count
        
        
        

sol = Solution
people = [3,5,3,4]
limit = 5
print(sol.numRescueBoats(people, limit))