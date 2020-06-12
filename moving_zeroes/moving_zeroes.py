'''
Input: a List of integers
Returns: a List of integers
'''

def _find_non_zero(subset):
    for i, val in enumerate(subset):
        if val != 0:
            return i


def _swap(x1, x2):
    return x2, x1


def moving_zeroes(arr):
    for i, val in enumerate(arr):
        if arr[i] == 0:
            subset_index = _find_non_zero(arr[i:])
            if subset_index is None:
                break
            swap_pos = i + subset_index 
            arr[i], arr[swap_pos] = _swap(arr[i], arr[swap_pos])

    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")