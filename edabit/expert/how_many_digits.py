"""
Imagine you took all the numbers between 0 and n and concatenated them together into a long string.
How many digits are there between 0 and n? Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and 100.
"""


def naive_how_many(n):
    b = [str(i) for i in range(1, n)]
    return len("".join(b))


def show(nums:list):
    for num in nums:
        print(num % 10, num // 10 )
        print("{} -> {}".format(num, naive_how_many(num)))


def how_many(n):
    def do_it(left_over, num_digits, total):
        max_digits = 9 * 10 ** (num_digits-1)
        if left_over > max_digits:
            return do_it(left_over - max_digits, num_digits + 1, total + (max_digits * num_digits))
        value = (left_over - 1) * num_digits
        return total + value
    return do_it(n, 1, 0)



show([5, 10, 15, 35, 101, 223, 1000])
print(9 * 1 + 90 * 2 + (223-99-1) * 3)

"""
5  ->   5 single
10 ->  9 single
15 -> 9 single, 5 double
35 -> 9 single, 25 double (9 * 1 + 25 X 2 = 61)
101 -> 9 single, 90 double, 1 triple, 
223 -> 9 singles, 90 doubles, 223-99-1 triples 
1000 -> 9 single, 90 double, 900 triple
2000 -> 9 single, 90 double, 900 triple, 1000 quadaple
"""
print("--------")
for n in (101, 223, 1000, 2000):
    print("n={} heur={} naive={}".format(n, how_many(n), naive_how_many(n)))


