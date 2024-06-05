class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if len(words) < 2:
            return words
        first_word = set(words[0])
        letters = []
        for letter in first_word:
            n = min([word.count(letter) for word in words])

            if n:
                letters += [letter] * n
        return letters


sol = Solution()
print(sol.commonChars(words=["bella", "label", "roller"]))
