from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(f"현재 방문 중인 노드의 번호: {node}")

        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)


def main():
    n = int(input("노드의 개수를 입력하세요: "))

    graph = [[] for _ in range(n)]

    # 각 노드의 인접 리스트 입력
    for i in range(n):
        print("인접한 노드 입력을 종료하시려면 -1을 입력하세요")
        while True:
            v = int(input(f"{i} 노드에 인접한 노드를 입력하세요: "))
            if v == -1:
                break
            graph[i].append(v)

    # 그래프 정보 출력
    print("***********그래프 정보 출력!**********")
    for i in range(n):
        print(f"{i}번째 노드의 인접한 노드:", *graph[i])

    # BFS 시작
    start = int(input("탐색 시작 지점을 입력하세요: "))

    print("***********BFS 시작!**********")
    print("탐색 순서는 다음과 같습니다.")

    visited = [False] * n
    bfs(graph, start, visited)


if __name__ == "__main__":
    main()
