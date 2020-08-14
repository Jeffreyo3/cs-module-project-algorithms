'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zeroRight = []
    for i, value in enumerate(arr):
        if value == 0:
            zeroRight.append(0)
        else:
            zeroRight.insert(0, value)

    return zeroRight


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

