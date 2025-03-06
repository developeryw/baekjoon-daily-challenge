import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        String[] numbers = sc.nextLine().split(" ");
        int maximum = -1000000;
        int minimum = 1000000;

        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(numbers[i]);

            if (number > maximum) {
                maximum = number;
            }

            if (number < minimum) {
                minimum = number;
            }
        }

        System.out.println(minimum + " " + maximum);
    }
}
