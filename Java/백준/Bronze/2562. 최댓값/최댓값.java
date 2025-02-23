import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int maximum = 0;
        int maxIndex = 0;

        for (int i = 1; i < 10; i++) {
            int n = sc.nextInt();

            if (maximum < n) {
                maximum = n;
                maxIndex = i;
            }
        }

        System.out.println(maximum);
        System.out.println(maxIndex);
    }
}