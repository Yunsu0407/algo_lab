import random


def main():
    test = False
    if test:
        array = [63, 86, 47, 89, 76, 42, 69, 35, 11, 36]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 101), array_size)

    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str, array)) + "]")

    sorted_array = heap_sort(array, ans)

    ans.append("최종 정렬 결과: [" + ", ".join(map(str, sorted_array)) + "]")
    final_ans = "\n".join(ans)
    print(final_ans)


def heap_sort(array, ans):
    n = len(array)

    # 1단계: 최대 힙(Max Heap) 만들기
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # 2단계: 힙에서 하나씩 꺼내 정렬
    for end in range(n - 1, 0, -1):
        # root(최대값)와 마지막 원소 교환
        array[0], array[end] = array[end], array[0]

        # 교환 후 힙 성질 복구
        heapify(array, end, 0)

        # heap root 저장
        ans.append(f"heap root : {array[0]}")

        # 현재 단계 결과 저장
        ans.append("정렬 단계: [" + ", ".join(map(str, array)) + "]")

    return array


def heapify(array, n, i):
    largest = i  # 현재 노드를 최대값으로 가정
    left = 2 * i + 1  # 왼쪽 자식 인덱스
    right = 2 * i + 2  # 오른쪽 자식 인덱스

    # 왼쪽 자식이 존재하고 현재 노드보다 크다면
    if left < n and array[left] > array[largest]:
        largest = left

    # 오른쪽 자식이 존재하고 현재 노드보다 크다면
    if right < n and array[right] > array[largest]:
        largest = right

    # 최대값이 현재 노드가 아니라면 교환 후 재귀적으로 heapify
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


if __name__ == "__main__":
    main()
