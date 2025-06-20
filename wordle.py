import time
start = time.time()

def likeness(word1, word2):
    green, yellow = [], []
    for i in range(5):
        if word1[i] == word2[i]:
            green.append(word1[i])
        elif word1[i] in word2:
            yellow.append(word1[i])
    for letter in yellow: # discard duplicate yellows
        word1Tot = yellow.count(letter) + green.count(letter)
        word2Tot = word2.count(letter)
        diff = word1Tot - word2Tot
        if diff > 0:
            for i in range(diff):
                yellow.remove(letter)
    score = (len(green)/5) + (len(yellow)/10)
    return score

def printTopN(dict, n):
    c = 0
    for key, value in dict.items():
        c += 1
        if c > n:  break
        print(c, key, value/2315)


answers = open("answers.txt").read().splitlines()
allowed = open("allowed.txt").read().splitlines()

print(len(allowed), len(answers))

tempDict = {}
for i in range(len(allowed)):
    allow = allowed[i]
    tempDict[allow] = 0
    for answer in answers:
        tempDict[allow] += likeness(allow, answer)
    if i % 1000 == 0:
        print(i, allow)
tempDict = dict(sorted(tempDict.items(), key = lambda item: item[1], reverse=True))

printTopN(tempDict, 10)
print(list(tempDict).index("stale"), "stale", tempDict["stale"])
print(list(tempDict).index("adieu"), "adieu", tempDict["adieu"])
print(list(tempDict).index("audio"), "audio", tempDict["audio"])

print(time.time()-start)