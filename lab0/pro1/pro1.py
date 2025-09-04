class stack1:
    def __init__(self, maxindex):
        self.point = 0
        self.maxindex = maxindex
        self.stack = []

    def __del__(self):
        print("종료 시점 포인트 위치 : " + str(self.point))
        print("종료 시점 데이터 상태 : ")
        print(self.stack)

    def push(self, v):
        self.point += 1
        self.stack.append(v)

    def pop(self):
        self.point -= 1
        temp = self.stack[self.point]
        self.stack.pop()
        return temp

    def empty(self):
        if not self.stack:
            return True
        else:
            return False

    def cur_print(self):
        print("현재 시점 포인트 위치 : " + str(self.point))
        print("현재 데이터 상태 : ")
        print(self.stack)


def main():
    input = "9  10  15  4  *  +  20  *  7  + +"
    list = input.split()  # 입력을 분할하여 리스트에 저장
    stack = stack1(len(list))  # 리스트의 크기를 전달하며 스택 생성

    for curr in list:  # 리스트의 크기만큼 반복
        value = None

        if curr.isdigit():  # 현재 값이 정수인 경우
            value = curr
        else:  # 현재 값이 연산자인 경우
            num1 = int(stack.pop())
            num2 = int(stack.pop())

            # 스택 상단에 있는 두 숫자를 꺼내서 연산
            if curr == "+":
                value = num1 + num2
            else:
                value = num1 * num2

        stack.push(value)  # 계산된 값을 다시 스택에 저장
        stack.cur_print()

    fin = stack.pop()
    print(f"최종 데이터 :{fin}")


if __name__ == "__main__":
    main()
