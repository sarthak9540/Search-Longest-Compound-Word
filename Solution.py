import time

def SearchLongestCompoundWord(wordsList):
    longest = ""
    secondLongest = ""
    dp = {}
    wordsSet = set(wordsList)

    def checkCompound(word):
        if word in dp:
            return dp[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if (prefix in wordsSet and suffix in wordsSet) or (prefix in wordsSet and checkCompound(suffix)):
                dp[word] = True
                return True
        dp[word] = False
        return False

    for word in wordsList:
        if checkCompound(word):
            if len(word) > len(longest):
                secondLongest = longest
                longest = word
            elif len(word) > len(secondLongest):
                secondLongest = word

    return f"Longest Compound Word: {longest}\nSecond Longest Compound Word: {secondLongest}"

fileName = input("Enter file name: ")
with open(fileName, 'r') as file:
    words = file.read().splitlines()

startTime = time.perf_counter()
solution = SearchLongestCompoundWord(words)
endTime = time.perf_counter()

print(solution)
print(f"Time taken to process file {fileName}: {(endTime - startTime) * 1000:.2f} ms")
