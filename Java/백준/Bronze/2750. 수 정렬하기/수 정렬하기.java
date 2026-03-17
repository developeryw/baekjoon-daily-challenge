import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int[] number = new int[n];

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      number[i] = Integer.parseInt(st.nextToken());
    }

    for (int i = 0; i < n - 1; i++) {
      for (int j = 0; j < n - 1; j++) {
        if (number[j] > number[j + 1]) {
          int temp = number[j + 1];
          number[j + 1] = number[j];
          number[j] = temp;
        }
      }
    }

    for (int item: number) {
      System.out.println(item);
    }
  }
}
