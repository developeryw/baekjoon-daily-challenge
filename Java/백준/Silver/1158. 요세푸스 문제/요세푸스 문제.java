import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        Deque<Integer> deque = new ArrayDeque<>();
        Deque<Integer> result = new ArrayDeque<>();

        for (int i = 1; i < N + 1; i++) {
            deque.addLast(i);
        }

        System.out.print("<");

        while (!deque.isEmpty()) {
            int cur = 0;
            for (int j = 0; j < K - 1; j++) {
                cur = deque.removeFirst();
                deque.addLast(cur);
            }

            cur = deque.removeFirst();
            if (deque.size() == 0) {
                System.out.print(cur);
            } else {
                System.out.print(cur + ", ");
            }
        }
        System.out.print(">");
    }
}
