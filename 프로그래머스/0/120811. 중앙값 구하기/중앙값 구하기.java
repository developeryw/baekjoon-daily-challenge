class Solution {
    public int solution(int[] array) {
        while(true) {
        int i = 0;
        int cnt = 0;

        for (int j = i; j < array.length - 1; j++) {
          if (array[j] > array[j + 1]) {
            int temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;

            cnt++;
          }
        }

        if (cnt == 0) {
          break;
        }
      }

      int answer = array[array.length / 2];
        
        return answer;
    }
}