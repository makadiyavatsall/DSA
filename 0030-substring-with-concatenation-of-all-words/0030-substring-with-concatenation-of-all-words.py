class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        k = len(words)
        window_size = word_len * k
        n = len(s)

        target = Counter(words)
        res = []

        # We try all possible offsets: 0 .. word_len-1
        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0  # number of valid words matched in current window

            # Move right in steps of word_len
            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    seen[word] += 1
                    count += 1

                    # If word appears too many times, shrink window from left
                    while seen[word] > target[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If we matched all words, record the start index
                    if count == k:
                        res.append(left)

                        # Move window forward by one word
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Invalid word → reset window
                    seen.clear()
                    count = 0
                    left = right + word_len

        return res