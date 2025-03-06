import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] alphabet = new int[26];
        for (int i = 0; i < alphabet.length; i++) {
            alphabet[i] = -1;
        }

        char[] arr = sc.nextLine().toCharArray();

        for (int i = arr.length - 1; i >= 0; i--) {
            int cur = arr[i] - 'a';

            alphabet[cur] = i;
        }

        for (int i = 0; i < alphabet.length; i++) {
            System.out.print(alphabet[i] + " ");
        }
    }
}