import java.lang.Math;

class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {0, 0};
        
        int numer = numer1 * denom2 + numer2 * denom1;
        int denom = denom1 * denom2;

        int minimum = Math.min(numer, denom);
        int gcd = 1;
        
        for (int i = 2; i <= minimum; i++) {
            if (numer % i == 0 && denom % i == 0) {
                gcd = i;
            }
        }
        
        answer[0] = numer / gcd;
        answer[1] = denom / gcd;
        
        return answer;
    }
}