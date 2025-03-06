import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int n = sc.nextInt();
            String s = Integer.toBinaryString(n);

            int index = 0;
            for (int j = s.length() - 1; j >= 0; j--) {
                if (s.charAt(j) == '1') {
                    System.out.print(index + " ");
                }

                index++;
            }

              System.out.println();
            }
    }
}