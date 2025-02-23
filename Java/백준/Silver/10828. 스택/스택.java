import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            String[] s = sc.nextLine().split(" ");

            if ((s[0].equals("pop") || s[0].equals("top") && stack.isEmpty()) && stack.isEmpty()) {
                System.out.println(-1);
                continue;
            }

            if (s[0].equals("push")) {
                stack.push(Integer.parseInt(s[1]));
            } else if (s[0].equals("pop")) {
                System.out.println(stack.pop());
            } else if (s[0].equals("size")) {
                System.out.println(stack.size());
            } else if (s[0].equals("empty")) {
                System.out.println(stack.isEmpty() ? 1 : 0);
            } else if (s[0].equals("top")) {
                System.out.println(stack.peek());
            }
        }
    }
}