from collections import Counter

def frequencySort(nums: list[int]) -> list[int]:
    res = Counter(nums)
    nums.sort(key = lambda x: (res[x], -x))
    return nums

if __name__ == "__main__":
    print(frequencySort([1,1,2,2,2,3]))
    print(frequencySort([2,3,1,3,2]))
    print(frequencySort([-1,1,-6,4,5,-6,1,4,1]))