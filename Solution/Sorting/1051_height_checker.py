def height_checker(heights: list[int]) -> int:
    counter = 0
    sorted_heights = sorted(heights)

    for i in range(0, len(sorted_heights)):
        if heights[i] != sorted_heights[i]:
            counter += 1
    return counter

if __name__ == "__main__":
    print(height_checker([1,1,4,2,1,3]))