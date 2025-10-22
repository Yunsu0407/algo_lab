import random


def main():
    test = False
    if test:
        array = [4, 22, 29, 33, 34, 50, 60, 82, 88, 92, 94, 94]
        # target = 22
        target = 70
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 100), array_size)
        array.sort()
        print(f"리스트: {array}")
        target = int(input("target data를 입력하세요:  "))

    result = find_target(array, 0, len(array) - 1, target)

    if result >= 0:
        ans = f"Target {target}는 인덱스 {result}에 있습니다."
    else:
        ans = "찾는 타겟이 없습니다."

    print(ans)


def find_target(array, front, rear, target):
    if front > rear:
        return -1

    print("찾는 구간")
    section = []
    for i in range(front, rear + 1):
        section.append(str(array[i]))
    sections = " ".join(section)
    print(sections)

    mid = (front + rear) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        front = mid + 1
        return find_target(array, front, rear, target)
    else:
        rear = mid - 1
        return find_target(array, front, rear, target)


if __name__ == "__main__":
    main()
