class Solution {
    public int solution(int[] array) {
        int[] cnt;
        cnt = new int[1001];
        
        for (int i = 0; i < array.length; i++) {
            cnt[array[i]]++;
        }
            
        int answer = 0;
        int isOnly = 1;
        int maximum = cnt[0];
        int cur = 0;
        
        for (int j = 1; j < cnt.length; j++) {
            if (cnt[j] > maximum) {
                maximum = cnt[j];
                isOnly = 1;
                cur = j;
            } else if (cnt[j] == maximum) {
                isOnly++;
                cur = j;
            }
        }
        
        if (isOnly == 1) {
            answer = cur;
        } else {
            answer = -1;
        }
        
        return answer;
    }
}