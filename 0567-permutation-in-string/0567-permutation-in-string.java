class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] count1 = new int[26];
        int[] count2 = new int[26];

        // frequency for s1 and first window
        for (int i = 0; i < s1.length(); i++) {
            count1[s1.charAt(i) - 'a']++;
            count2[s2.charAt(i) - 'a']++;
        }

        // slide window
        for (int i = s1.length(); i < s2.length(); i++) {
            if (matches(count1, count2)) return true;

            // remove char going out of window
            count2[s2.charAt(i - s1.length()) - 'a']--;
            // add new char coming into window
            count2[s2.charAt(i) - 'a']++;
        }

        return matches(count1, count2);
    }

    private boolean matches(int[] count1, int[] count2) {
        for (int i = 0; i < 26; i++) {
            if (count1[i] != count2[i]) return false;
        }
        return true;
    }
}
