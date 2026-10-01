class Solution {
    public int solution(int n) {
        int answer = 1;
        
        while (true) {
            int pizza = answer * 6;
            
            if (pizza % n == 0 && pizza % 6 == 0) {
                break;
            }
            
            answer++;
        }
        
        return answer;
    }
}