class Solution {
    public String solution(String s) {
        String answer = "";
        int c = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == (' ')) {
                answer += ' ';
                c++;
            } else if (c >= 1) {
                answer += Character.toUpperCase(s.charAt(i));
                c = 0;
            } else if (i == 0) {
                answer += Character.toUpperCase(s.charAt(i));
                c = 0;
            } else {
                answer += Character.toLowerCase(s.charAt(i));
                c = 0;
            }
        }
        return answer;
    }
}