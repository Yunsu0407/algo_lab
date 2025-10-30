def main():
    test = False
    text = "Human Computer Interaction Lab, Jin-Woo Jung, Algorithm Lab Work6"
    if test:
        pattern = "Work6"
        # pattern = "Human"
        # pattern = "human"
    else:
        pattern = input("찾을 패턴을 입력하세요 : ")

    idx = boyer_moore_search(text, pattern)
    if idx != -1:
        print(f"패턴이 인덱스 {idx} 에서 발견되었습니다.")
        print("해당 패턴을 찾았습니다.")
    else:
        print("해당 패턴을 찾지 못했습니다.")


def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return -1

    # Bad character 테이블 생성
    bad_char = build_bad_char_table(pattern)

    i = 0  # text에서 시작 인덱스
    while i <= n - m:
        j = m - 1

        # 패턴 뒤에서부터 비교
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        # 패턴을 찾은 경우
        if j < 0:
            return i  # 시작 인덱스 반환

        # 불일치 문자가 존재하면 이동 거리 계산
        move = bad_char.get(text[i + m - 1], m)
        i += move

    return -1


def build_bad_char_table(pattern):
    table = {}
    length = len(pattern)
    for i in range(length - 1):
        table[pattern[i]] = length - 1 - i
    return table


if __name__ == "__main__":
    main()
