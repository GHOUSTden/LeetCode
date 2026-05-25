def two_sum(nums: list[int], target: int) -> list[int]:
    counter_j = 0
    for i in range(0, len(nums)):
        counter_j += 1
        for j in range(counter_j, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9)) #== [0, 1]
    print(two_sum([3,2,4], 6)) #== [1,2]
    print(two_sum([3,3], 6)) #== [0,1]
    print(two_sum([2,5,5,11], 10)) #== [1,2]