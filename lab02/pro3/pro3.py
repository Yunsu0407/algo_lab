import random


def main():
    test = False
    if test:
        array_size = 10
        array = [8, 26, 85, 84, 45, 29, 81, 36, 40, 9]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 101), array_size)

    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")
    ans.append("퀵 정렬 시작: ")

    section = [0, len(array) - 1]
    recursive_quick_sort(array, section, ans)

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, array)) + "]")
    final_ans = "\n".join(ans)
    print(final_ans)


def recursive_quick_sort(array, section, ans):
    left, right = section
    if right - left < 1:
        return

    pivot = array[left]
    ans.append(f"생성된 피벗의 값: {pivot}")

    low = left + 1
    high = right

    while True:
        while low <= high and array[low] <= pivot:
            low = low + 1

        while low <= high and array[high] >= pivot:
            high = high - 1

        if low > high:
            break

        array[low], array[high] = array[high], array[low]

    array[left], array[high] = array[high], array[left]

    low_section = [left, high - 1]
    high_section = [high + 1, right]

    ans.append("정렬 단계: [" + ", ".join(map(str, array)) + "]")

    recursive_quick_sort(array, low_section, ans)
    recursive_quick_sort(array, high_section, ans)


if __name__ == "__main__":
    main()
