import unittest
from assertpy import assert_that
from game_of_life_rules import should_live
from hypothesis import given
from hypothesis.strategies import integers


def count_live_neighbours(grid):
    return 3


class GameOfLifeRules(unittest.TestCase):
    @staticmethod
    def test_cell_with_no_live_neighbours_dies():
        assert_that(should_live(0)).is_false()

    @staticmethod
    def test_cell_with_3_live_neighbours_lives():
        assert_that(should_live(3)).is_true()

    @given(integers(min_value=4))
    def test_cell_with_more_than_3_live_neighbours_lives(self, i):
        assert_that(should_live(i)).is_false()


if __name__ == '__main__':
    unittest.main()
