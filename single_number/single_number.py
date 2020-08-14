'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # create dictionary to hold numbers
    storage = {}
    # loop through array
    for value in arr:
        # assign value to a key and set to true
        if value not in storage.keys():
            storage[value] = True
        # if key already exists, change value to false
        else:
            storage[value] = False

    # loop through dictionary to find which value is true
    for key, value in storage.items():
        if value is True:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")