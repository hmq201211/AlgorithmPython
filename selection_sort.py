def selection_sort(nums: list, is_max: bool) -> None:
    def search(arr: list) -> int:
        saved = arr[0]
        saved_index = 0
        for i in range(1, len(arr)):
            if is_max:
                if saved < arr[i]:
                    saved = arr[i]
                    saved_index = i
            else:
                if saved > arr[i]:
                    saved = arr[i]
                    saved_index = i
        print(saved)
        return saved_index

    def swap(arr: list, index_1: int, index_2: int) -> None:
        temp = arr[index_1]
        arr[index_1] = arr[index_2]
        arr[index_2] = temp

    for j in range(len(nums) - 1):
        target = search(nums[j:]) + j
        swap(nums, j, target)


test_list = [2, 4, 6, 2, 3, 4, 6, 9]
selection_sort(test_list, True)
print(test_list)
