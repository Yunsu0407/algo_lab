import random


def main():
    test = False
    if test:
        array = [42, 75, 58, 13, 14, 71, 7, 96, 90, 64]
        target = 13
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 100), array_size)
        print(f"리스트: {array}")
        target = int(input("target data를 입력하세요: "))

    result = find_target(array, target)

    if result >= 0:
        ans = f"값 {target}는 인덱스 {result}에 있습니다."
    else:
        ans = "찾는 타겟이 없습니다."
    print(ans)


def find_target(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return i

    return -1


if __name__ == "__main__":
    main()
