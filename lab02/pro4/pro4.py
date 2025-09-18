import random


def main():
    test = False
    if test:
        array_size = 20
        array = [
            66,
            31,
            10,
            75,
            39,
            6,
            9,
            35,
            50,
            81,
            31,
            19,
            25,
            44,
            50,
            29,
            49,
            69,
            44,
            26,
        ]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 101), array_size)

    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")
    ans.append("합병 정렬 시작:")

    n = len(array)
    size = 1  # 처음에는 1개씩 묶어서 비교/합병 시작

    # 크기를 1, 2, 4, 8... 늘려가며 병합 수행
    while size < n:
        # i는 병합할 구간의 시작점
        for i in range(0, n, size * 2):
            mid = i + size
            end = min(i + size * 2, n)

            if mid < end:  # 실제로 병합할 오른쪽 부분이 존재할 때만
                merged = merge(array[i:mid], array[mid:end])
                array[i:end] = merged

        ans.append(f"크기 {size} 단계: [" + ", ".join(map(str, array)) + "]")
        size *= 2

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, array)) + "]")

    final_ans = "\n".join(ans)
    print(final_ans)


def merge(left, right):
    """두 개의 정렬된 배열을 병합하는 함수"""
    result = []
    l_ptr = r_ptr = 0

    # 두 배열에서 작은 값을 하나씩 꺼내 result에 채움
    while l_ptr < len(left) and r_ptr < len(right):
        if left[l_ptr] <= right[r_ptr]:
            result.append(left[l_ptr])
            l_ptr += 1
        else:
            result.append(right[r_ptr])
            r_ptr += 1

    # 남아 있는 원소들 붙여주기
    result.extend(left[l_ptr:])
    result.extend(right[r_ptr:])
    return result


if __name__ == "__main__":
    main()
