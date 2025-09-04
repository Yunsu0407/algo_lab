import random


def main():
    size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))

    array = random.sample(range(1, 101), size)

    ans = []
    ans.append("버블 정렬 시작: ")

    for i in range(size - 1):  # size - 1번 동안 버블 정렬 실행
        bubble_sort(array, i)  # 정렬 함수 호출
        ans.append(f"단계 {i + 1}: [" + ", ".join(map(str, array)) + "]")

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, array)) + "]")

    final_ans = "\n".join(ans)
    print(final_ans)


# 버블 정렬 실행 함수
def bubble_sort(array, sub_val):
    limit = len(array) - (sub_val + 1)
    # 0부터 limit전까지 비교 수행
    for i in range(limit):
        if array[i] > array[i + 1]:  # 앞의 값(i)이 뒤의 값(i + 1) 보다 큰 경우
            # 두 값을 교환
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp


if __name__ == "__main__":
    main()
