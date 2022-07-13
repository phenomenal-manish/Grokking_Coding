# Brute Force 
'''
# O(n * k) time | O(n) space
def find_averages_of_subarray(K, arr):
    result = []
    for i in range(len(arr) - K + 1):
        sum = 0.
        for j in range(i, i + K):
            sum += arr[j]
        result.append(sum/K)
    return result
'''

# O(n) time | O(n) space
def find_averages_of_subarray(K, arr):
    result = []
    windowSum = 0.0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K) #calculate the average
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window ahead

    return result

def main():
    result = find_averages_of_subarray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: "+str(result))

main()