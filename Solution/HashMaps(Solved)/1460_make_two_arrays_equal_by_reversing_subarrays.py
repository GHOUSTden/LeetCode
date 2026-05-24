from collections import Counter

def canBeEqual(target: list[int], arr: list[int]) -> bool:
    target = Counter(target)
    arr = Counter(arr)
    for i in arr:
        if i not in target or target[i] != arr[i]:
            return False
    return True

if __name__ == "__main__":
    print(canBeEqual([1,2,3,4], [2,4,1,3]))
    print(canBeEqual([7], [7]))
    print(canBeEqual([3,7,9], [3,7,11]))