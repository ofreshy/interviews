"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

from queue import PriorityQueue
from typing import List


def max_sliding_window(nums: List[int], k: int):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    tick = 0
    max_val = None
    queue = PriorityQueue()

    def is_valid(elem):
        return tick - elem[1] < k

    def search_queue():
        maybe_elem = queue.get()
        if is_valid(maybe_elem):
            queue.put(maybe_elem)
            return -maybe_elem[0]
        else:
            return search_queue()

    def inject_val(val):
        queue.put((val * -1, tick))

    for val in nums[:k]:
        tick += 1
        inject_val(val)
        max_val = val if max_val is None else max(val, max_val)
    yield max_val

    for val in nums[k:]:
        tick += 1
        inject_val(val)

        if val > max_val:
            max_val = val
        else:
            max_val = search_queue()
        yield max_val


# it = max_sliding_window([1,3,-1,-3,5,3,6,7], k = 3)
it = max_sliding_window([1,-1], 1)
for a in it:
    print(a)