import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());

    int result = 0;

    for (int i = 1; i < n + 1; i++) {
      int start = i;
      int total = 0;

      while (total <= n) {
        total += start;

        if (total == n) {
          result += 1;
        }

        start++;
      }
    }

    System.out.println(result);
  }
}
