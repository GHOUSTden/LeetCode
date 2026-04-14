def evaluate_reverse_polish_notation(tokens: list[str]) -> int:
    res = []
    for v in tokens:
        if v in "-+/*":
            b = res.pop()
            a = res.pop()

            if v == "+":
                res.append(a + b)
            elif v == "-":
                res.append(a - b)
            elif v == "*":
                res.append(a * b)
            elif v == "/":
                res.append(int(a / b))
        else:
            res.append(int(v))

    return res[0]

if __name__ == "__main__":
    print(evaluate_reverse_polish_notation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))