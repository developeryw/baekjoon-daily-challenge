import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    PriorityQueue<Integer> pq = new PriorityQueue<>((n1, n2) -> {
      // n1이 n2보다 절댓값이 더 작거나 음수여서 먼저 큐를 나와야 한다면 (우선순위가 낮아야 한다면)
      // 이 함수는 음수는 반환해야 하므로 아래와 같이 작성함.

      int n1_abs = Math.abs(n1);
      int n2_abs = Math.abs(n2);

      if (n1_abs == n2_abs) {
        return n1 > n2 ? 1 : -1;
      }

      return n1_abs - n2_abs;

    });

    for(int i = 0; i < N; i++) {
      int cur = Integer.parseInt(br.readLine());

      if (cur == 0) {
        if (pq.isEmpty()) {
          System.out.println(0);
        } else {
          System.out.println(pq.poll());
        }
      } else {
        pq.add(cur);
      }
    }
  }
}
