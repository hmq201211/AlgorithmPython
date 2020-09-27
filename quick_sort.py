def quick_sort(nums: list) -> None:
    def swap(arr: list, index_1: int, index_2: int) -> None:
        temp = arr[index_1]
        arr[index_1] = arr[index_2]
        arr[index_2] = temp

    def partition(arr: list, left: int, right: int) -> int:
        temp = left
        pivot = arr[left]
        while True:
            while left < right:
                if nums[left] > pivot:
                    break
                else:
                    left += 1
            while right > temp:
                if nums[right] < pivot:
                    break
                else:
                    right -= 1
            if right < left:
                break
            swap(nums, right, left)
        swap(nums, temp, right)
        return right

    def sort(arr: list, left: int, right: int) -> None:
        if left >= right:
            return
        else:
            split = partition(arr, left, right)
            sort(arr, left, split - 1)
            sort(arr, split + 1, right)
        sort(nums, 0, len(nums) - 1)


test_list = [6, 6]
quick_sort(test_list)
print(test_list)
