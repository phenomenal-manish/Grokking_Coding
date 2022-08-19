'''
Given an array of n-1 integers in the range from 1 to n, find the one number that is missing from the array.

Example:
Input: 1, 5, 2, 6, 4
Answer: 3
'''
# Summation of int numbers can also work, but it can lead to buffer overflow when n is large

# O(n) time | O(1) space
def find_missing_number(arr):
    n = len(arr) + 1
    # x1 represents XOR of all values from 1 to n
    x1 = 1
    for i in range(2, n+1):
        x1 = x1 ^ i

    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ arr[i]
  
    # missing number is the xor of x1 and x2
    return x1 ^ x2

def main():
    arr = [1, 5, 2, 6, 4] 
    print('Missing number is:' + str(find_missing_number(arr)))

main()