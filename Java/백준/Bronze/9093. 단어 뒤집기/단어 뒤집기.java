import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = Integer.parseInt(sc.nextLine());

        while (T-- > 0) {
            String[] str = sc.nextLine().split(" ");

            for (String s : str) {
                StringBuilder sb = new StringBuilder(s);
                System.out.print(sb.reverse().toString() + " ");
            }

            System.out.println();
        }

        sc.close();
    }
}