def sort_array(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i - 1
        k = nums[i]

        while j >= 0 and k < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = k

    return nums

if __name__ == "__main__":
    print(sort_array([5,1,1,2,0,0]))