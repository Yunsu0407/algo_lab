import random


def bucket_sort(arr, ans):
    bucket_count = 10  # 버킷 개수 고정
    min_val, max_val = min(arr), max(arr)

    # 버킷 크기를 실수로 계산
    bucket_size = (max_val - min_val) / bucket_count

    # 빈 버킷 생성
    buckets = [[] for _ in range(bucket_count)]

    # 1단계: 각 데이터를 버킷에 분배
    for num in arr:
        # 버킷 인덱스 = (값 - min) / 버킷크기
        idx = int((num - min_val) / bucket_size)
        if idx >= bucket_count:  # max 값은 마지막 버킷에 강제로 배치
            idx = bucket_count - 1
        buckets[idx].append(num)
        ans.append("단계별 버킷들 : " + str(buckets))

    # 2단계: 각 버킷 내부 정렬 (삽입 정렬)
    for b in buckets:
        for i in range(1, len(b)):
            key = b[i]
            j = i - 1
            while j >= 0 and b[j] > key:
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = key

    # 3단계: 모든 버킷 합치기
    sorted_arr = []
    for b in buckets:
        sorted_arr.extend(b)

    return sorted_arr


def main():
    test = True
    if test:
        array = [78, 49, 91, 91, 46, 57, 52, 99, 73, 73]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요 (최소 10): "))
        array = [random.randint(1, 100) for _ in range(array_size)]

    ans = []
    ans.append("생성된 list : " + str(array))

    sorted_arr = bucket_sort(array, ans)

    ans.append("최종 정렬 결과: " + str(sorted_arr))
    print("\n".join(ans))


if __name__ == "__main__":
    main()
