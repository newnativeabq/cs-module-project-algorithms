'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    counts = {}    
    val = None
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return [key for key in counts if counts[key] == 1][0]


def single_number_xor_test(arr):
    val = 0
    for num in arr:
        val ^= num 
    return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    # print(f"The odd-number-out is {single_number_hash(arr)}")
    print(f"The odd-number-out is {single_number(arr)}")