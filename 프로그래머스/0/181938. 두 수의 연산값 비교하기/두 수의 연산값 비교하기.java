class Solution {
    public int solution(int a, int b) {
        String sa = Integer.toString(a);
        String sb = Integer.toString(b);
        
        int ab = Integer.parseInt(sa + sb);
        int ab2 = a * b * 2;
        
        int answer = 0;
        
        if (ab > ab2) {
            answer = ab;
        } else {
            answer = ab2;
        }
        
        return answer;
    }
}