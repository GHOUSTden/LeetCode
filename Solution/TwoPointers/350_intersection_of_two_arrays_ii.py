from collections import Counter

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1_counter = Counter(nums1)
    nums2_counter = Counter(nums2)

    result = []

    for i in nums1_counter:
        if i in nums2_counter:
            frequency = min(nums1_counter[i], nums2_counter[i])
            for _ in range(frequency):
                result.append(i)
    return result

if __name__ == "__main__":
    print(intersection([1,2,2,1],[2,2]))
    print(intersection([4,9,5],[9,4,9,8,4]))