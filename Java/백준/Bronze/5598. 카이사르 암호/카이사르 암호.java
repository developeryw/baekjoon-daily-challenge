import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] chr = sc.nextLine().toCharArray();

        for (char c : chr) {
            int n = (int)c;

            if (n < 68) {
                System.out.print((char)(c + 23));
            } else {
                System.out.print((char)(c - 3));
            }
        }
    }
}