class Solution {
    public double solution(int[] arr) {
        double t = 0;
        for (int i:arr) {
            t += i;
        }
        double p = t / arr.length;
        return p;
    }
}