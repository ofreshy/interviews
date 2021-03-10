# -*- coding: utf-8 -*-

"""


You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee.

Write a class TempTracker with these methods:

    insert()—records a new temperature
    get_max()—returns the highest temp we've seen so far
    get_min()—returns the lowest temp we've seen so far
    get_mean()—returns the mean  of all temps we've seen so far
    get_mode()—returns a mode  of all temps we've seen so far

Optimize for space and time. Favor speeding up the getter functions (get_max(), get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter functions can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..1100..110.

If there is more than one mode, return any of the modes.

"""
from collections import defaultdict


class TemperatureTracker(object):
    def __init__(self):
        self.samples = 0
        self.max = None
        self.min = None
        self.mean = None
        self.freq = defaultdict(int)
        self.modes = set()

    def insert(self, temp):
        self.samples += 1
        if self.max is None or temp > self.max:
            self.max = temp
        if self.min is None or temp < self.min:
            self.min = temp
        if self.mean is None:
            self.mean = 0
        self.mean = (self.mean*(self.samples-1) + temp) / self.samples

        mode_freq = 0 if not self.modes else self.freq[list(self.modes)[0]]
        temp_freq = self.freq[temp] + 1
        if temp_freq == mode_freq:
            self.modes.add(temp)
        elif temp_freq > mode_freq:
            self.modes = set([temp])
        self.freq[temp] = temp_freq

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        if self.modes is None:
            return None
        import random
        return random.choice(list(self.modes))


t = TemperatureTracker()
assert t.get_max() is None
assert t.get_min() is None
assert t.get_mean() is None

t.insert(5)
assert t.get_max() == 5
assert t.get_min() == 5
assert t.get_mean() == 5
assert t.get_mode() == 5


t.insert(7)
assert t.get_max() == 7
assert t.get_min() == 5
assert t.get_mean() == 6
assert t.get_mode() in set([5, 7])

t.insert(0)
assert t.get_max() == 7
assert t.get_min() == 0
assert t.get_mean() == 4
assert t.get_mode() in set([5, 7, 0])

t.insert(0)
assert t.get_mode() == 0


