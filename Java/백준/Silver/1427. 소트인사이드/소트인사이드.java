import java.io.*;
import java.util.*;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    String n = sc.nextLine();

    int[] numbers = new int[n.length()];
    int idx = 0;

    for (char c : n.toCharArray()) {
      numbers[idx] = c - '0';
      idx++;
    }

    for (int i = 0; i < numbers.length - 1; i++) {
      for (int j = i + 1; j < numbers.length; j++) {
        if (numbers[i] < numbers[j]) {
          int temp = numbers[i];
          numbers[i] = numbers[j];
          numbers[j] = temp;
        }
      }
    }

    for (int item: numbers) {
      System.out.print(item);
    }
  }

}
