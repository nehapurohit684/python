def swap(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
class SelectionSort:
    def selection_sort(nums):
        for i in range(len(nums)):
            minIndex = i
            for idx in range(i + 1, len(nums)):
                if (nums[idx] < nums[minIndex]):
                    swap(minIndex, idx, nums)
        return nums

nums = [3,2,9,1,10,5]
print(SelectionSort.selection_sort(nums))