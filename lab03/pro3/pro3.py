import random


def main():
    test = True
    if test:
        array_size = 20
        array = [
            4785,
            8642,
            7638,
            5502,
            7276,
            3657,
            7246,
            2591,
            3770,
            4156,
            6807,
            730,
            9999,
            6405,
            7594,
            1003,
            605,
            8390,
            9636,
            3716,
        ]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요 (최소 20): "))
        array = [random.randint(1, 10000) for _ in range(array_size)]

    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")

    sorted_arr = radix_sort(array, ans)

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, sorted_arr)) + "]")
    final_ans = "\n".join(ans)
    print(final_ans)


def radix_sort(arr, ans):
    # 최대값 구해서 자릿수 확인
    max_num = max(arr)

    exp = 1  # 1의 자리부터 시작
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp, ans)
        exp *= 10

    return arr


def counting_sort_by_digit(arr, exp, ans):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 자릿수는 0~9

    # 1단계: 현재 자리수의 count 배열 만들기
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # 2단계: 누적합 (자리별 위치 결정)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3단계: output 배열 채우기 (안정 정렬 유지)
    i = n - 1
    while i >= 0:
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1

    # 4단계: 결과를 원본 arr에 반영
    for i in range(n):
        arr[i] = output[i]

    # 현재 자릿수 단계 결과 저장
    ans.append(f"자릿수 {exp} 단계: [" + ", ".join(map(str, arr)) + "]")


if __name__ == "__main__":
    main()
