def guess(num: int, pick: int = None) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

def guessNumber(n: int, pick: int = None) -> int:
    left = 0
    right = n

    while left < right:
        mid = (left + right) // 2
        if guess(mid, pick) == 0:
            return mid
        elif guess(mid, pick) == -1:
            right = mid - 1
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    print(guessNumber(10,6))