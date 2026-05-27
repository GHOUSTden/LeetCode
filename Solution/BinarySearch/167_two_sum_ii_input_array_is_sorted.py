def twoSum(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1

    for _ in range(0, len(nums)):
        if (nums[left] + nums[right]) == target:
            return [left + 1, right + 1]
        if (nums[left] + nums[right]) < target:
            left += 1
        else:
            right -= 1

if __name__ == "__main__":
    print(twoSum([2,7,11,15],9))