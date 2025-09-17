import random

def main():
    # array_size = 10
    array_size = int(input("생성할 랜덤 변수 개수를 입력하세요: "))

    # array = [8, 26, 85, 84, 45, 29, 81, 36, 40, 9]
    array = random.sample(range(1,101), array_size)
    ans = []
    ans.append("생성된 list : [" + ", ".join(map(str,array)) + "]")


    ans.append("최종 정렬 결과: [" + ", ".join(map(str,array)) + "]")

    final_ans = "\n".join(ans)
    print(final_ans)


if __name__ == "__main__":
    main()