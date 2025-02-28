import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            for (int j = N - 1; j > i; j--) {
                System.out.print(" ");
            }

            for (int k = 0; k < i + 1; k++) {
                System.out.print("*");
            }

            for (int l = 0; l < i; l++) {
                System.out.print("*");
            }

            System.out.println();
        }

        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j < i + 1; j++) {
                System.out.print(" ");
            }

            for (int k = N - 1; k > i; k--) {
                System.out.print("*");
            }

            for (int l = 0; l < N - i - 2; l++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}