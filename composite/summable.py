from collections.abc import Iterable
from abc import ABC
import unittest

class Summable(Iterable, ABC):
    @property
    def sum(self):
        sum_value = 0
        for s in self:
            if hasattr(s, 'value'):
                sum_value = sum_value + s.value
            elif isinstance(s, Sumable):
                sum_value = sum_value + s.sum
            else:
                sum_value = sum_value + s
        return sum_value


class SingleValue(Summable):
    value: int
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self

class ManyValues(list, Summable):
    def __init__(self):
        super().__init__()


## Test
class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)