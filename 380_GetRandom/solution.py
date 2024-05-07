from random import *

class RandomizedSet:

    def __init__(self):
            self.random_set = []
            self.index_map = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.random_set.append(val)
            self.index_map[val] = len(self.random_set) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            last_elem, indx = self.random_set[-1], self.index_map[val]
            self.random_set[indx] = last_elem
            self.index_map[last_elem] = indx
            
            self.random_set.pop()
            del self.index_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.random_set)

    
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
