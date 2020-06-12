'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

class Window():
    def __init__(self, k, max_len):
        self.k = k
        self.max_len = max_len
        self.min = 0
        if k < max_len:
            self.max = k
        else:
            self.max = max_len


    def _return_valid_max(self):
        if self.max <= self.max_len:
            return self.max 
        return self.max_len


    def shift(self, m=1):
        self.min += m 
        self.max += m 
        return self.min, self.max


class Bounds():
    def __init__(self, mini, maxi):
        self.min = mini
        self.max = maxi



def sliding_window_max(arr, k):
    window = Window(k=k, max_len=len(arr))
    max_arr = []
    for _ in arr:
        max_arr.append(
            max(arr[window.min:window.max])
        )
        if window.max == window.max_len:
            break
        window.shift()
    return max_arr



# def _get_max(job):
#     arr = job[0]
#     bounds = job[1]
#     return max(arr[bounds.min:bounds.max])

# def _build_bounds(arr, k):
#     window = Window(k=k, max_len=len(arr))
#     bounds= []
#     for _ in arr:
#         bounds.append(
#             Bounds(mini=window.min, maxi=window.max)
#         )
#         if window.max == window.max_len:
#             break
#         window.shift()
#     return bounds

# def sliding_window_max(arr, k):
#     bounds = _build_bounds(arr, k)
#     return list(map(
#         _get_max, list(zip([arr]*len(bounds), bounds))
#     ))



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
