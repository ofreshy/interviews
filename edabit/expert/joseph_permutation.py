"""
A group of n prisoners stand in a circle awaiting execution.
Starting from an arbitrary position(0),
the executioner kills every kth person until one person remains standing,
who is then granted freedom (see examples).

Create a function that takes 2 arguments — the number of people to be executed n, and the step size k,
and returns the original position (index) of the person who survives.

who_goes_free(9, 2) ➞ 2

# Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Executed people replaced by - (a dash) for illustration purposes.
# 1st round of execution = [0, -, 2, -, 4, -, 6, -, 8]  -> [0, 2, 4, 6, 8]
# 2nd round = [-, 2, -, 6, -] -> [2, 6]  # 0 is killed in this round because it's beside 8 who was skipped over.
# 3rd round = [2, -]

who_goes_free(9, 3) ➞ 0

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
# [0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
# [0, 1, -, 6] -> [0, 1, 6]
# [0, -, 6] -> [0, 6]
# [0, -] -> [0]
"""


def who_goes_free(num_people, step):
    def bang(people, ind, count):
        # Termination of recursion
        if len(people) == 1:
            return people[0]
        if ind == len(people):
            ind = 0
        # Eliminate person :(
        if count == step:
            return bang(people[:ind] + people[ind+1:], ind, 1)
        else:
            return bang(people, ind+1, count+1)

    return bang(list(range(num_people)), 0, 1)


assert who_goes_free(9, 2) == 2
assert who_goes_free(9, 3) == 0


class DeathRound(object):

    @classmethod
    def make(cls, n, k):
        return cls([p for p in range(n)], k)

    def __init__(self, people, step):
        self.people = people
        self.step = step
        self.count = 1
        self.index = 0

    def solve(self):
        def move():
            if self.index == len(self.people):
                self.index = 0
            if self.count == self.step:
                self.count = 1
                self.people = self.people[:self.index] + self.people[self.index + 1:]
            else:
                self.count += 1
                self.index += 1

        def survivor():
            return None if len(self.people) > 1 else self.people[0]

        while survivor() is None:
            move()
        return survivor()


def who_goes_free_2(n, k):
    d = DeathRound.make(n, k)
    return d.solve()


assert who_goes_free_2(9, 2) == 2
assert who_goes_free_2(9, 3) == 0
