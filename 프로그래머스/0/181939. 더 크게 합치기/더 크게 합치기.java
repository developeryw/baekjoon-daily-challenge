class Solution {
    public int solution(int a, int b) {
        String str = "";
        String sa = Integer.toString(a);
        String sb = Integer.toString(b);
        
        int ab = Integer.parseInt(sa + sb);
        int ba = Integer.parseInt(sb + sa);
        
        int answer = 0;
        
        if (ab > ba) {
            answer = ab;
        } else {
            answer = ba;
        }
        
        return answer;
    }
}