import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for (int i = 0; i < a.length(); i++) {
            char ch = a.charAt(i);
            
            if (ch >= 'A' && ch <= 'Z') {
                System.out.print((char)(ch + 32));
            } else {
                System.out.print((char)(ch - 32));
            }
        }
        
        sc.close();
    }
}