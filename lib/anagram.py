# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = sorted(word)

    def match(self, l):
        matchedList = []
        for x in l:
            if sorted(x) == self.word:
                matchedList.append(x)
        return matchedList