import java.util.*;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    Deque<Integer> deque = new ArrayDeque<>();

    for (int i = 1; i < n + 1; i++) {
      deque.addLast(i);
    }

    int temp;

    while (true) {
      if (n == 1) {
        System.out.println(1);
        break;
      }
      
      temp = deque.pollFirst();

      if (deque.size() <= 1) {
        System.out.println(deque.pollLast());
        break;
      }

      temp = deque.pollFirst();
      deque.addLast(temp);
    }
  }
}
