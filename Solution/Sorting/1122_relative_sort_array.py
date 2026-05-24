def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    d = {}
    s = []
    for v in arr1:
        if v in d:
            d[v] = d[v] + 1
        else:
            d[v] = 1

    for v in arr2:
        s.extend([v] * d.pop(v))

    leftovers = sorted(d.keys())
    for v in leftovers:
        s.extend([v] * d[v])

    return s

if __name__ == "__main__":
    print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))