import random


def main():
    my_input = "11 12"  # 입력 예제
    sizes = my_input.split()
    size_n = int(sizes[0])  # 집합 A의 크기 n
    size_m = int(sizes[1])  # 집합 B의 크기 m

    lists = [[] for _ in range(4)]  # 집합 A, 집합 B, 합집합, 교집합
    # lists[0] = [1, 3, 4, 5, 9, 11, 19, 22, 26, 32, 55] # 집합 A 예제
    # lists[1] = [3, 5, 7, 8, 9, 11, 12, 21, 32, 40, 42, 43] # 집합 B 예제
    lists[0] = random.sample(range(1, 101), size_n)  # 집합 A에 난수 배정
    lists[1] = random.sample(range(1, 101), size_m)  # 집합 B에 난수 배정
    lists[2] = getUnion(lists[0], lists[1])  # 합집합
    lists[3] = getIntersection(lists[0], lists[1])  # 교집합

    titles = ["집합 A", "집합 B", "합집합", "교집합"]  # 각 집합에 대한 제목

    lines = []  # 최종 출력문
    for one_title, one_list in zip(titles, lists):  # 반복을 통해 출력문 생성
        lines.append(f"{one_title} - {one_list}")

    print("\n".join(lines))  # 정답 출력


# 합집합을 구하는 함수
def getUnion(setA, setB):
    setU = setB.copy()  # 합집합, setB 복사
    for val in setA:
        if val not in setU:  # 값이 중복되지 않으면
            setU.append(val)  # 합집합에 추가

    return sorted(setU)


# 교집합을 구하는 함수
def getIntersection(setA, setB):
    setI = []  # 교집합
    for val in setA:
        if val in setB:  # 값이 중복되면
            setI.append(val)  # 교집합에 추가

    return sorted(setI)


if __name__ == "__main__":
    main()
