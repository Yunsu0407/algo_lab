def dfs(graph, start, visited):
    visited[start] = True
    print(f"현재 방문 중인 노드의 번호 : {start}")

    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)


def main():
    n = int(input("노드의 개수를 입력하세요 : "))

    graph = [[] for _ in range(n)]

    # 각 노드의 인접 리스트 입력
    for i in range(n):
        print("인접한 노드 입력을 종료하시려면 -1을 입력하세요")
        while True:
            v = int(input(f"{i}노드에 인접한 노드를 입력하세요 : "))
            if v == -1:
                break
            graph[i].append(v)

    # 그래프 정보 출력
    print("\n***********그래프 정보 출력!**********")
    for i in range(n):
        print(f"{i}번째 노드의 인접한 노드 :", *graph[i])

    # DFS 시작
    print("\n***********DFS 시작!**********")
    start = int(input("탐색시작 지점을 입력하세요 : "))

    print("탐색 순서는 다음과 같습니다.")
    visited = [False] * n
    dfs(graph, start, visited)


if __name__ == "__main__":
    main()
