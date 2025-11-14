def main():
    points = [
        (2.0, 3.0),
        (3.0, 3.0),
        (4.0, 3.0),
        (3.0, 2.0),
        (2.0, 2.0),
        (1.0, 3.0),
        (3.0, 5.0),
        (2.0, 1.0),
        (4.0, 1.0),
        (5.0, 3.0),
    ]

    result = point_wrapping(points)
    print("Wrapping Results:", result)


def orientation(p, q, r):
    """
    반시계 방향(CCW)면 양수
    시계 방향(CW)면 음수
    일직선이면 0
    """
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def point_wrapping(points):
    hull = []

    # 1. x값이 가장 작은 점 선택 (왼쪽 끝점)
    start = min(points, key=lambda x: (x[0], x[1]))  # x 최소 → y 최소
    p = start

    while True:
        hull.append(p)

        # 임시 후보 q = p와 다른 아무 점
        q = points[0] if points[0] != p else points[1]

        for r in points:
            if r == p:
                continue

            # orientation(p, q, r) < 0 → p→q→r 방향이 시계(CW)
            if orientation(p, q, r) < 0:
                q = r

            # 일직선일 경우 더 먼 점을 선택 (정확한 헐 유지)
            elif orientation(p, q, r) == 0:
                # p→r이 p→q보다 더 멀면 r 선택
                dist_pr = (r[0] - p[0]) ** 2 + (r[1] - p[1]) ** 2
                dist_pq = (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2
                if dist_pr > dist_pq:
                    q = r

        p = q

        if p == start:  # 처음점으로 돌아오면 종료
            break

    return hull


if __name__ == "__main__":
    main()
