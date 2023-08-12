class Anagram:
    def __init__(self, word):
        self.letters = sorted([letter for letter in word])

    def match(self, word_list):
        match_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.letters:
                match_list.append(word)

        return match_list