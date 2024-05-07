class Solution:
    def numRescueBoats(people, limit) -> int:
        people.sort()
        boat_count = 0
        
        start = 0
        end = len(people) - 1
        
        while start < end:
            if (people[end] == limit):
                end -= 1
                boat_count += 1
            else:
                s = people[start] + people[end]
                if (s == limit):
                    start += 1
                    end -= 1
                    boat_count += 1
                elif (s > limit):
                    end -= 1
                    boat_count += 1
                else:
                    start += 1
                    end -= 1
                    boat_count += 1
        if (start == end and people[end] <= limit):
            return boat_count + 1
        return boat_count
        
        
        
        

sol = Solution
people = [3,5,3,4]
limit = 5
print(sol.numRescueBoats(people, limit))