import random


def main():
    size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))

    array = random.sample(range(1, 101), size)
    ans = []
    ans.append("선택 정렬 시작:")

    for i in range(size - 1):  # size - 1번 동안 선택 정렬 진행
        selection_sort(array, i)  # 정렬 함수 호출
        ans.append(f"단계 {i + 1}: [" + ", ".join(map(str, array)) + "]")

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, array)) + "]")

    final_ans = "\n".join(ans)
    print(final_ans)


# 선택 정렬 실행 함수
def selection_sort(array, start_idx):
    min_val = array[start_idx]  # 최솟값
    min_idx = start_idx  # 최소 인덱스

    for i in range(start_idx + 1, len(array)):
        if array[i] < min_val:  # 현재 값이 최솟값보다 작은 경우
            min_val = array[i]  # 최솟값 갱신
            min_idx = i  # 최소 인덱스 갱신

    # 현재 위치와 최솟값 교환
    temp = array[start_idx]
    array[start_idx] = min_val
    array[min_idx] = temp


if __name__ == "__main__":
    main()
