def edit_distance(n, X, m, Y, ins, delete, change):
    D = [[0] * (m + 1) for _ in range(n + 1)]

    # 초기화
    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + delete
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + ins

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 0 if X[i - 1] == Y[j - 1] else change
            D[i][j] = min(
                D[i - 1][j] + delete,  # 삭제
                D[i][j - 1] + ins,  # 삽입
                D[i - 1][j - 1] + c,
            )  # 변경 or 그대로
    return D


def main():
    test = False
    if test:
        X = "bbabb"
        Y = "aaba"
    else:
        X = input("초기 문자열을 입력하시오 : ")
        Y = input("목표 문자열을 입력하시오 : ")

    ins = delete = change = 1  # 문제 예제를 보면 모두 비용 1로 계산됨

    D = edit_distance(len(X), X, len(Y), Y, ins, delete, change)

    print("편집거리 테이블")
    for row in D:
        print(*row)

    print("최소편집비용 :", D[len(X)][len(Y)])


if __name__ == "__main__":
    main()
