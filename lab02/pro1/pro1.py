import random


def main():
    size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))

    # array = [67, 14, 27, 8, 56, 18, 3, 96, 15, 96]
    array = random.sample(range(1, 101), size)
    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")
    ans.append("삽입 정렬 시작:")

    for i in range(size - 1):  # size - 1번 동안 삽입 정렬 실행
        curr_idx = i + 1  # 현재 인덱스
        prev_idx = curr_idx - 1  # 이전 인덱스

        ans.append(f"단계별 선택된 key : {array[curr_idx]}")

        # 범위 초과를 방지하기 위해 0보다 크며, 현재 값이 더 작은 경우에만 교환
        while curr_idx > 0 and array[curr_idx] < array[prev_idx]:
            temp_val = array[prev_idx]
            array[prev_idx] = array[curr_idx]
            array[curr_idx] = temp_val
            curr_idx = curr_idx - 1  # 인덱스 감소
            prev_idx = curr_idx - 1  # 인덱스 감소

        ans.append(f"단계 {i + 1}:[" + ", ".join(map(str, array)) + "]")

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, array)) + "]")

    final_ans = "\n".join(ans)
    print(final_ans)


if __name__ == "__main__":
    main()
