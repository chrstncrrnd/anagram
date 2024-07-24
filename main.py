from math import prod

# in order of most used in order to save memory
char2prime = {
    "e": 2,
    "t": 3,
    "a": 5,
    "o": 7,
    "i": 11,
    "n": 13,
    "s": 17,
    "h": 19,
    "r": 23,
    "d": 29,
    "l": 31,
    "c": 37,
    "u": 41,
    "m": 43,
    "w": 47,
    "f": 53,
    "g": 59,
    "y": 61,
    "p": 67,
    "b": 71,
    "v": 73,
    "k": 79,
    "j": 83,
    "x": 89,
    "q": 97,
    "z": 101,
}
def wordToNumber(word):
    return prod([char2prime.get(c) for c in [*word]])

def getWords():
    wordFile = open("words_fixed.txt", "r")
    words = wordFile.read().splitlines()
    wordFile.close()
    return list(filter(onlyCommonLetters, words))



def onlyCommonLetters(candidate):
    # I actually don't even know how I came up with this algorithm wtf
    candidateNumber = wordToNumber(candidate)

    return initialNumber % candidateNumber == 0
    


def continueRecursive(currentWordNumber: int, currentWordList: list):
    if currentWordNumber == 1:
        currentWordList.sort()
        allCombinations.append(" ".join(currentWordList))
        return
    for word in words:
        wNum = wordToNumber(word)
        if currentWordNumber % wNum == 0:
            continueRecursive(currentWordNumber / wNum, [*currentWordList, word])


if __name__ == "__main__":
    initial = input("What sentence do you want to anagramify? ").lower().strip().replace(" ", "")
    print("Generating anagram")
    initialNumber = wordToNumber(initial)
    words: list = getWords()

    allCombinations = []
    continueRecursive(initialNumber, [])
    allCombinations = list(set(allCombinations))
    
    print(allCombinations)

