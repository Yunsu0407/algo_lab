import random
import operator


def main():
    test = False
    if test:
        array = [87, 4, 262, 746, 338, 864, 965, 691, 29, 851]
    else:
        array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))
        array = random.sample(range(1, 1000), array_size)

    ans = []
    ans.append("data list : [" + ", ".join(map(str, array)) + "]")

    min = findExtreme(array, True)
    max = findExtreme(array, False)
    ans.append(f"최댓값: {max} / 최솟값: {min}")

    final_ans = "\n".join(ans)
    print(final_ans)


def findExtreme(array, is_min):
    compare = operator.lt if is_min else operator.gt
    extreme = array[0]

    for val in array[1:]:
        if compare(val, extreme):
            extreme = val

    return extreme


if __name__ == "__main__":
    main()
