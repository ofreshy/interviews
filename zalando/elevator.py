

def solution(A, B, M, X, Y):
    """

    :param A: people weight
    :param B: people floor destination
    :param M: number of floors but we don't need you
    :param X: max people
    :param Y: max load
    :return: number of stops
    """
    people = zip(A, B)
    elevator = Elevator(max_people=X, max_load=Y, max_floor=M)
    for p in people:
        if elevator.can_add_person(p):
            elevator.add_person(p)
        else:
            elevator.rendezvous()
            # Don't forget that person
            elevator.add_person(p)

    elevator.rendezvous()

    return elevator.stops


class Elevator(object):
    def __init__(self, max_people, max_load, max_floor):
        self._max_people = max_people
        self._max_load = max_load
        self._max_floor = max_floor

        # mutable
        self.stops = 0
        self._current_load = 0
        self._current_num_people = 0
        self._current_destinations = set()

    def has_people(self):
        return bool(self._current_num_people)

    def can_add_person(self, person):
        weight, floor = person
        if self._current_num_people == self._max_people:
            return False
        if self._current_load + weight > self._max_load:
            return False
        if self._max_floor < floor:
            return False
        return True

    def add_person(self, person):
        if not self.can_add_person(person):
            # This can be a custom error
            raise ValueError
        weight, destination = person
        self._current_num_people += 1
        self._current_load += weight
        self._current_destinations.add(destination)

    def _clear(self):
        self._current_num_people = 0
        self._current_load = 0
        self._current_destinations = set()

    def rendezvous(self):
        if self.has_people():
            # We only really care here about the total number of stops
            # so just add it to stops
            self.stops += len(self._current_destinations)
            # Add one for going back down again
            self.stops += 1
        self._clear()


assert solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200) == 6
assert solution([60, 80, 40], [2, 3, 5], 5, 2, 200) == 5
assert solution([60, 80, 40], [2, 3, 5], 5, 2, 200) == 5
assert solution([60, 80, 40], [2, 2, 2], 5, 3, 200) == 2
assert solution([60, 80, 40], [2, 2, 2], 5, 3, 80) == 6
