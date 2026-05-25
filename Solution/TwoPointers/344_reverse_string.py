def reverseString(s: list[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp

        left += 1
        right -= 1

if __name__ == "__main__":
    s = ["h","e","l","l"]
    reverseString(s)
    print(s)