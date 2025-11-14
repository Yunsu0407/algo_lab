def main():
    # 입력
    print("첫 번째 직선")
    x1, y1 = map(float, input("첫 번째 점의 좌표를 입력하시오: ").split())
    x2, y2 = map(float, input("두 번째 점의 좌표를 입력하시오: ").split())

    print("두 번째 직선")
    x3, y3 = map(float, input("첫 번째 점의 좌표를 입력하시오: ").split())
    x4, y4 = map(float, input("두 번째 점의 좌표를 입력하시오: ").split())

    # 처리
    a1, b1 = get_line_equation(x1, y1, x2, y2)
    a2, b2 = get_line_equation(x3, y3, x4, y4)

    # 출력
    result = check_relation(a1, b1, a2, b2)
    print(result)


def get_line_equation(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return None, None  # 에러
    if x2 == x1:
        return float("inf"), x1  # 수직선: 기울기를 무한대로 표현
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a, b


def check_relation(a1, b1, a2, b2):
    if a1 is None or a2 is None:
        return "유효하지 않은 선분이 입력되었습니다."

    if a1 == a2:
        if b1 == b2:
            return "두 선분은 일치합니다."
        else:
            return "두 선분은 평행합니다."
    else:
        return "두 선분은 교차합니다."


if __name__ == "__main__":
    main()
