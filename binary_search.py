from typing import List


def binary_search(nums: List, target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


numbers = [i for i in range(5)]
result = binary_search(numbers, 6)
print(result)