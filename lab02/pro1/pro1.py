import random


def main():
    test = False
    if test:
        array_size = 10
        array = [67, 14, 27, 8, 56, 18, 3, 96, 15, 96]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 101), array_size)

    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")
    ans.append("삽입 정렬 시작:")

    for i in range(array_size - 1):  # size - 1번 동안 삽입 정렬 실행
        curr_idx = i + 1  # 현재 key의 위치
        key = array[curr_idx]  # 삽입할 값 저장
        j = i  # key 앞쪽 인덱스부터 검사 시작

        ans.append(f"단계별 선택된 key : {key}")

        # key보다 큰 값들을 한 칸씩 뒤로 이동
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # j가 멈춘 자리 바로 뒤에 key 삽입
        array[j + 1] = key

        ans.append(f"단계 {i + 1}:[" + ", ".join(map(str, array)) + "]")

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, array)) + "]")

    final_ans = "\n".join(ans)
    print(final_ans)


if __name__ == "__main__":
    main()
