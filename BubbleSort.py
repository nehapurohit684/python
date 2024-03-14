def swap(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


class BubbleSort:
    def bubble_sort(nums):
        for i in range(len(nums)):
            for idx in range(len(nums) - 1, i, -1):
                if (nums[idx] < nums[idx - 1]):
                    swap(idx - 1, idx, nums)
        return nums


nums = [2, 9, 1, 10, 5]
print(BubbleSort.bubble_sort(nums))
