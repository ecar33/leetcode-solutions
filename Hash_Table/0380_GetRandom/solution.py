from random import choice

class RandomizedSet:

    def __init__(self):
        self.random_set = []  # List to store elements
        self.index_map = {}   # Dictionary to store element indices

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.random_set.append(val)  # Append to the list
            self.index_map[val] = len(self.random_set) - 1  # Store index in dictionary
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            last_elem = self.random_set[-1]  # Get the last element
            indx = self.index_map[val]  # Get index of the element to remove
            self.random_set[indx] = last_elem  # Swap with the last element
            self.index_map[last_elem] = indx  # Update index of the last element
            
            self.random_set.pop()  # Remove the last element from the list
            del self.index_map[val]  # Delete the element from the dictionary
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.random_set)  # Return a random element from the list

obj = RandomizedSet()
param_1 = obj.insert(3)
param_2 = obj.remove(2)
param_3 = obj.insert(4)
param_4 = obj.insert(3)
param_5 = obj.remove(3)
param_6 = obj.insert(0)
param_7 = obj.getRandom()

outcomes = [param_1, param_2, param_3, param_4, param_6, param_7]

print(outcomes)
