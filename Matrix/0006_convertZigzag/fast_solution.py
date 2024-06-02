class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows>len(s):
            return s

        index = 0
        step = 0
        new_list = [[] for i in range(numRows)]
        for char in s:
            new_list[index].append(char)
            if index == 0:
                step = 1
            if index == numRows-1:
                step = -1            
            index = index+step
        new_string = ''
        for i in range(numRows):
            new_string = new_string+''.join(new_list[i])
        
        return new_string