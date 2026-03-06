import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);

    int n = scanner.nextInt(); // 숫자 개수 n
    String array = scanner.next(); // 문자열로 입력 받기

    int total = 0;

    for (int i = 0; i < n; i++) {
      total += array.charAt(i) - '0';
      // charAt() 사용해서 한 문자씩 추출한 후 - '0' 처리하여 정수로 바꾸기
    }

    System.out.println(total);
   }
}
