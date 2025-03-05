from typing import List

def search_range(nums: List[int], target: int) -> List[int]:
    def binary_search(left: bool) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target or (left and nums[mid] == target):
                r = mid - 1
            else:
                l = mid + 1
        return l

    left_index = binary_search(True)
    if left_index >= len(nums) or nums[left_index] != target:
        return [-1, -1]

    return [left_index, binary_search(False) - 1]

# Test
print(search_range([5,7,7,8,8,10], 8))  # Output: [3, 4]
