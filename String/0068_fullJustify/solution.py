from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_length = 0
        current_line = []

        
        for word in words:
            #  char length      spaces count        new word
            if current_length + len(current_line) + len(word) > maxWidth:
                result.append((current_line, current_length))
                current_line = []
                current_length = 0
                
            current_line.append(word)
            current_length += len(word)
            
        if current_line:
            result.append((current_line, current_length + len(current_line) - 1))

        
        justified_output = []
        for index, line in enumerate(result):
            words, _ = line
            num_of_gaps = len(words) - 1
            line_length = line[1]
            is_last_line = (index == len(result) - 1)
            
            if num_of_gaps > 0:
                total_spaces_needed = maxWidth - line_length
                base_spaces, extra_spaces = divmod(total_spaces_needed, num_of_gaps)
            else:
                base_spaces = maxWidth - line_length
                extra_spaces = 0
            
            justified_line = self.build_justified_line(words, base_spaces, extra_spaces, maxWidth, is_last_line)            
            justified_output.append(justified_line)
            
        
        return justified_output

    def build_justified_line(self, words, base_spaces, extra_spaces, maxWidth, is_last_line):
        line = ''
        
        if len(words) == 1:
            return words[0] + (' ' * base_spaces)
    
        for i, word in enumerate(words):
            line += word
            if not is_last_line:
                if i < len(words) - 1:
                    line += ' ' * (base_spaces + (1 if i < extra_spaces else 0))
            else:
                if i < len(words) - 1:
                    line += ' '
        
        if is_last_line:
            line += ' ' * (maxWidth - len(line))
        
        return line
            
                    
                
    

s = Solution()
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(s.fullJustify(words, maxWidth))    
            