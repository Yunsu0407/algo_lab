import random


def main():
    test = False
    if test:
        array_size = 10
        array = [92, 21, 5, 100, 31, 64, 47, 78, 77, 12]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 101), array_size)

    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")
    ans.append("쉘 정렬 시작:")

    gap = array_size // 2
    while gap > 0:
        chunk_size = array_size // gap
        chunks = []

        # gap 크기에 맞춰 chunk 요소 구성
        for i in range(gap):
            chunk = []
            for j in range(chunk_size):
                idx = i + j * gap
                if idx < array_size:
                    chunk.append(idx)
            chunks.append(chunk)

        # 각 chunk에 대한 삽입 정렬 실행
        insertion_sort(array, chunks)
        ans.append(f"간격 {gap} 단계: [" + ", ".join(map(str, array)) + "]")

        gap = gap // 2

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, array)) + "]")

    final_ans = "\n".join(ans)
    print(final_ans)


def insertion_sort(array, chunks):
    for chunk in chunks:
        for i in range(1, len(chunk)):
            core_val = array[chunk[i]]
            j = i
            # core_val보다 큰 값들을 오른쪽으로 한 칸씩 밀기
            while j > 0 and array[chunk[j - 1]] > core_val:
                array[chunk[j]] = array[chunk[j - 1]]
                j -= 1
            array[chunk[j]] = core_val


if __name__ == "__main__":
    main()
