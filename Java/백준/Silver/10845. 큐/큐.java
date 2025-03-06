import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        Queue<Integer> queue = new LinkedList<>();
        int last = 0;

        for (int i = 0; i < N; i++) {
            String[] arr = sc.nextLine().split(" ");

            switch (arr[0]) {
                case "push":
                    last = Integer.parseInt(arr[1]);
                    queue.add(last);
                    break;
                case "pop":
                    if (queue.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(queue.poll());
                    }
                    break;
                case "size":
                    System.out.println(queue.size());
                    break;
                case "empty":
                    if (queue.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                case "front":
                    if (queue.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(queue.peek());
                    }
                    break;
                case "back":
                    if (queue.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(last);
                    }
                    break;
            }
        }
    }
}
