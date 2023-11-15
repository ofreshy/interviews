"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

"""
from typing import List


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    def max_it(l: List[int], current_max, max_list):
        if len(l) == 1:
            return max_list
        new_max = max(l[0], current_max)
        max_list.append(new_max)
        return max_it(l[1:], new_max, max_list)

    hl = max_it(height, 0, [0])
    hr = list(reversed(max_it(list(reversed(height)), 0, [0])))
    min_left_right = [
        min(r, l)
        for r, l
        in zip(hl, hr)
    ]
    trapped_water = [
        max(0, ml-hi)
        for hi, ml
        in zip(height, min_left_right)
    ]
    return sum(trapped_water)


trap([4,2,0,3,2,5])
trap([0,1,0,2,1,0,1,3,2,1,2,1])



