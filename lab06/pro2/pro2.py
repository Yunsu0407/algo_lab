def main():
    test = False
    txt_ex = "Human Computer Interaction Lab, Jin-Woo Jung, Algorithm Lab Work6"  # text of example
    if test:
        txt_tg = "Work6"  # text of target
        # target = "Human"
        # target = "human"
    else:
        txt_tg = input("찾을 패턴을 입력하세요 : ")  # text of target

    ans_idx = find_target(txt_ex, txt_tg)  # answer index

    if ans_idx >= 0:
        ans = f"패턴이 인덱스 {ans_idx}에서 발견되었습니다.\n해당 패턴을 찾았습니다."
    else:
        ans = "해당 패턴을 찾지 못했습니다."

    print(ans)


# Example에서 Target을 찾는 함수
def find_target(txt_ex, txt_tg):
    base = 62
    div = 101  # div = divisor
    len_ex = len(txt_ex)  # length of example
    len_tg = len(txt_tg)  # length of target

    h_ex = hashing(base, div, txt_ex[0:len_tg])  # hashed_example
    h_tg = hashing(base, div, txt_tg)  # hashed_target

    for i in range(0, len_ex - len_tg + 1):
        if h_tg == h_ex:
            if txt_ex[i : i + len_tg] == txt_tg:
                return i

        # 롤링 해쉬, (조건 => 마지막 인덱스에서 다음 해쉬를 구할 필요 없음)
        if i < len_ex - len_tg:
            # 이전 문자열의 맨 앞 해쉬 값 제거
            h_ex = (h_ex - ord(txt_ex[i]) * pow(base, len_tg - 1, div)) % div
            # 추가되는 문자의 해쉬값 가산
            h_ex = (h_ex * base + ord(txt_ex[len_tg + i])) % div

    return -1


# 문자열을 해쉬값으로 변환하는 함수
def hashing(base, div, text):
    result = 0
    for i in range(len(text)):
        result = (result * base + ord(text[i])) % div

    return result % div


if __name__ == "__main__":
    main()
