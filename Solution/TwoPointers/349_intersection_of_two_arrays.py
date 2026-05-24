def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    for i in nums1:
        for j in nums2:
            if i == j and i not in result:
                result.append(i)
    return result

if __name__ == "__main__":
    print(intersection([1,2,2,1],[2,2]))
    print(intersection([4,9,5],[9,4,9,8,4]))