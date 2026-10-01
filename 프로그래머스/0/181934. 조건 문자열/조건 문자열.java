class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        String str = ineq + eq;
        boolean result = true;
        
        if (str.equals(">=")) {
            result = (n >= m);
        } else if (str.equals("<=")) {
            result = (n <= m);
        } else if (str.equals(">!")) {
            result = (n > m);
        } else {
            result = (n < m);
        }
        
        if (result) {
            answer = 1;
        }
        
        return answer;
    }
}