class Solution {
    public int[] solution(int n) {
        int len = 0;
        
        if (n % 2 == 0) {
            len = n / 2;
        } else {
            len = n / 2 + 1;
        }
        
        int[] answer;
        answer = new int[len];
        
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                answer[i / 2] = i;
            }
        }
        
        return answer;
    }
}