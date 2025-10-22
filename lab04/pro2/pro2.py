import random


def main():
    test = False
    if test:
        array = [981, 178, 831, 657, 14, 294, 888, 968, 928, 946]
        table_size = 2
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 1000), array_size)
        table_size = int(input("몇 개의 테이블로 나눌 것인지 입력하세요: "))

    ans = []
    ans.append(f"data list : {array}")

    balanced_multiway_merge_sort(array, table_size, ans)

    final_ans = "\n".join(ans)
    print(final_ans)


def balanced_multiway_merge_sort(array, table_size, ans):
    # 1. 초기 분배
    tapes = [[] for _ in range(table_size)]
    for i, item in enumerate(array):
        tapes[i % table_size].append(item)

    ans.append(f"분할할 리스트 : {tapes}")

    # 2. 개별 리스트 정렬
    sorted_tapes = []
    for tape in tapes:
        sorted_tape = sort_sublist_with_steps(tape, ans)
        sorted_tapes.append(sorted_tape)

    # 3. 최종 병합
    ans.append(f"정렬해서 합쳐진 리스트 : {sorted_tapes}")

    final_result = []
    if sorted_tapes:
        final_result = sorted_tapes[0]
        for i in range(1, len(sorted_tapes)):
            final_result = merge(final_result, sorted_tapes[i])

    ans.append(f"최종적으로 합쳐진 리스트 : {final_result}")


def sort_sublist_with_steps(arr, ans):
    if len(arr) <= 1:
        return arr

    list1 = arr[::2]
    list2 = arr[1::2]
    ans.append(f"분할할 리스트 : {[list1, list2]}")

    sorted_list1 = sort_sublist_with_steps(list1, ans)
    sorted_list2 = sort_sublist_with_steps(list2, ans)

    ans.append(f"정렬해서 합쳐진 리스트 : {[sorted_list1, sorted_list2]}")
    return merge(sorted_list1, sorted_list2)


def merge(left, right):
    merged_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return merged_list


if __name__ == "__main__":
    main()
