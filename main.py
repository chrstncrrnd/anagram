from math import prod

char2prime = {
    "a": 2,
    "b": 3,
    "c": 5,
    "d": 7,
    "e": 11,
    "f": 13,
    "g": 17,
    "h": 19,
    "i": 23,
    "j": 29,
    "k": 31,
    "l": 37,
    "m": 41,
    "n": 43,
    "o": 47,
    "p": 53,
    "q": 59,
    "r": 61,
    "s": 67,
    "t": 71,
    "u": 73,
    "v": 79,
    "w": 83,
    "x": 89,
    "y": 97,
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
    


def continueRecursive(currentWordNumber: int, currentWordList: list, checked: list):
    if currentWordNumber == 1:
        allCombinations.append(currentWordList)
        return
    cWords = filter(lambda x: not x in checked, words)
    for word in cWords:
        wNum = wordToNumber(word)
        if currentWordNumber % wNum == 0:
            continueRecursive(currentWordNumber / wNum, [*currentWordList, word], [*checked, word])


if __name__ == "__main__":
    initial = input("What sentence do you want to anagramify? ").lower().strip().replace(" ", "")
    print("Generating anagram")
    initialNumber = wordToNumber(initial)
    words: list = getWords()

    allCombinations = []
    continueRecursive(initialNumber, [], [])
    print(allCombinations)

