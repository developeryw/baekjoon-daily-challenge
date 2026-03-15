import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());

    Stack<Integer> stack = new Stack<>();
    ArrayList<String> result = new ArrayList<>();
    boolean possible = true;

    int cnt = 1; // 스택에 push 하기를 대기하는 숫자
    // 오름차순으로 넣기 때문에 변수 하나만 사용해서 조건에 따라 +1 하는 방식 채택

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int goal = Integer.parseInt(st.nextToken());

      if (stack.empty()) {
        while (cnt <= goal) {
          stack.add(cnt);
          result.add("+");
          cnt++;
        }
      }

      if (stack.peek() == goal) {
        stack.pop();
        result.add("-");
      } else if (stack.peek() < goal) {
        while (cnt <= goal) {
          stack.add(cnt);
          result.add("+");
          cnt++;
        }

        stack.pop();
        result.add("-");
      } else {
        possible = false;
      }
    }

    if (possible) {
      for (String item: result) {
        System.out.println(item);
      }
    } else {
      System.out.println("NO");
    }
  }
}
