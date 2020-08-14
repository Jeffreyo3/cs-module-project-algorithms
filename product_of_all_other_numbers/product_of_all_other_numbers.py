'''
Input: a List of integers
Returns: a List of integers
'''
# TO-DO O(n)
def product_of_all_other_numbers(arr):
    if len(arr) < 2:
        return None

    except_index = [None] * len(arr)

    # for each int, find product of all the integers
    # store total product so far each time
    
    for i in range(len(arr)):
        current = 1
        for j in range(len(arr)):
            print(i, j)
            if j != i:
                current *= arr[j]

        except_index[i] = current

    return except_index


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
