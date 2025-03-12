import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] floor = new int[N][M];

        for (int i = 0; i < N; i++) {
            char[] arr = sc.next().toCharArray();

            for (int j = 0; j < M; j++) {
                floor[i][j] = (arr[j] == '-' ? 0 : 1);
            }
        }

        int row = 0;
        int col = 0;

        int cnt = 0;
        int cur;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cur = floor[i][j];

                row = i;
                col = j;

                if (cur == -1) {
                    continue;
                }

                floor[i][j] = -1;

                if (cur == 0) {
                    col++;

                    while ((col < M) && (floor[row][col] == 0)) {
                        floor[row][col] = -1;
                        col++;
                    }

                    cnt++;
                } else if (cur == 1) {
                    row++;

                    while ((row < N) && (floor[row][col] == 1)) {
                        floor[row][col] = -1;
                        row++;
                    }

                    cnt++;
                }
            }
        }

        System.out.println(cnt);
        
        sc.close();
    }
}
