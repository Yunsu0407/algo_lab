def main():
    n = int(input("입력: "))

    for i in range(n + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    main()
