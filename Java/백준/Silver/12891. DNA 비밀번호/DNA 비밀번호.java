import java.io.*;
import java.util.*;

public class Main {
  static int[] myArr; // 현재 부분문자열에서 각 DNA 개수
  static int[] checkArr; // 비밀번호가 되는 조건
  static int checkSecret; // A, C, T, G가 전부 만족하는지

  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int s = Integer.parseInt(st.nextToken());
    int p = Integer.parseInt(st.nextToken());

    int result = 0; // 최종 정답 저장 (가능한 비밀번호 개수)
    myArr = new int[4];
    checkArr = new int[4];
    checkSecret = 0;

    char[] dna = br.readLine().toCharArray();

    st = new StringTokenizer(br.readLine());

    for (int i = 0; i < 4; i++) {
      checkArr[i] = Integer.parseInt(st.nextToken());

      if (checkArr[i] == 0) { // 0이면 이미 조건 만족
        checkSecret++;
      }
    }

    for (int i = 0; i < p; i++) { // 초기 부분 문자열 세팅
      Add(dna[i]);
    }

    if (checkSecret == 4) { // 초기 문자열이 조건을 만족한다면
      result++;
    }

    // 슬라이딩 윈도우 사용
    for (int i = p; i < s; i++) { // 오른쪽 포인터
      int j = i - p; // 왼쪽 포인터
      // 범위를 유지하면서 한 칸씩 이동

      Add(dna[i]);
      Remove(dna[j]);

      if (checkSecret == 4) {
        result++;
      }
    }

    System.out.println(result);

    br.close();
  }

  private static void Add(char c) {
    switch (c) {
      case 'A':
        myArr[0]++;
        if (myArr[0] == checkArr[0]) {
          checkSecret++;
        }
        break;
      case 'C':
        myArr[1]++;
        if (myArr[1] == checkArr[1]) {
          checkSecret++;
        }
        break;
      case 'G':
        myArr[2]++;
        if (myArr[2] == checkArr[2]) {
          checkSecret++;
        }
        break;
      case 'T':
        myArr[3]++;
        if (myArr[3] == checkArr[3]) {
          checkSecret++;
        }
        break;
    }
  }

  private static void Remove(char c) {
    switch (c) {
      case 'A':
        if (myArr[0] == checkArr[0]) {
          checkSecret--;
        }
        myArr[0]--;
        break;
      case 'C':
        if (myArr[1] == checkArr[1]) {
          checkSecret--;
        }
        myArr[1]--;
        break;
      case 'G':
        if (myArr[2] == checkArr[2]) {
          checkSecret--;
        }
        myArr[2]--;
        break;
      case 'T':
        if (myArr[3] == checkArr[3]) {
          checkSecret--;
        }
        myArr[3]--;
        break;
    }
  }
}
