class Solution {
    public int solution(int num1, int num2) {
        float n1 = num1;
        float n2 = num2;
        
        int answer = (int) ((n1 / n2) * 1000) ;
        return answer;
    }
}