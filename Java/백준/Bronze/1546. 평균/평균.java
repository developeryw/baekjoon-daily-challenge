import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        String[] scores = sc.nextLine().split(" ");
        double maxScore = 0;
        double result = 0;

        for (int i = 0; i < N; i++) {
            int score = Integer.parseInt(scores[i]);

            if (score > maxScore) {
                maxScore = score;
            }
        }

        for (int i = 0; i < N; i++) {
            int score = Integer.parseInt(scores[i]);

            result += (score / maxScore * 100);
        }

        result /= N;

        System.out.println(result);
    }
}