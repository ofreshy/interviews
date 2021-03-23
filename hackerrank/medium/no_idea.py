"""
There is an array of integers. There are also disjoint sets, and , each containing integers. You like all the integers in set and dislike all the integers in set . Your initial happiness is . For each integer in the array, if , you add to your happiness. If , you add

to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since
and

are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints


Input Format

The first line contains integers
and separated by a space.
The second line contains integers, the elements of the array.
The third and fourth lines contain integers, and

, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

Explanation

You gain
unit of happiness for elements and in set . You lose unit for in set . The element in set

does not exist in the array so it is not included in the calculation.

['3 2\n', '1 5 3\n', '3 1\n', '5 7']

"""


def rate_happiness(data):
    my_nums = [n for n in data[1].strip().split(" ")]
    happy_set = set([n for n in data[2].strip().split(" ")])
    unhappy_set = set([n for n in data[3].strip().split(" ")])

    happiness = 0
    for n in my_nums:
        if n in happy_set:
            happiness += 1
        elif n in unhappy_set:
            happiness -= 1

    return happiness


assert rate_happiness(['3 2\n', '1 5 3\n', '3 1\n', '5 7']) == 1




