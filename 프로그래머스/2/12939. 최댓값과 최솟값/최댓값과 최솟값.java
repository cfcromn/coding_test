class Solution {
    public String solution(String s) {
        String[] array = s.split(" ");
        int max = Integer.valueOf(array[0]);
        int min = Integer.valueOf(array[0]);
        for (int i = 1; i < array.length; i++) {
            int arrayValue = Integer.valueOf(array[i]);
            if (max < arrayValue) {
                max = arrayValue;
            }
            if (min > arrayValue) {
                min = arrayValue;
            }
        }
        String maxMinStr = String.valueOf(min) + " " + String.valueOf(max);
        return maxMinStr;
    }
}