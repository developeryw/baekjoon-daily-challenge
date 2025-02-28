import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int result = 0;
        int minimum = 99;

        for (int i = 0; i < 7; i++) {
            int n = sc.nextInt();

            if (n % 2 != 0) {
                result += n;

                if (n < minimum) {
                    minimum = n;
                }
            }
        }

        if (result == 0) {
            System.out.println(-1);
        } else {
            System.out.println(result);
            System.out.println(minimum);
        }
    }
}