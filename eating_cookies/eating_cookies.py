'''
Input: an integer
Returns: an integer
'''
# TO-DO: need to implement a cache for large tests
def eating_cookies(n, cache=[]):
    # base case
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        if len(cache) == 0:
            cache = [0] * (n+1)

        if cache[n] != 0:
            return cache[n]
        
        # 3 recursive calls
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]




if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
