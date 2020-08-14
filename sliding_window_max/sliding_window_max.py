'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# TO-DO re-factor for max_large test
def sliding_window_max(nums, k):
    maxValues = []
    for i in range(len(nums)-(k-1)):
        # print(f"INDEX {i}")
        current = nums[i]
        for j in range(i, (i+k)):
            # print(f"num {nums[j]}")
            if nums[j] > current:
                current = nums[j]
        maxValues.append(current)
    return maxValues


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
