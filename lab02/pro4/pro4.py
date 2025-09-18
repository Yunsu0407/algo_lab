import random

def main():
    # array_size = 10
    array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))

    # array = [66, 31, 10, 75, 39, 6, 9, 35, 50, 81, 31, 19, 25, 44, 50, 29, 49, 69, 44, 26]
    array = random.sample(range(1,101), array_size)
    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str,array)) + "]")

    recursive_merge_sort(array)

    ans.append("최종 정렬 결과: [" + ", ".join(map(str,array)) + "]")
    final_ans = "\n".join(ans)
    print(final_ans)

def recursive_merge_sort():


def merge():
    


if __name__ == "__main__":
    main()