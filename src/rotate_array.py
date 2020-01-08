class Solution:
    def rotate_iterate(self, nums, k):
        """ Move array item k times

        Time: O(kn) Space: O(1)

        :param nums:
        :param k:
        :return:
        """
        if len(nums) == 0:
            return

        for x in range(k):
            start = nums[-1]
            for y in range(len(nums) - 1, -1, -1):
                nums[y] = nums[y - 1]
            nums[0] = start

    def rotate_slice(self, nums, k):
        """ Slice Array and concat

        Time: O(n) Space: O(n)

        :param nums:
        :param k:
        :return:
        """
        length = len(nums)
        nums[:] = nums[length - k:] + nums[:length - k]

    def rotate_copy(self, nums, k):
        """ Copy to another array

        Time: O(n) Space: O(n)

        :param nums:
        :param k:
        :return:
        """
        length = len(nums)
        new_nums = [0, ] * length
        for index, x in enumerate(nums):
            real_index = (index + k) % length
            new_nums[real_index] = x

        nums[:] = new_nums



