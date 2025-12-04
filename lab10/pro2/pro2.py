def main():
    n = int(input("N의 값을 입력해주세요: "))
    print("분할정복 시작")

    ans = power_of_two(n)
    print(f"2의 {n}제곱은 {ans}입니다.")


def power_of_two(n, level=1):
    print(f"{level}차 분할: 2^{n}")

    if n == 0:
        print(f"{level}차 합치기: 2^0 = 1")
        return 1

    if n % 2 == 0:
        half = power_of_two(n // 2, level + 1)
        result = half * half
        print(f"{level}차 합치기: 2^{n} = 2^{n//2} * 2^{n//2} = {result}")
        return result
    else:
        half = power_of_two(n // 2, level + 1)
        result = half * half * 2
        print(f"{level}차 합치기: 2^{n} = 2^{n//2} * 2^{n//2} * 2 = {result}")
        return result


if __name__ == "__main__":
    main()
