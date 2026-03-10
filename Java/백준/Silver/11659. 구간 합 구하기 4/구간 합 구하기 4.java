import java.io.*;
import java.util.StringTokenizer;

public class Main {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    int[] numbers = new int[n + 1];

    st = new StringTokenizer(br.readLine());

    for (int i = 1; i < n + 1; i++) {
      numbers[i] = numbers[i - 1] + Integer.parseInt(st.nextToken());
    }

    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());

      sb.append(numbers[end] - numbers[start - 1]).append('\n');
    }

    System.out.print(sb);
  }
}
