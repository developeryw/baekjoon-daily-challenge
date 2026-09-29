import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = Arrays.copyOf(numbers, numbers.length);

        for (int i = 0; i < numbers.length; i++) {
            answer[i] = numbers[i] * 2;
        }

        return answer;
    }
}