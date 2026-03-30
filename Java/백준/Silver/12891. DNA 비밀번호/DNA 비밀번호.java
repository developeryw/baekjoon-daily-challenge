import java.io.*;
import java.util.*;

public class Main {
  static int[] cur = new int[4];
  static int[] check = new int[4];
  static int isCorrect = 0;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int S = Integer.parseInt(st.nextToken());
    int P = Integer.parseInt(st.nextToken());

    int result = 0;

    char[] dna = br.readLine().toCharArray();

    st = new StringTokenizer(br.readLine());

    for (int i = 0; i < 4; i++) {
      check[i] = Integer.parseInt(st.nextToken());

      if (check[i] == 0) {
        isCorrect++;
      }
    }

    for (int i = 0; i < P; i++) {
      Add(dna[i]);
    }

    if (isCorrect == 4) {
      result += 1;
    }

    for (int i = P; i < S; i++) {
      int j = i - P;

      Add(dna[i]);
      Remove(dna[j]);

      if (isCorrect == 4) {
        result += 1;
      }
    }

    System.out.println(result);
  }

  private static void Add(char c) {
    switch(c) {
      case 'A':
        cur[0]++;
        if (cur[0] == check[0]) {
          isCorrect++;
        }
        break;
      case 'C':
        cur[1]++;
        if (cur[1] == check[1]) {
          isCorrect++;
        }
        break;
      case 'G':
        cur[2]++;
        if (cur[2] == check[2]) {
          isCorrect++;
        }
        break;
      case 'T':
        cur[3]++;
        if (cur[3] == check[3]) {
          isCorrect++;
        }
        break;
    }
  }

  private static void Remove(char c) {
    switch(c) {
      case 'A':
        if (cur[0] == check[0]) {
          isCorrect--;
        }
        cur[0]--;
        break;
      case 'C':
        if (cur[1] == check[1]) {
          isCorrect--;
        }
        cur[1]--;
        break;
      case 'G':
        if (cur[2] == check[2]) {
          isCorrect--;
        }
        cur[2]--;
        break;
      case 'T':
        if (cur[3] == check[3]) {
          isCorrect--;
        }
        cur[3]--;
        break;
    }
  }
}
