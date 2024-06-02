def intToRoman(num: int) -> str:
    hmap = {
      1:    'I',
      4:    'IV',
      5:    'V',
      9:    'IX',
     10:    'X',
     40:    'XL',
     50:    'L',
     90:    'XC',
    100:    'C',
    400:    'CD',
    500:    'D',
    900:    'CM',
   1000:    'M'
    }
    result = ''
    
    thousands_digit = int(num / 1000 % 10)
    hundreds_digit = int(num / 100 % 10)
    tens_digit = int(num / 10 % 10)
    ones_digit = int(num / 1 % 10)
    
    if thousands_digit:
        result += hmap[1000] * thousands_digit
    if hundreds_digit:
        if hundreds_digit == 4:
            result += hmap[400]
        elif hundreds_digit == 9:
            result += hmap[900]
        elif hundreds_digit in range(5, 9):
            result += hmap[500] + hmap[100] * (hundreds_digit - 5)
        else:
            result += hmap[100] * hundreds_digit
    if tens_digit:
        if tens_digit == 4:
            result += hmap[40]
        elif tens_digit == 9:
            result += hmap[90]
        elif tens_digit in range(5, 9):
            result += hmap[50] + hmap[10] * (tens_digit - 5)
        else:
            result += hmap[10] * tens_digit
    if ones_digit:
        if ones_digit == 4:
            result += hmap[4]
        elif ones_digit == 9:
            result += hmap[9]
        elif ones_digit in range(5, 9):
            result += hmap[5] + hmap[1] * (ones_digit - 5)
        else:
            result += hmap[1] * ones_digit
        
    return result
    



num = 3749
print(intToRoman(num))