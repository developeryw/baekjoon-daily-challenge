import java.io.*;
import java.util.*;

public class Main {
  static int N, M;
  static boolean[] visited;
  static ArrayList<Integer>[] graph; // 각 요소가 정수인 리스트를 배열로
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    visited = new boolean[N + 1];

    graph = new ArrayList[N + 1];
    for (int i = 1; i < N + 1; i++) {
      graph[i] = new ArrayList<Integer>(); // 초기화
    }

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int u = Integer.parseInt(st.nextToken());
      int v = Integer.parseInt(st.nextToken());

      // 방향성이 없는 그래프의 형태이므로 양쪽 다 넣어줘야 함.
      graph[u].add(v);
      graph[v].add(u);
    }

    int cnt = 0;

    for (int i = 1; i < N + 1; i++) {
      if (!visited[i]) {
        DFS(i); // DFS가 한 차례 끝나면
        cnt++; // 개수 + 1
      }
    }

    System.out.println(cnt);
  }

  private static void DFS(int V) {
    if (visited[V]) { // 이미 방문했으면 탐색 끝내기
      return;
    }

    visited[V] = true; // 방문했다고 표시

    for (int i : graph[V]) { // 현재 노드와 이어진 다른 노드 중
      if (!visited[i]) { // 방문하지 않은 노드 탐색하기
        DFS(i);
      }
    }
  }
}
