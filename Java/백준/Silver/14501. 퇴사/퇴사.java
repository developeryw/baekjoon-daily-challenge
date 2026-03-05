import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    String str = scanner.next();
    int n = Integer.parseInt(str); // 퇴사까지 남은 n일

    int[] day = new int[n]; // i일에 잡혀있는 상담에 걸리는 일수
    int[] price = new int[n]; // i일에 잡혀있는 상담의 금액

    for (int i = 0; i < n; i++) {
      day[i] = scanner.nextInt();
      price[i] = scanner.nextInt();
    }

    /* 해결 방법
    1. n -> 1 역행 (1부터 하면 중간에 여러 가지 선택지가 있을 때 비교하기 어려움)
    2. 이때 i일에서의 최대값을 저장하는 별도의 배열 maximum 사용
    3. i + 1일에서 최댓값과 i일을 선택했을 때의 값(Pi + P(i + Ti)) 비교
       즉, i일을 선택했을 때와 선택하지 않았을 때를 비교
    4. 더 큰 값을 maximum[i]에 넣어두기
     */

    int[] maximum = new int[n + 1];
    maximum[n] = 0;

    for (int i = n - 1; i >= 0; i--) {
      if (i + day[i] <= n) { // i를 선택했을 때 퇴사까지 남은 일수를 넘지 않도록 해야 함.
        maximum[i] = Math.max(maximum[i + 1], price[i] + maximum[i + day[i]]);
      } else {
        maximum[i] = maximum[i + 1];
      }
    }

    System.out.println(maximum[0]);
  }
}
