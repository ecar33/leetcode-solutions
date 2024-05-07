def main():
    nums = [3,13,9,8,5,18,11,10]
    k = 13
    
    
    for num in nums:
        print(f'{num} is: {format(num, '04b')}')
    
    xorNums = xorArr(nums)
    print(bin(xorNums))
    print(bin(k))
    diff = xorNums ^ k
    
    for position in range(diff.bit_length()):  # iterate through each bit position
        print(position)
    
    print(bin(diff))
    

    
    print(count_set_bits(diff)) 
    
    
def xorArr(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
        
    
 

    # position = 1
    # k = 15
    # print(f'{k} in bin is {bin(k)}')
    # mask = 1 << position
    # print(bin(mask))
    # if (k & mask):
    #     print(f"There is 1 on pos {position} for k")

if __name__ == '__main__':
    main()