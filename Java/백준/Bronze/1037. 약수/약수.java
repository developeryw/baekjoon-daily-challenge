import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        String[] divisors = sc.nextLine().split(" ");

        int max = 0;
        int min = 999999;

        for (int i = 0; i < N; i++) {
            int cnt = Integer.parseInt(divisors[i]);

            if (cnt > max) {
                max = cnt;
            }

            if (cnt < min) {
                min = cnt;
            }
        }

        System.out.println(max * min);
    }
}