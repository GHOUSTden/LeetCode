def sort_colors(nums: list[int]) -> None:
    for i in range(1, len(nums)):
        j = i - 1
        k = nums[i]
        while j >= 0 and k < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
            nums[j + 1] = k

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    print(nums)
    sort_colors(nums)
    print(nums)