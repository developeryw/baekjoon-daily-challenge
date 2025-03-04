import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < N; i++) {
            String[] arr = sc.nextLine().split("");
            Deque<Integer> stack = new ArrayDeque<>();
            int theEnd = 0;

            for (int j = 0; j < arr.length; j++) {
                if (arr[j].equals("(")) {
                    stack.push(1);
                } else {
                    if (stack.isEmpty()) {
                        System.out.println("NO");
                        theEnd = 1;
                        break;
                    } else {
                        stack.pop();
                    }
                }
            }

            if (theEnd == 0) {
                if (stack.isEmpty()) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }
}
