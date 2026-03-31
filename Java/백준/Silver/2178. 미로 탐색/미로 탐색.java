import java.io.*;
import java.util.*;

public class Main {
  static int[][] maze;
  static boolean[][] visited;
  static int N, M;

  static int[] dx = {-1, 0, 1, 0};
  static int[] dy = {0, -1, 0, 1};

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    maze = new int[N][M];
    visited = new boolean[N][M];

    for (int i = 0; i < N; i++) {
      String temp = br.readLine();

      for (int j = 0; j < M; j++) {
        maze[i][j] = Integer.parseInt(temp.substring(j, j+1));
      }
    }

    BFS(0, 0);

    System.out.println(maze[N - 1][M - 1]);
  }

  private static void BFS(int start_x, int start_y) {
    Queue<int[]> queue = new LinkedList<>();
    queue.offer(new int[] {start_x, start_y});
    visited[start_x][start_y] = true;

    while (!queue.isEmpty()) {
      int[] cur = queue.poll();

      for (int i = 0; i < 4; i++) {
        // 현재 위치에서 상하좌우 탐색
        int x = cur[0] + dx[i];
        int y = cur[1] + dy[i];

        if (x >= 0 && y >= 0 && x < N && y < M) { // x, y 좌표가 미로 안이라면
          if (maze[x][y] != 0 && !visited[x][y]) { // 미로에서 해당 위치가 1이고, 아직 방문하지 않았다면
            visited[x][y] = true;
            maze[x][y] = maze[cur[0]][cur[1]] + 1;
            queue.add(new int[] {x, y});
          }
        }
      }
    }
  }
}
