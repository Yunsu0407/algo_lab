def main():
    test = False
    text = "Human Computer Interaction Lab, Jin-Woo Jung, Algorithm Lab Work6"
    if test:
        pattern = "Work6"
        # pattern = "Human"
        # pattern = "human"
    else:
        pattern = input("찾을 패턴을 입력하세요 : ")

    idx = kmp_search(text, pattern)
    if idx != -1:
        print(f"패턴이 인덱스 {idx} 에서 발견되었습니다.")
        print("해당 패턴을 찾았습니다.")
    else:
        print("해당 패턴을 찾지 못했습니다.")


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    i = j = 0  # i: text 인덱스, j: pattern 인덱스

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:  # 패턴을 모두 찾음
            return i - j  # 시작 인덱스 반환
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # 이전까지 일치한 접두사/접미사의 길이
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


if __name__ == "__main__":
    main()
