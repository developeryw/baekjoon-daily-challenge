import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    String str = scanner.nextLine();
    int n = Integer.parseInt(str); // 시험장 개수

    int[] a = new int[n];
    for (int i = 0; i < n; i++) {
      str = scanner.next();
      a[i] = Integer.parseInt(str);
    } // i번째 시험장에 있는 응시자 수

    int b = scanner.nextInt(); // 총감독관이 한 시험장에서 감시할 수 있는 응시자 수

    int c = scanner.nextInt(); // 부감독관이 한 시험장에서 감시할 수 있는 응시자 수

    // 조건: 각 시험장에 총감독관은 1명, 부감독관은 여러 명이어도 상관없음.

    // 구해야 하는 것: 최소 감독관 수
    long total = 0; // int 오버플로우 주의

    /* 해결 방법
    1. 각 시험장(정수 배열)에서 총감독관 감시 가능 응시자 수를 뺀다. (+1)
    2. 남은 응시자 수를 부감독관 감시 가능 응시자 수로 나눈다. (몫 계산)
    3. 나머지가 있다면 부감독관을 추가한다. (+1)
    */

    for (int i = 0; i < n; i++) {
      total += 1;
      a[i] -= b; // 총감독관이 감시 가능한 응시자 수 처리

      if (a[i] <= 0){
        continue;
      } // 부감독이 필요없다면

      total += a[i] / c; // 부감독관이 감시 가능한 응시자 수 처리
      a[i] = a[i] % c;

      if (a[i] % c > 0) {
        total += 1;
      } // 나머지에 대해 부감독관 1명 추가

    }

    System.out.println(total);
  }
}
