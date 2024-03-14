class InsertionSort:
    def swap(i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def insertion_sort(nums):
        for i in range(len(nums)):
            temp1 = nums[i]
            red = i - 1
            while red >= 0 and nums[red] > temp1:
                nums[red + 1] = nums[red]
                red = red - 1
            nums[red + 1] = temp1
        return nums


nums = [2, 9, 1, 10, 5]
print(InsertionSort.insertion_sort(nums))
