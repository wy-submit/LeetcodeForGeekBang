import unittest
from ..rotate_array import Solution


class TestSolution(unittest.TestCase):
    def __main_test(self):
        test_arr = [
            [[1, 2, 3, 4], 3, [2, 3, 4, 1]],
            [[1, 2, 3, 4], 4, [1, 2, 3, 4]],
            [[1, 2, 3, 4], 0, [1, 2, 3, 4]],
            [[1, 2, 3, 4], 2, [3, 4, 1, 2]],
            [[], 5, []]
        ]

        solu = Solution()
        for arr, k, res in test_arr:
            solu.rotate_iterate(arr, k)
            self.assertListEqual(arr, res)

    def test_rotate_iterate(self):
        self.__main_test()

    def test_rotate_slice(self):
        self.__main_test()

    def test_rotate_copy(self):
        self.__main_test()


if __name__ == '__main__':
    unittest.main()
