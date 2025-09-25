import random


def main():
    test = True
    if test:
        array_size = 10
        array = [4, 8, 4, 4, 4, 2, 7, 1, 3, 5]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요 (최소 10): "))
        array = [random.randint(1, 10) for _ in range(array_size)]

    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")

    sorted_arr = counting_sort_step(array, ans)

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, sorted_arr)) + "]")
    final_ans = "\n".join(ans)
    print(final_ans)


def counting_sort_step(arr, ans):
    max_val = 10  # 값의 범위 (1~10)

    # 1단계: count 배열 초기화
    count = [0] * max_val
    for num in arr:
        count[num - 1] += 1  # 1~10 → 인덱스 0~9

    ans.append("초기 원소의 개수 배열 : [" + ", ".join(map(str, count)) + "]")

    sorted_arr = arr[:]  # 원본 배열 복사해서 단계별 교체

    # 2단계: count 배열 순회하면서 정렬
    index = 0
    for i in range(max_val):
        while count[i] > 0:
            count[i] -= 1
            sorted_arr[index] = i + 1  # 실제 값은 인덱스+1
            index += 1
            # 단계별 출력
            ans.append("원소의 개수 배열 : [" + ", ".join(map(str, count)) + "]")
            ans.append("단계별 배열 : [" + ", ".join(map(str, sorted_arr)) + "]")

    return sorted_arr


if __name__ == "__main__":
    main()
